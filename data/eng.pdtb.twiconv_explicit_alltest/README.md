# TwiConv Explicit-Only All-Test Data

This directory is for the pooled TwiConv explicit-only target benchmark. The
`.rels` file is ignored by Git because it contains protected Twitter/X data.

## Source Data

This corpus pools the explicit-only train, dev, and test rows from:

```text
data/eng.pdtb.twiconv_explicit/
```

It is intended for target-domain evaluation only, not for model training.

## Generated File

```text
eng.pdtb.twiconv_explicit_alltest_test.rels
```

The file uses `test` as its split name so DiscReT can consume it as an
evaluation corpus.

## Relation Types

| Split | **Explicit** | Implicit | Total |
|---|---:|---:|---:|
| all-test | **1,415** | 0 | 1,415 |

## Explicit-Only Label Distribution

| Label | All-Test |
|---|---:|
| conjunction | 407 |
| concession | 325 |
| causal | 203 |
| temporal | 177 |
| condition | 155 |
| explanation | 38 |
| contrast | 38 |
| alternation | 37 |
| mode | 19 |
| elaboration | 7 |
| purpose | 5 |
| reformulation | 4 |
| **Total** | **1,415** |

