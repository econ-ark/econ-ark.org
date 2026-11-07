---
DOI: 10.5281/zenodo.22839070
abstract: An Econ-ARK REMARK that reimplements the monthly model of Korinek, Jones,
  Sacher, Cotter, and McCrory (2026) and records the twelve inputs, definitions, and
  orderings a reimplementation needs beyond the paper's text, most of which can be
  read from the authors' scenario explorer. The reimplementation agrees with the authors'
  scenario explorer in every series and month to rounding error and reproduces all
  226 published numbers within the paper's printed rounding. One script fails when
  any number stops reproducing.
authors:
- Alan Lujan
authors-original-paper:
- Anton Korinek
- Charles I. Jones
- Szymon Sacher
- Tess Cotter
- Peter McCrory
cff-version: 1.2.0
date-released: '2026-09-18'
doi: 10.5281/zenodo.22839070
keywords:
- artificial intelligence
- macroeconomic scenarios
- labor reallocation
- household saving
- reproduction
- Econ-ARK
license: MIT
message: If you use this REMARK, cite it as below.
redirect_from: []
references:
- authors:
  - family-names: Korinek
    given-names: Anton
  - family-names: Jones
    given-names: Charles I.
  - family-names: Sacher
    given-names: Szymon
  - family-names: Cotter
    given-names: Tess
  - family-names: McCrory
    given-names: Peter
  title: Economic Scenarios for Transformative AI
  type: report
  url: https://www.anthropic.com/institute/econ-scenarios
  year: 2026
remark-name: econ-scenarios
repository-code: https://github.com/econ-ark/econ-scenarios
tags:
- REMARK
- Reproduction
- Notebook
tier: 3
title: "Reproducing \u201CEconomic Scenarios for Transformative AI\u201D"
title-original-paper: Economic Scenarios for Transformative AI
type: software
version: 0.1.0
---

# Reproducing “Economic Scenarios for Transformative AI”

`reproduce.sh` installs the pinned environment with uv, downloads the public
data behind the calibration rechecks, runs the test suite that gates every table, figure, and
quoted number of the report and its supplement on the code, and builds the site. Nothing here
solves a household, so the whole path takes minutes. `reproduce_min.sh` runs the model's
internal identities, the published-number tables, and the quit order alone. The README describes
the report, the layout of the code, and what each check establishes.
