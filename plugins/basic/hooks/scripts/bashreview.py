#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
Bash 명령어 보안 검사 훅
위험한 명령어를 실행 전에 차단합니다.
"""

import sys
import json
import re
from typing import Dict, Tuple


# 위험한 명령어 패턴과 메시지 정의
DANGEROUS_PATTERNS: Dict[str, str] = {
    r'rm\s+-[^\s]*r[^\s]*f|rm\s+-[^\s]*f[^\s]*r': '"rm -rf" is dangerous',
    r'chmod': '"chmod" is not allowed',
    r'curl.*\|.*bash|wget.*\|.*sh': 'remote shell direct run is dangerous',
    r'shutdown': '"shutdown" is not allowed',
    r'reboot': '"reboot" is not allowed',
    r'poweroff': '"poweroff" is not allowed',
    r'halt': '"halt" is not allowed',
    r'export': '"export" is not allowed',
    r'unset': '"unset" is not allowed',
    r'mkfs': '"mkfs" is not allowed',
    r'init 0': '"init 0" is not allowed',
    r'history\s+-c|rm.*\.bash_history': '"history delete" is not allowed',
    r'fdisk': '"fdisk" is not allowed',
    r'dd if=/dev/zero': '"dd if=/dev/zero" is not allowed',
    r':\(\)\{ :\|:& \};:': 'Fork bomb is not allowed',
    r'while true; do': '"infinite loop" is not allowed',
}


def check_dangerous_command(command: str) -> Tuple[bool, str]:
    """
    명령어가 위험한 패턴을 포함하는지 검사

    Args:
        command: 검사할 명령어

    Returns:
        (is_dangerous, error_message) 튜플
    """
    for pattern, message in DANGEROUS_PATTERNS.items():
        if re.search(pattern, command):
            return True, message
    return False, ""


def main() -> int:
    """
    메인 함수

    Returns:
        0: 통과, 2: 차단
    """
    try:
        # stdin에서 JSON 읽기
        data = json.loads(sys.stdin.read())

        # Bash 도구가 아니면 통과
        tool_name = data.get("tool_name", "")
        if tool_name != "Bash":
            return 0

        # 명령어 추출
        command = data.get("tool_input", {}).get("command", "")
        if not command:
            return 0

        # 위험한 명령어 검사
        is_dangerous, error_message = check_dangerous_command(command)
        if is_dangerous:
            print(f"BLOCK: {error_message}", file=sys.stderr)
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