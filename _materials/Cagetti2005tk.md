---
authors:
- affiliation: Johns Hopkins University
  email: rzheng21@jh.edu
  family-names: Zheng
  given-names: Rudan
cff-version: 1.2.0
github_repo_url: https://github.com/rzheng2112/Cagetti2005tk
keywords:
- Entrepreneurship
- Wealth
- Occupational choice
- Heterogeneous agents
license: Apache-2.0
message: If you use this repository, please cite it using the metadata below. When
  referring to the economic model, cite the preferred citation (journal article).
notebooks:
- Cagetti2005tk_material/cagetti2005_theory_reproduction.ipynb
- Cagetti2005tk_material/Cagetti2005-tk_intro.ipynb
- Cagetti2005tk_material/Cagetti2005-tk_prior-literature.ipynb
- Cagetti2005tk_material/Cagetti2005-tk_summary.ipynb
- Cagetti2005tk_material/Cagetti2005-tk_subsequent-literature.ipynb
- Cagetti2005tk_material/Cagetti2005-tk_bellman-stages.ipynb
preferred-citation:
  authors:
  - family-names: Cagetti
    given-names: Marco
  - family-names: De Nardi
    given-names: Mariacristina
  doi: 10.1086/508032
  end: 870
  issue: 5
  journal: Journal of Political Economy
  start: 835
  title: Entrepreneurship, Frictions, and Wealth
  type: article
  volume: 114
  year: 2006
redirect_from:
- /materials/Cagetti2005tk/
remark-name: Cagetti2005tk
repository-code: https://github.com/rzheng2112/Cagetti2005tk
tags:
- REMARK
- Notebook
- Reproduction
tier: 2
title: Cagetti2005tk
type: software
url: https://github.com/rzheng2112/Cagetti2005tk
version: 0.2.0
---

# Cagetti2005tk

This is a **REMARK-in-progress** (documentation target: Tier 2) that
partially reproduces the theoretical model of

