# TwiConv Explicit-Only Data

This directory is for locally generated TwiConv explicit-only `.rels` files and
their reproducibility notes. The `.rels` files are ignored by Git because they
contain protected Twitter/X data.

## Source Data

Start from existing DISRPT-style TwiConv `.rels` files:

```text
twiconv.pdtb_train.rels
twiconv.pdtb_dev.rels
twiconv.pdtb_test.rels
```

The source `.rels` files should already contain valid TwiConv relation rows in
the standard DISRPT relation-classification format.

## Explicit-Only Filtering

From the project root, run the filter once per split, replacing
`PATH_TO_TWICONV_RELS` with your local directory containing the full TwiConv
`.rels` files:

```bash
python3 scripts/filter_explicit_rels.py \
  --input PATH_TO_TWICONV_RELS/twiconv.pdtb_train.rels \
  --output data/eng.pdtb.twiconv_explicit/eng.pdtb.twiconv_explicit_train.rels
```

```bash
python3 scripts/filter_explicit_rels.py \
  --input PATH_TO_TWICONV_RELS/twiconv.pdtb_dev.rels \
  --output data/eng.pdtb.twiconv_explicit/eng.pdtb.twiconv_explicit_dev.rels
```

```bash
python3 scripts/filter_explicit_rels.py \
  --input PATH_TO_TWICONV_RELS/twiconv.pdtb_test.rels \
  --output data/eng.pdtb.twiconv_explicit/eng.pdtb.twiconv_explicit_test.rels
```

For a pooled target benchmark, concatenate the full split files or the
explicit-only split files with a single shared header. In this project, the
pooled explicit-only target file is named:

```text
data/eng.pdtb.twiconv_explicit_alltest/eng.pdtb.twiconv_explicit_alltest_test.rels
```

## Relation Types

| Split | **Explicit** | Implicit | Total |
|---|---:|---:|---:|
| train | **1,134** | 579 | 1,713 |
| dev | **144** | 76 | 220 |
| test | **137** | 74 | 211 |
| all-test | **1,415** | 729 | 2,144 |

Note: after filtering, only **explicit relations** remain.

## Explicit-Only Label Distribution

| Label | Train | Dev | Test | All-Test |
|---|---:|---:|---:|---:|
| conjunction | 330 | 42 | 35 | 407 |
| concession | 262 | 30 | 33 | 325 |
| causal | 159 | 20 | 24 | 203 |
| temporal | 151 | 17 | 9 | 177 |
| condition | 122 | 16 | 17 | 155 |
| explanation | 31 | 4 | 3 | 38 |
| contrast | 28 | 8 | 2 | 38 |
| alternation | 27 | 4 | 6 | 37 |
| mode | 14 | 2 | 3 | 19 |
| elaboration | 4 | 1 | 2 | 7 |
| purpose | 5 | 0 | 0 | 5 |
| reformulation | 1 | 0 | 3 | 4 |
| **Total** | **1,134** | **144** | **137** | **1,415** |
