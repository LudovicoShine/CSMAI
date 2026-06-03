#!/usr/bin/env python3
import argparse
from datetime import date
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Append usage feedback to REFERENCES/feedback_log.md.")
    parser.add_argument("--issue", required=True, help="Observed issue or feedback")
    parser.add_argument("--impact", required=True, help="Why it matters")
    parser.add_argument("--suggestion", required=True, help="Suggested change or action")
    parser.add_argument("--source", default="使用反馈", help="Feedback source")
    parser.add_argument("--status", default="待处理", help="Feedback status")
    parser.add_argument(
        "--log-file",
        default="REFERENCES/feedback_log.md",
        help="Path to feedback log, relative to skill root by default",
    )
    return parser.parse_args()


def escape_cell(value):
    return value.replace("|", "\\|").replace("\n", " ").strip()


def main():
    args = parse_args()
    skill_root = Path(__file__).resolve().parents[1]
    log_path = Path(args.log_file)
    if not log_path.is_absolute():
        log_path = skill_root / log_path

    row = "| {date} | {source} | {issue} | {impact} | {suggestion} | {status} |\n".format(
        date=date.today().isoformat(),
        source=escape_cell(args.source),
        issue=escape_cell(args.issue),
        impact=escape_cell(args.impact),
        suggestion=escape_cell(args.suggestion),
        status=escape_cell(args.status),
    )

    if not log_path.exists():
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(
            "# 使用反馈记录\n\n"
            "| 日期 | 来源 | 问题现象 | 影响 | 已采取动作 | 状态 |\n"
            "|---|---|---|---|---|---|\n",
            encoding="utf-8",
        )
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(row)
    print(str(log_path))


if __name__ == "__main__":
    main()