> Cagetti, M. and De Nardi, M. (2006),
> *Entrepreneurship, Frictions, and Wealth*,
> **Journal of Political Economy**, 114(5), 835--870.
> [doi:10.1086/508032](https://doi.org/10.1086/508032)

It is **not** an officially accepted Econ-ARK catalog REMARK. Local
reproduction and documentation are under review; do not treat `tier: 2`
in the front matter as catalog certification.

## What a reviewer should read first

1. This file --- scope and expected outputs (below).
2. `README.md` --- one-command quick start and corrected baseline.
3. `ARCHITECTURE.md` --- file-by-file map of the repository.
4. `Cagetti2005tk_material/cagetti2005_theory_reproduction.ipynb`
   --- the reproduction notebook itself, cell-level commentary.
5. `NOTICES.md` --- vendored code provenance (SolvingMicroDSOPs).

## How to reproduce

```bash
git clone https://github.com/rzheng2112/Cagetti2005tk.git
cd Cagetti2005tk
./reproduce.sh
```

Bare `./reproduce.sh` runs the minimal reproduction
(`./reproduce_min.sh`) and writes an executed notebook and log under
`.reproduction/`. Build the report separately with
`./reproduce.sh --docs main`. The minimal reproduction alone takes
roughly 8--12 minutes on a recent laptop.

To run only the minimal reproduction:

```bash
./reproduce_min.sh
```

`uv` (<https://docs.astral.sh/uv/>) is required by `reproduce_min.sh`.
The runner synchronizes `uv.lock` with `--locked --group jupyter` and
invokes the project Python explicitly via an isolated Jupyter kernel.

## What IS reproduced

The notebook
`Cagetti2005tk_material/cagetti2005_theory_reproduction.ipynb` solves
the household-side partial-equilibrium Bellman system of the paper:

- **Occupational choice** between worker and entrepreneur for the young
  population, with endogenous bankruptcy / collateral enforcement
  (eq. 5), and old entrepreneur / retiree continuations.
- **Value functions** \(V_w\), \(V_e\), \(V=\max(V_w,V_e)\), \(W_e\),
  \(W_r\), \(W=\max(W_e,W_r)\), solved by damped value-function
  iteration (retiree, worker, old entrepreneur, then young entrepreneur) using the SolvingMicroDSOPs Endogenous-Grid-Method stage
  (`Code/Python/`). An irregular-grid / first-order-endpoint formula
  builds the EGM consumed function \(c_\delta\) (see notebook
  `cδ_from_v_grid`).
- **Calibrated structural parameters** (Table 5 of the paper):
  \(\beta = 0.865\), \(\sigma = 1.5\), \(\delta = 0.06\), \(\nu = 0.88\),
  \(f = 0.75\), \(\pi_y = 0.978\), \(\pi_o = 0.911\), \(\eta = 1.0\).
- **Income process** from paper Appendix A (5-state labour productivity)
  and entrepreneurial ability \(\theta \in \{0, 0.514\}\) (Table 5).
- **Nine supported regenerated artifacts** under `Figures/Cagetti2005tk/`
  and `Tables/Cagetti2005tk/`:
  - `values_policies_kstar.{pdf,png}` --- values and \(k^\star\) policy
  - `convergence.{pdf,png}` --- VFI residual history
  - `mu_marginal_assets.{pdf,png}` --- young-only asset distribution
  - `summary.csv` --- headline scalars
  - `counterfactuals.csv` --- PE re-solves (see convergence flags)
  - `wealth_concentration.csv` --- young-only PE wealth diagnostics
- Historical `wealth_lorenz.{pdf,png}` and `wealth_moments.csv` are
  preserved but have **no** verified generator in this workflow and are
  excluded from reproduction checks.

Corrected baseline (local reproduction after the EGM endpoint fix):
VFI converges in 115 iterations with final sum-norm
\(\approx 4.75\times10^{-4}\); young-only entrepreneur share
\(\approx 0.0833\); mean assets \(\approx 4.18\); young-only Gini
\(\approx 0.671\).

## What IS NOT reproduced

This REMARK-in-progress does **not** claim to match the paper's full
general-equilibrium stationary distribution:

- **Partial equilibrium.** The net interest rate (0.065) comes from Table 7 and the wage is normalized to one; Appendix B capital-market clearing is not iterated.
- **Young-only stationary kernel.** `iterate_mu_young_kernel` carries
  mass over \((\theta, y, a)\) with young staying young; it does not
  carry \(s \in \{YW, YE, OE, OR\}\) with demographic replacement or
  inheritance flows. Wealth concentration numbers in
  `wealth_concentration.csv` are **young-only PE diagnostics**. They are
  **not** paper Table 6 moments and **not** formal lower bounds on the
  paper's GE / full-demographic concentration.
- **Capital-grid ceiling.** Discrete \(k\) search uses `k_max = 18`.
  Enforcement and this numerical ceiling can both bind; \(k^\star\) is
  not determined by borrowing constraints alone.
- **Estate taxation.** The unused `estate_tax` parameter is reserved for a possible extension.
- **Payroll balance.** \(\tau = 0.10\) is illustrative; Appendix B
  social-security budget balance is not imposed.
- **Some PE counterfactuals.** Rows with `converged=False` in
  `counterfactuals.csv` hit the iteration limit with large residuals.
  They are numerical diagnostics, not valid comparative statics. The
  `n_k = 35 (uniform)` row uses a uniform grid on
  \([10^{-5}, k_{\max}]\), not a denser hybrid grid.

## Numerical checks

After the notebook runs, `reproduce_min.sh` invokes
`scripts/check_reproduction.py`, which asserts bands around the
**corrected** baseline (and fails a regression to the pre-EGM-fix
wealth statistics):

| metric                    | expected band (approx.) |
|---------------------------|-------------------------|
| `ent_share_mu_young_only` | \([0.05, 0.12]\)        |
| `mean_assets_mu`          | \([3.80, 4.60]\)        |
| `E_y_under_mu`            | \([0.90, 1.10]\)        |
| `final_sum_norm`          | \([0, 0.0005)\)  |
| `converged`               | `True`                  |
| wealth `gini`             | \([0.64, 0.72]\)        |
| wealth `top1` | [0.14, 0.15] |
| wealth `top5` | [0.36, 0.38] |

All counterfactual residuals must be finite and nonnegative. Converged rows must fall below 0.0005;
nonconvergence is allowed and is **not** required as a success condition.

## Code provenance

The three files under `Code/Python/` (`solution.py`, `resources.py`,
`stages/cons_noshocks.py`) are vendored from
<https://github.com/llorracc/SolvingMicroDSOPs> at a pinned revision.
See `NOTICES.md` and `scripts/revendor_smd.sh` for the refresh workflow.
