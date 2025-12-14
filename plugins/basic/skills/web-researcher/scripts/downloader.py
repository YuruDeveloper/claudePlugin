#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests"]
# ///

"""
File Downloader for Web Researcher Skill
Downloads files to ./.claude/download/ in the current project
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote


def GetDownloadDir() -> Path:
    """Get or create the download directory"""
    DownloadDir = Path.cwd() / ".claude" / "download"
    DownloadDir.mkdir(parents=True, exist_ok=True)
    return DownloadDir


def ExtractFilename(Url: str, ContentDisposition: str | None = None) -> str:
    """Extract filename from URL or Content-Disposition header"""
    if ContentDisposition:
        Parts = ContentDisposition.split("filename=")
        if len(Parts) > 1:
            return Parts[1].strip('"\'')

    ParsedUrl = urlparse(Url)
    Filename = unquote(os.path.basename(ParsedUrl.path))

    if not Filename or Filename == "/":
        Filename = "downloaded_file"

    return Filename


def DownloadFile(Url: str, CustomFilename: str | None = None) -> dict:
    """
    Download a file from URL

    Args:
        Url: The URL to download from
        CustomFilename: Optional custom filename

    Returns:
        dict with status, path, and message
    """
    try:
        Response = requests.get(Url, stream=True, timeout=30)
        Response.raise_for_status()

        ContentDisposition = Response.headers.get("Content-Disposition")
        Filename = CustomFilename or ExtractFilename(Url, ContentDisposition)

        DownloadDir = GetDownloadDir()
        FilePath = DownloadDir / Filename

        # Handle duplicate filenames
        Counter = 1
        OriginalPath = FilePath
        while FilePath.exists():
            Stem = OriginalPath.stem
            Suffix = OriginalPath.suffix
            FilePath = DownloadDir / f"{Stem}_{Counter}{Suffix}"
            Counter += 1

        with open(FilePath, "wb") as File:
            for Chunk in Response.iter_content(chunk_size=8192):
                File.write(Chunk)

        return {
            "status": "success",
            "path": str(FilePath),
            "filename": FilePath.name,
            "size": FilePath.stat().st_size
        }

    except requests.exceptions.RequestException as Error:
        return {
            "status": "error",
            "message": str(Error)
        }


def Main():
    if len(sys.argv) < 2:
        print("Usage: downloader.py <url> [filename]")
        print("Downloads file to ./.claude/download/")
        sys.exit(1)

    Url = sys.argv[1]
    CustomFilename = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Downloading: {Url}")
    Result = DownloadFile(Url, CustomFilename)

    if Result["status"] == "success":
        print(f"Success: {Result['path']}")
        print(f"Size: {Result['size']} bytes")
    else:
        print(f"Error: {Result['message']}")
        sys.exit(1)


if __name__ == "__main__":
    Main()