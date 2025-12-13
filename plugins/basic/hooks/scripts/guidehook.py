#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
파일 작성/편집 가이드 제공 훅
파일 확장자에 따라 적절한 작성 가이드를 출력합니다.
"""

import sys
import json
import os
from pathlib import Path


# 플러그인 루트 디렉토리 (환경 변수에서 가져오거나 스크립트 위치 기준)
def get_plugin_dir() -> Path:
    """플러그인 디렉토리 경로 반환"""
    plugin_dir = os.environ.get("CLAUDE_PLUGIN_DIR")
    if plugin_dir:
        return Path(plugin_dir)
    # 환경 변수가 없으면 스크립트 위치 기준으로 계산
    # scripts/guidehook.py -> ../.. (plugins/basic/)
    return Path(__file__).parent.parent.parent


# 파일 확장자별 가이드 파일 매핑
GUIDE_MAPPING = {
    ".md": "md/guide/md-guide.md",
    ".json": "md/guide/json-guide.md",
    ".yaml": "md/guide/yaml-guide.md",
    ".yml": "md/guide/yaml-guide.md",
    ".sh": "md/guide/bash-guide.md",
    "Makefile": "md/guide/makefile-guide.md",
    ".mk": "md/guide/makefile-guide.md",
}

DEFAULT_GUIDE = "md/guide/code-guide.md"


def get_guide_file(file_path: str) -> str:
    """
    파일 경로에 따른 가이드 파일 경로 반환

    Args:
        file_path: 대상 파일 경로

    Returns:
        가이드 파일 경로
    """
    plugin_dir = get_plugin_dir()
    file_name = os.path.basename(file_path)

    # Makefile 체크
    if file_name.lower() == "makefile":
        return str(plugin_dir / GUIDE_MAPPING["Makefile"])

    # 확장자 체크
    ext = os.path.splitext(file_path)[1].lower()
    guide_file = GUIDE_MAPPING.get(ext, DEFAULT_GUIDE)

    return str(plugin_dir / guide_file)


def read_guide_file(guide_path: str) -> str:
    """
    가이드 파일 내용 읽기

    Args:
        guide_path: 가이드 파일 경로

    Returns:
        가이드 파일 내용
    """
    try:
        with open(guide_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"# Warning: Guide file not found at {guide_path}"
    except Exception as e:
        return f"# Error reading guide file: {e}"


def main() -> int:
    """
    메인 함수

    Returns:
        항상 0 (가이드는 차단하지 않음)
    """
    try:
        # stdin에서 JSON 읽기
        data = json.loads(sys.stdin.read())

        # Write 또는 Edit 도구가 아니면 통과
        tool_name = data.get("tool_name", "")
        if tool_name not in ["Write", "Edit"]:
            return 0

        # 파일 경로 추출
        file_path = data.get("tool_input", {}).get("file_path", "")
        if not file_path:
            return 0

        # 가이드 파일 경로 결정
        guide_path = get_guide_file(file_path)

        # 가이드 내용 읽어서 JSON 형식으로 출력 (Claude가 볼 수 있도록)
        guide_content = read_guide_file(guide_path)
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "permissionDecisionReason": guide_content
            }
        }
        print(json.dumps(output))

        return 0

    except json.JSONDecodeError as e:
        print(f"# ERROR: Invalid JSON input: {e}", file=sys.stderr)
        return 0  # 가이드는 에러가 있어도 차단하지 않음
    except Exception as e:
        print(f"# ERROR: Unexpected error: {e}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(main())