#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
파일 읽기 보안 검사 훅
민감한 파일 읽기를 차단합니다.
"""

import sys
import json
import re


# 민감한 파일 패턴들
SENSITIVE_PATTERNS = [
    r'\.env',
    r'credentials',
    r'secrets',
    r'\.ssh/',
    r'\.pem$',
    r'\.key$',
    r'token',
    r'api_key',
]


def is_sensitive_file(file_path: str) -> bool:
    """
    파일 경로가 민감한 파일인지 검사

    Args:
        file_path: 검사할 파일 경로

    Returns:
        민감한 파일이면 True
    """
    for pattern in SENSITIVE_PATTERNS:
        if re.search(pattern, file_path):
            return True
    return False


def main() -> int:
    """
    메인 함수

    Returns:
        0: 통과, 2: 차단
    """
    try:
        # stdin에서 JSON 읽기
        data = json.loads(sys.stdin.read())

        # Read 도구가 아니면 통과
        tool_name = data.get("tool_name", "")
        if tool_name != "Read":
            return 0

        # 파일 경로 추출
        file_path = data.get("tool_input", {}).get("file_path", "")
        if not file_path:
            return 0

        # 민감한 파일 검사
        if is_sensitive_file(file_path):
            print("BLOCK: Sensitive configuration files cannot be read", file=sys.stderr)
            return 2

        return 0

    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON input: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())