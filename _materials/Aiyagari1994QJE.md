---
abstract: 'This repository computes the stationary equilibrium of Aiyagari''s (1994)
  economy, "Uninsured Idiosyncratic Risk and Aggregate Saving", for every cell of
  its Table II, with two toolkits: HARK''s (Heterogeneous Agents Resources and toolKit)
  MarkovConsumerType, and dolo with DolARK, its extension to heterogeneous agents.
  Both solve Aiyagari''s own economy, his seven-state Tauchen chain for income, and
  one code computes both toolkits'' stationary populations, on a grid of its own.
  At converged settings the two agree to within a few thousandths of a percentage
  point; Aiyagari''s published values differ from both by up to 0.26 percentage points.
  Results of record for each toolkit at each level of settings are in table-ii/. For
  the baseline calibration, the HARK notebook also draws the consumption functions,
  the wealth distribution and the supply of and demand for capital, and saves those
  figures and the economy''s key numbers. The HARK computation is also a Python package,
  aiyagari1994qje, that other programs can install to compute the same numbers.'
authors:
- affiliation: Johns Hopkins University
  email: edwardsadam01@gmail.com
  family-names: Edwards
  given-names: Adam
cff-version: 1.2.0
date-released: 2026-11-24
github_repo_url: https://github.com/econ-ark/Aiyagari1994QJE
keywords:
- heterogeneous agents
- incomplete markets
- precautionary saving
- stationary equilibrium
- HARK
- dolo
license: Apache-2.0
message: If you use this software, please cite it as below.
notebooks:
- AiyagariMarkovHARK.ipynb
- AiyagariDolARK.ipynb
redirect_from:
- /materials/aiyagari1994QJE/
- /materials/Aiyagari1994qje/
- /materials/Aiyagari1994QJE/
references:
- authors:
  - family-names: Aiyagari
    given-names: S. Rao
  doi: 10.2307/2118417
  end: 684
  issue: 3
  journal: The Quarterly Journal of Economics
  publisher:
    name: Oxford University Press
  start: 659
  title: Uninsured idiosyncratic risk and aggregate saving
  type: article
  url: https://academic.oup.com/qje/article-abstract/109/3/659/1838287
  volume: 109
  year: 1994
remark-name: Aiyagari1994QJE
repository-code: https://github.com/econ-ark/Aiyagari1994QJE
tags:
- REMARK
- Replication
- Notebook
tier: 2
title: 'Aiyagari (1994QJE): Uninsured Idiosyncratic Risk and Aggregate Saving - Computational
  Implementation'
title-original-paper: Uninsured idiosyncratic risk and aggregate saving
type: software
url: https://github.com/econ-ark/Aiyagari1994QJE
version: 2.0.0
---

# Abstract

This REMARK computes the stationary equilibrium of Aiyagari's (1994) economy, in which households facing uninsurable
income risk and a borrowing limit save more than they would with complete markets, raising capital and lowering the
interest rate. It reproduces every cell of his Table II with two toolkits, HARK's `MarkovConsumerType` and dolo with
DolARK, given one economy, his seven-state Tauchen chain for income, and one code for the stationary population of
households. At its most refined settings the two toolkits' interest rates agree to within 0.00024 percentage points
across the table; Aiyagari's published values differ from both by up to 0.26 percentage points, most where income is
persistent and volatile and households averse to risk.

The REMARK's first version reproduced Aiyagari's baseline within 0.02 percentage points because two numerical errors
cancelled: a coarse grid for the household's rule overstated saving, and a simulation too short to reach the
stationary distribution understated it. The HARK notebook shows both, and the DolARK notebook shows how its first
version solved a different economy. For the baseline calibration the HARK notebook draws the consumption functions,
the distribution of wealth and the market for capital, and saves them with the economy's numbers for other documents
to use; the HARK computation is also an installable Python package, `aiyagari1994qje`.

# What it establishes

- Table II's stationary equilibria, converged: each toolkit's solution at named levels of settings in `table-ii/`,
  with diagnostics that need no reference solution.
- That two toolkits agree once they solve one economy with one population code, and that the remaining gaps from
  Aiyagari's table are his numerical solution's, not the model's.
- An exact statement of the economy, with a register of the conventions that made two solutions differ
  ([`docs/model.md`](docs/model.md)), from which a comparison of toolkits can start.

# Using it

The [README](README.md) explains how to reproduce the results with Docker, with uv, with conda or on Binder, what
each file is for, and how to use the package and the baseline's figures and numbers in another program. The HARK
notebook runs in about 15 minutes and the DolARK notebook, at its default level, in about 10 more.

# For teaching

**Prerequisites:** graduate macroeconomic theory (dynamic programming, the consumption-saving problem, competitive
equilibrium), some Python, and Markov chains.

**What a student learns:** to define a stationary equilibrium with heterogeneous households and incomplete markets,
and to say why its interest rate lies below the rate of time preference; to solve a household's problem under
uninsurable risk with HARK and with dolo; to compute a stationary distribution by simulation and directly, and to
recognize the errors of each; and to tell a numerical solution's error from a model's property, by converging
settings, comparing toolkits, and reading a published table as one computation among others. The HARK notebook ends
with exercises: no risk, other chains, the simulation's sampling error, the saving-rate identity, and who is
constrained.
