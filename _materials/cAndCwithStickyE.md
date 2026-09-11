---
abstract: A Replication of Sticky Expectations and Consumption Dynamics.
authors:
- family-names: Carroll
  given-names: Christopher D.
  orcid: https://orcid.org/0000-0003-3732-9312
- family-names: Crawley
  given-names: Edmund
- family-names: Slacalek
  given-names: Jiri
- family-names: Kiichi
  given-names: Tokuoka
- family-names: White
  given-names: Matthew
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
redirect_from:
- /_materials/candcwithstickye
- /_materials/candcwithstickyE
- /_materials/candcwithStickye
- /_materials/candcwithStickyE
- /_materials/candCwithstickye
- /_materials/candCwithstickyE
- /_materials/candCwithStickye
- /_materials/candCwithStickyE
- /_materials/cAndcwithstickye
- /_materials/cAndcwithstickyE
- /_materials/cAndcwithStickye
- /_materials/cAndcwithStickyE
- /_materials/cAndCwithstickye
- /_materials/cAndCwithstickyE
- /_materials/cAndCwithStickye
references:
- authors:
  - family-names: Carroll
    given-names: Christopher D.
    orcid: https://orcid.org/0000-0003-3732-9312
  - family-names: Crawley
    given-names: Edmund
  - family-names: Slacalek
    given-names: Jiri
  - family-names: Kiichi
    given-names: Tokuoka
  - family-names: White
    given-names: Matthew N.
  date-released: 2020-07-01
  doi: 10.1257/mac.20180286
  publisher:
    name: 'American Economic Journal: Macroeconomics'
  title: Sticky Expectations and Consumption Dynamics
  type: article
remark-name: cAndCwithStickyE
repository-code: https://github.com/econ-ark/cAndCwithStickyE
tags:
- REMARK
- Reproduction
title: Sticky Expectations and Consumption Dynamics
---

# cAndCwithStickyE is a Reproduction

This is a reproduction of the results in the paper "Sticky Expectations and Consumption Dynamics" by Carroll, Crawley, Slacalek, Tokuoka, and White. The [html version](http://econ.jhu.edu/people/ccarroll/papers/cAndCwithStickyE) contains links to resources including the PDF version, the presentation slides, a repo containing the paper and code, and related material

The root directory contains three files:

* `do_min.py` executes the representative agent version of the model
* `do_mid.py` reproduces some of the core results of the paper
* `do_all.py` reproduces all computational results in the paper

Any of these can be run using ipython from the command line, for example:

ipython do_min.py

In all cases, there should be a message that indicates how long it takes to run the code on a particular computer with a particular configuration.

## References

Carroll, C. D., Crawley, E., Slacalek, J., Tokuoka, K., & White, M. N. (2020). Sticky expectations and consumption dynamics. American economic journal: macroeconomics, 12(3), 40-76.

