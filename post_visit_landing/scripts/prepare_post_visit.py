#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


FUZZY_PATTERNS = [
    r"\[听不清\]",
    r"\[不清楚\]",
    r"\[模糊\]",
    r"\?\?\?",
]

VALID_QUALITIES = ("完整清晰", "部分模糊", "碎片化")


def read_text(path_str: Optional[str]) -> str:
    if not path_str:
        return ""
    path = Path(path_str)
    return path.read_text(encoding="utf-8")


def count_fuzzy_markers(text: str) -> Tuple[int, Dict[str, int]]:
    detail = {}
    total = 0
    for pattern in FUZZY_PATTERNS:
        matches = re.findall(pattern, text)
        detail[pattern] = len(matches)
        total += len(matches)
    return total, detail


def infer_quality(char_count: int, fuzzy_count: int) -> str:
    if char_count < 1200 or fuzzy_count >= 12:
        return "碎片化"
    if 1200 <= char_count < 2500 or 3 <= fuzzy_count < 12:
        return "部分模糊"
    return "完整清晰"


def should_manual_review(
    inferred_quality: str,
    char_count: int,
    fuzzy_count: int,
    has_annotations: bool,
) -> bool:
    boundary_hit = (
        char_count in {1200, 2500}
        or fuzzy_count in {3, 12}
        or abs(char_count - 1200) <= 50
        or abs(char_count - 2500) <= 50
        or fuzzy_count in {2, 11}
    )
    return boundary_hit or not has_annotations or inferred_quality != "完整清晰"


def build_notes(
    inferred_quality: str,
    has_annotations: bool,
    manual_override: Optional[str],
) -> List[str]:
    notes = []
    if not has_annotations:
        notes.append("未提供 csm_annotations，建议人工补充现场认可/否定/新增场景。")
    if inferred_quality != "完整清晰":
        notes.append("录音文本存在模糊或碎片化信号，建议人工复核 transcript_quality。")
    if manual_override:
        notes.append("最终 transcript_quality 使用手动传入值；自动判断结果保留在 transcript_quality_signals。")
    return notes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare normalized Post-Visit payload from transcript and optional notes."
    )
    parser.add_argument("--transcript-file", required=True, help="Path to transcript .txt or .md file")
    parser.add_argument("--annotations-file", help="Optional path to CSM annotations file")
    parser.add_argument("--skill1-output-file", help="Optional path to Pre-Visit output file")
    parser.add_argument("--meeting-date", help="Optional meeting date, e.g. 2026-06-02")
    parser.add_argument("--customer-industry", help="Optional customer industry")
    parser.add_argument(
        "--transcript-quality",
        choices=VALID_QUALITIES,
        help="Optional manual override for transcript_quality",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    transcript = read_text(args.transcript_file).strip()
    if not transcript:
        print("transcript file is empty", file=sys.stderr)
        return 1

    annotations = read_text(args.annotations_file).strip()
    skill1_output = read_text(args.skill1_output_file).strip()

    char_count = len(transcript)
    fuzzy_count, fuzzy_detail = count_fuzzy_markers(transcript)
    inferred_quality = infer_quality(char_count, fuzzy_count)
    final_quality = args.transcript_quality or inferred_quality
    has_annotations = bool(annotations)
    needs_manual_review = should_manual_review(
        inferred_quality=inferred_quality,
        char_count=char_count,
        fuzzy_count=fuzzy_count,
        has_annotations=has_annotations,
    )

    payload = {
        "transcript": transcript,
        "transcript_quality": final_quality,
        "transcript_quality_signals": {
            "inferred_quality": inferred_quality,
            "char_count": char_count,
            "fuzzy_marker_count": fuzzy_count,
            "fuzzy_marker_detail": fuzzy_detail,
            "manual_override": args.transcript_quality or "",
        },
        "csm_annotations": annotations,
        "skill1_output": skill1_output,
        "meeting_date": args.meeting_date or "",
        "customer_industry": args.customer_industry or "",
        "needs_manual_review": needs_manual_review,
        "notes": build_notes(
            inferred_quality=inferred_quality,
            has_annotations=has_annotations,
            manual_override=args.transcript_quality,
        ),
    }

    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
