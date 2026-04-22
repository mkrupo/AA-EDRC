# AA-EDRC

Repository for *Ambiguity-Aware Explicit Discourse Relation Classification*.

`sharedtask2025/` is included as a Git submodule and provides the DISRPT corpus
format and official restoration script.

## Setup

Clone with submodules:

```bash
git clone --recurse-submodules git@github.com:mkrupo/AA-EDRC.git>
```

If the repository was cloned without submodules, initialize them afterwards:

```bash
git submodule update --init --recursive
```

## Data

- [PDTB-3 explicit-only](data/pdtb/README.md)
- TwiConv explicit-only: pending regeneration/audit

## Scripts

- `scripts/filter_explicit_rels.py`: filter one DISRPT-style `.rels` file to
  rows where `rel_type == explicit`.
