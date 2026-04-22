# PDTB-3 Explicit-Only Data

This directory is for locally generated PDTB-3 explicit-only `.rels` files and
their reproducibility notes. The `.rels` files are ignored by Git because the
restored Wall Street Journal text is protected data.

## Source Data

Use the DISRPT shared-task PDTB-3 corpus:

```text
sharedtask2025/data/eng.pdtb.pdtb/
```

The shared-task repository ships PDTB-3 with underscore placeholders. Restore
the text first with the official DISRPT script:

```bash
cd sharedtask2025/utils
python3 process_underscore_2025.py -c eng.pdtb.pdtb -m add
```

When prompted, provide the local raw WSJ/PDTB path.

The restoration step updates `.rels`, `.tok`, and `.conllu` in the shared-task
PDTB directory. For this project, we only copy/filter `.rels` files.

## Explicit-Only Filtering

From the project root, run:

```bash
python3 scripts/filter_explicit_rels.py \
  --input sharedtask2025/data/eng.pdtb.pdtb/eng.pdtb.pdtb_train.rels \
  --output data/pdtb/eng.pdtb.pdtb_explicit_train.rels
```

```bash
python3 scripts/filter_explicit_rels.py \
  --input sharedtask2025/data/eng.pdtb.pdtb/eng.pdtb.pdtb_dev.rels \
  --output data/pdtb/eng.pdtb.pdtb_explicit_dev.rels
```

```bash
python3 scripts/filter_explicit_rels.py \
  --input sharedtask2025/data/eng.pdtb.pdtb/eng.pdtb.pdtb_test.rels \
  --output data/pdtb/eng.pdtb.pdtb_explicit_test.rels
```

## Relation Types

| Split | **Explicit** | Implicit | AltLex | AltLexC | Hypophora | Total |
|---|---:|---:|---:|---:|---:|---:|
| train | **19,925** | 18,108 | 1,264 | 108 | 119 | 39,524 |
| dev | **2,030** | 1,796 | 112 | 17 | 18 | 3,973 |
| test | **2,227** | 1,922 | 122 | 15 | 9 | 4,295 |

Note: after filtering, only **explicit relations** remain.

## Explicit-Only Label Distribution

| Label | Train | Dev | Test |
|---|---:|---:|---:|
| conjunction | 7,187 | 756 | 788 |
| concession | 3,918 | 412 | 448 |
| temporal | 3,328 | 311 | 419 |
| causal | 1,597 | 166 | 174 |
| condition | 1,340 | 122 | 133 |
| contrast | 1,151 | 104 | 115 |
| elaboration | 473 | 52 | 55 |
| mode | 324 | 37 | 28 |
| purpose | 320 | 23 | 38 |
| alternation | 241 | 39 | 24 |
| explanation | 24 | 6 | 2 |
| reformulation | 22 | 2 | 3 |
| **Total** | **19,925** | **2,030** | **2,227** |
