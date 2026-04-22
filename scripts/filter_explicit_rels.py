#!/usr/bin/env python3
"""Filter a DISRPT-style .rels file to explicit relations only."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path


RELS_HEADER = [
    "doc",
    "unit1_toks",
    "unit2_toks",
    "unit1_txt",
    "unit2_txt",
    "u1_raw",
    "u2_raw",
    "s1_toks",
    "s2_toks",
    "unit1_sent",
    "unit2_sent",
    "dir",
    "rel_type",
    "orig_label",
    "label",
]

REL_TYPE_INDEX = RELS_HEADER.index("rel_type")
LABEL_INDEX = RELS_HEADER.index("label")


def filter_explicit_rels(input_path: Path, output_path: Path) -> dict[str, object]:
    """Read one .rels file, keep rel_type == explicit rows, and write one .rels file."""
    lines = input_path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError(f"Input .rels file is empty: {input_path}")

    header = lines[0].split("\t")
    if header != RELS_HEADER:
        raise ValueError(f"Unexpected .rels header in {input_path}: {header}")

    output_lines = [lines[0]]
    source_rel_types: Counter[str] = Counter()
    explicit_label_counts: Counter[str] = Counter()

    for line_no, line in enumerate(lines[1:], start=2):
        if not line:
            continue
        fields = line.split("\t")
        if len(fields) != len(RELS_HEADER):
            raise ValueError(f"{input_path}:{line_no}: expected 15 tab-separated fields, found {len(fields)}")

        rel_type = fields[REL_TYPE_INDEX]
        source_rel_types[rel_type] += 1
        if rel_type != "explicit":
            continue

        output_lines.append(line)
        explicit_label_counts[fields[LABEL_INDEX]] += 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(output_lines) + "\n", encoding="utf-8")

    return {
        "input": str(input_path),
        "output": str(output_path),
        "source_rows": sum(source_rel_types.values()),
        "source_rel_type_counts": dict(source_rel_types),
        "explicit_rows": sum(explicit_label_counts.values()),
        "explicit_label_counts": dict(explicit_label_counts),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Input DISRPT-style .rels file.")
    parser.add_argument("--output", required=True, type=Path, help="Output explicit-only .rels file.")
    args = parser.parse_args()

    summary = filter_explicit_rels(args.input, args.output)
    print(f"Wrote {summary['explicit_rows']} explicit rows to {summary['output']}")
    print(f"Source relation types: {summary['source_rel_type_counts']}")
    print(f"Explicit label counts: {summary['explicit_label_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
