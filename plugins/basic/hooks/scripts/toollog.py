#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
도구 사용 로그 기록 훅 (PostToolUse)
모든 도구 호출을 JSON 형식으로 기록합니다.
"""

import sys
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


def get_log_file_path(cwd: str) -> Path:
    """
    로그 파일 경로 반환

    Args:
        cwd: 현재 작업 디렉토리

    Returns:
        로그 파일 경로
    """
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", cwd)
    log_dir = Path(project_dir) / ".claude"
    log_dir.mkdir(parents=True, exist_ok=True)
    return log_dir / "tools.json"


def load_logs(log_file: Path) -> List[Dict[str, Any]]:
    """
    기존 로그 파일 읽기

    Args:
        log_file: 로그 파일 경로

    Returns:
        로그 엔트리 리스트
    """
    if not log_file.exists():
        return []

    try:
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        # 손상된 JSON 파일은 빈 배열로 시작
        return []
    except Exception:
        return []


def save_logs(log_file: Path, logs: List[Dict[str, Any]]) -> None:
    """
    로그 파일에 저장

    Args:
        log_file: 로그 파일 경로
        logs: 저장할 로그 엔트리 리스트
    """
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)


def extract_tool_info(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    도구 정보를 로그용으로 추출

    Args:
        data: PostToolUse hook에서 받은 데이터

    Returns:
        로그에 저장할 정보
    """
    tool_name = data.get("tool_name", "Unknown")
    tool_input = data.get("tool_input", {})
    tool_response = data.get("tool_response", {})

    # 기본 로그 엔트리
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "tool_name": tool_name,
        "session_id": data.get("session_id"),
        "tool_use_id": data.get("tool_use_id"),
    }

    # 도구별 중요 정보 추출
    if tool_name == "Bash":
        log_entry["command"] = tool_input.get("command")
        log_entry["description"] = tool_input.get("description")
        log_entry["exit_code"] = tool_response.get("exitCode")

    elif tool_name in ["Read", "Write", "Edit"]:
        log_entry["file_path"] = tool_input.get("file_path")
        log_entry["success"] = tool_response.get("success")

    elif tool_name == "Grep":
        log_entry["pattern"] = tool_input.get("pattern")
        log_entry["path"] = tool_input.get("path")
        log_entry["output_mode"] = tool_input.get("output_mode")

    elif tool_name == "Glob":
        log_entry["pattern"] = tool_input.get("pattern")
        log_entry["path"] = tool_input.get("path")

    elif tool_name == "Task":
        log_entry["subagent_type"] = tool_input.get("subagent_type")
        log_entry["description"] = tool_input.get("description")

    elif tool_name == "WebFetch":
        log_entry["url"] = tool_input.get("url")

    elif tool_name == "WebSearch":
        log_entry["query"] = tool_input.get("query")

    else:
        # 기타 도구는 전체 input 저장
        log_entry["tool_input"] = tool_input

    return log_entry


def main() -> int:
    """
    메인 함수

    Returns:
        항상 0 (로그는 실행을 방해하지 않음)
    """
    try:
        # stdin에서 JSON 읽기
        data = json.loads(sys.stdin.read())

        # 작업 디렉토리
        cwd = data.get("cwd", os.getcwd())

        # 로그 파일 경로
        log_file = get_log_file_path(cwd)

        # 기존 로그 로드
        logs = load_logs(log_file)

        # 새 로그 엔트리 추가
        log_entry = extract_tool_info(data)
        logs.append(log_entry)

        # 최근 1000개만 유지 (파일 크기 관리)
        if len(logs) > 1000:
            logs = logs[-1000:]

        # 로그 저장
        save_logs(log_file, logs)

        return 0

    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON input: {e}", file=sys.stderr)
        return 0  # 로그 실패해도 실행은 계속
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(main())