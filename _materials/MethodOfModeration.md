---
abstract: "In a risky world, a pessimist assumes the worst will happen. Someone who\
  \ ignores risk altogether is an optimist. Consumption decisions are mathematically\
  \ simple for both the pessimist and the optimist because both behave as if they\
  \ live in a riskless world. A realist (someone who wants to respond optimally to\
  \ risk) faces a much more difficult problem, but (under standard conditions) will\
  \ choose a level of spending somewhere between the pessimist\u2019s and the optimist\u2019\
  s. We use this fact to redefine the space in which the realist searches for optimal\
  \ consumption rules: we interpolate the logit of a moderation ratio that records\
  \ where between those two rules the realist lies. The resulting solution accurately\
  \ represents the numerical consumption rule over the entire interval of feasible\
  \ wealth values with remarkably few computations: on five gridpoints the approximation\
  \ is accurate throughout, and beyond the last of them it is more than an order of\
  \ magnitude more accurate than the endogenous gridpoints method, because it cannot\
  \ leave the bounds. The construction carries over to the value function, to an artificial\
  \ borrowing constraint, to risky returns, and to the standard incomplete-markets\
  \ models written in assets, where the bracket is formed within each income state.\
  \ Applied to the portfolio share it needs one change: the share\u2019s upper bound\
  \ is a constraint attained at finite wealth rather than approached asymptotically,\
  \ so the transform that straightens it is the logarithm of the moderation ratio\
  \ and not the logit, and the bracket is formed by a single limiting investor together\
  \ with the leverage constraint."
authors:
- address: Baltimore, MD
  affiliation: Johns Hopkins University
  family-names: Carroll
  given-names: Christopher D.
  orcid: 0000-0003-3732-9312
- affiliation: Reserve Bank of New Zealand
  family-names: Chipeniuk
  given-names: Karsten
- address: Baltimore, MD
  affiliation: Johns Hopkins University
  email: alujan@jhu.edu
  family-names: Lujan
  given-names: Alan
  orcid: 0000-0002-5289-7054
- affiliation: Japanese Ministry of Finance
  family-names: Tokuoka
  given-names: Kiichi
- address: Washington, DC
  affiliation: Fannie Mae
  family-names: Wu
  given-names: Weifeng
cff-version: 1.2.0
contact:
- address: Baltimore, MD
  affiliation: Johns Hopkins University
  email: alujan@jhu.edu
  family-names: Lujan
  given-names: Alan
  orcid: 0000-0002-5289-7054
github_repo_url: https://github.com/econ-ark/method-of-moderation
keywords:
- Dynamic Stochastic Optimization
- Consumption-Saving Models
- Numerical Methods
- Endogenous Gridpoints Method
- Precautionary Saving
- Bounded Approximation
- Extrapolation
license: CC-BY-SA-3.0
license-url: https://creativecommons.org/licenses/by-sa/3.0/
message: Please cite the following works when using this project.
notebooks:
- code/method-of-moderation.md
redirect_from:
- /materials/method-of-moderation/
- /materials/methodofModeration/
- /materials/methodOfmoderation/
- /materials/methodOfModeration/
- /materials/Methodofmoderation/
- /materials/MethodofModeration/
- /materials/MethodOfmoderation/
- /materials/MethodOfModeration/
remark-name: MethodOfModeration
remark-version: '1.0'
repository: https://github.com/econ-ark/method-of-moderation
tags:
- REMARK
- Notebook
title: The Method of Moderation
---

# The Method of Moderation

A technique for solving consumption-saving models that uses analytical
optimist and pessimist bounds to produce numerically stable approximations
with guaranteed theoretical properties.

## References

Carroll, Christopher D., Karsten Chipeniuk, Alan Lujan, Kiichi Tokuoka, and Weifeng Wu.
"The Method of Moderation."
