---
abstract: "Heterogeneous-agent models with multiple decisions face a computational\
  \ dilemma. Joint optimization over all choices is slow; strong separability restrictions\
  \ speed computation but rule out economically interesting interactions. I introduce\
  \ Sequential EGM (EGM^n), which eases this tension by decomposing the problem into\
  \ sequential stages so that each stage can exploit the Endogenous Grid Method\u2019\
  s closed-form inversion, chaining speed gains across decisions wherever separable\
  \ utility or an invertible transition permits it. The resulting curvilinear grids\
  \ require interpolation that respects their structure, so I develop ENGINE (ENdogenous\
  \ Grid INterpolation and Extrapolation), which exploits the index structure inherited\
  \ from exogenous grids, with no construction step and no triangulation. In the canonical\
  \ liquid-illiquid household block, EGM^n solves an order of magnitude faster than\
  \ the nested method in serial and 3.7 to 7.9 times faster at sixteen threads. Replacing\
  \ existing curvilinear interpolation with ENGINE cuts full-solve time 2.8- to 4.5-fold\
  \ at matched accuracy."
authors:
- affiliation: Johns Hopkins University
  city: Washington
  email: alujan@jhu.edu
  family-names: Lujan
  given-names: Alan
  orcid: 0000-0002-5289-7054
  region: DC
  website: https://advanced.jhu.edu/directory/alan-lujan/
cff-version: 1.2.0
contact:
- affiliation: Johns Hopkins University
  city: Washington
  email: alujan@jhu.edu
  family-names: Lujan
  given-names: Alan
  orcid: 0000-0002-5289-7054
  region: DC
  website: https://advanced.jhu.edu/directory/alan-lujan/
date-released: '2026-10-10'
keywords:
- endogenous grid method
- dynamic programming
- interpolation
- computational economics
license: CC-BY-NC-ND-4.0
license-url: https://creativecommons.org/licenses/by-nc-nd/4.0/
message: Please cite the following works when using this project.
notebooks:
- code/examples/example_ConsumptionLabor.md
- code/examples/example_TwoAssetHousehold.md
- code/examples/example_HealthInvestment.md
- code/examples/example_ENGINEInterpolation.md
redirect_from:
- /materials/sequentialEGM/
- /materials/Sequentialegm/
- /materials/SequentialEGM/
remark-name: SequentialEGM
remark-version: '1.0'
repository: https://github.com/alanlujan91/sequential_egm
tags:
- REMARK
- Notebook
tier: 2
title: The Sequential Endogenous Grid Method
---

# The Sequential Endogenous Grid Method

<!-- [[[cog
import pathlib
import yaml
front = pathlib.Path("content/paper/egmn_paper_only.md").read_text().split("---")[1]
cog.outl(yaml.safe_load(front)["parts"]["abstract"])
]]] -->
Heterogeneous-agent models with multiple decisions face a computational dilemma. Joint optimization over all choices is slow; strong separability restrictions speed computation but rule out economically interesting interactions. I introduce Sequential EGM (EGM$^n$), which eases this tension by decomposing the problem into sequential stages so that each stage can exploit the Endogenous Grid Method's closed-form inversion, chaining speed gains across decisions wherever separable utility or an invertible transition permits it. The resulting curvilinear grids require interpolation that respects their structure, so I develop ENGINE (ENdogenous Grid INterpolation and Extrapolation), which exploits the index structure inherited from exogenous grids, with no construction step and no triangulation. In the canonical liquid-illiquid household block, EGM$^n$ solves an order of magnitude faster than the nested method in serial and $3.7$ to $7.9$ times faster at sixteen threads. Replacing existing curvilinear interpolation with ENGINE cuts full-solve time $2.8$- to $4.5$-fold at matched accuracy.
<!-- [[[end]]] -->

## Reproduction

- `reproduce.sh` regenerates every table, figure and quoted reading of the paper and
  online appendix into `content/figures/`, one command per row of the exhibit table in
  `code/README.md`.
- `reproduce_min.sh` runs the test suite and builds the website with every example
  notebook executed, in a few minutes.

Both scripts install the locked environment with `uv sync --locked` first.

## Reference

Lujan, Alan. "The Sequential Endogenous Grid Method." Working paper. See `CITATION.cff`.
