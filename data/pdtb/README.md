# PDTB-3 Explicit-Only Data

This directory is for locally generated PDTB-3 explicit-only `.rels` files and
their reproducibility notes. The `.rels` files are ignored by Git because the
restored Wall Street Journal text is protected data.

## Source Data

Use the DISRPT shared-task PDTB-3 corpus:

```text
../sharedtask2025/data/eng.pdtb.pdtb/
```

The shared-task repository ships PDTB-3 with underscore placeholders. Restore
the text first with the official DISRPT script:

```bash
cd ../sharedtask2025/utils
python3 process_underscore_2025.py -c eng.pdtb.pdtb -m add
```

When prompted, provide the local raw WSJ/PDTB path.

The restoration step updates `.rels`, `.tok`, and `.conllu` in the shared-task
PDTB directory. For this project, we only copy/filter `.rels` files.

## Explicit-Only Filtering

From the project root, run:

```bash
python3 scripts/filter_explicit_rels.py \
  --input ../sharedtask2025/data/eng.pdtb.pdtb/eng.pdtb.pdtb_train.rels \
  --output data/pdtb/eng.pdtb.pdtb_explicit_train.rels
```

```bash
python3 scripts/filter_explicit_rels.py \
  --input ../sharedtask2025/data/eng.pdtb.pdtb/eng.pdtb.pdtb_dev.rels \
  --output data/pdtb/eng.pdtb.pdtb_explicit_dev.rels
```

```bash
python3 scripts/filter_explicit_rels.py \
  --input ../sharedtask2025/data/eng.pdtb.pdtb/eng.pdtb.pdtb_test.rels \
  --output data/pdtb/eng.pdtb.pdtb_explicit_test.rels
```

## Relation Types

| Split | Explicit | Implicit | AltLex | AltLexC | Hypophora | Total |
|---|---:|---:|---:|---:|---:|---:|
| train | 19,925 | 18,108 | 1,264 | 108 | 119 | 39,524 |
| dev | 2,030 | 1,796 | 112 | 17 | 18 | 3,973 |
| test | 2,227 | 1,922 | 122 | 15 | 9 | 4,295 |

Note: after filtering, only **explicit relations** remain.

## Explicit-Only Label Distribution

### Train

| Label | Count |
|---|---:|
| conjunction | 7,187 |
| concession | 3,918 |
| temporal | 3,328 |
| causal | 1,597 |
| condition | 1,340 |
| contrast | 1,151 |
| elaboration | 473 |
| mode | 324 |
| purpose | 320 |
| alternation | 241 |
| explanation | 24 |
| reformulation | 22 |
| **Total** | **19,925** |

### Dev

| Label | Count |
|---|---:|
| conjunction | 756 |
| concession | 412 |
| temporal | 311 |
| causal | 166 |
| condition | 122 |
| contrast | 104 |
| elaboration | 52 |
| alternation | 39 |
| mode | 37 |
| purpose | 23 |
| explanation | 6 |
| reformulation | 2 |
| **Total** | **2,030** |

### Test

| Label | Count |
|---|---:|
| conjunction | 788 |
| concession | 448 |
| temporal | 419 |
| causal | 174 |
| condition | 133 |
| contrast | 115 |
| elaboration | 55 |
| purpose | 38 |
| mode | 28 |
| alternation | 24 |
| reformulation | 3 |
| explanation | 2 |
| **Total** | **2,227** |
