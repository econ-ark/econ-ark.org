---
name: CGMPortfolio
summary: 'This is a reproduction of the results in the paper "Consumption and Portfolio Choice over the Life Cycle" by Mateo Velasquez-Giraldo and Matthew V. Zahn.'
type: replication
is_notebook: true
published:
authors:
  - Mateo Velasquez-Giraldo
  - Matthew V. Zahn
tags:
  - Replication
location_url: https://github.com/econ-ark/CGMPortfolio/blob/master/Code/Python/CGMPortfolio.ipynb
github_user: econ-ark
github_repository: CGMPortfolio
github_branch: master
github_path: Code/Python/CGMPortfolio.ipynb
---

This is a reproduction of the results in Cocco, Gomes, & Maenhout (2005) "Consumption and Portfolio Choice Over the Life Cycle".

Location of main files:
1. A notebook attempting to replicate the paper's main results using HARK can be found at "Code/Python/CGMPortfolio.ipynb".
2. A document going into more detail on our attempt to replicate can be found at "CGMPortfolio.pdf".
3. The code that generates all the figures and results in the previous document can be found at "Code/Python". Files can be run independently, or all at once through the script "./do_ALL.py". Additional files "./do_MIN.py" and "./do_MID.py" are made available to execute subsets of the results.
- ""./do_MIN.py": solves the baseline model plotting its policy functions, and presents mean simulated life-cycle behavior of variables of interest. Runtime: ~400 seconds.
- "./do_MID.py": additionally compares the policy functions obtained with HARK with those that we obtain from executing the authors' FORTRAN 90 code. Runtime: ~600 seconds.
- "./do_ALL.py": additionally computes all the results from the apendices, in which we alter the baseline model in HARK to cases in which analytical solutions are available. Runtime: ~1300 seconds.

Note: runtimes are estimated using an Intel Core i7-6700HQ CPU @ 2.60GHz.
