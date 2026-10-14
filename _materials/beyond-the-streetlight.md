---
abstract: 'Materials for Christopher Carroll''s discussion of Corrado, Kennickell
  and Cajner, "Beyond the Streetlight: Economic Measurement in the Division of Research
  and Statistics at the Federal Reserve", at the Federal Reserve''s R&S Centennial
  Conference (November 2023). The code analyzes the trend in the errors of the Tealbook/Greenbook
  (GB) and Survey of Professional Forecasters (SPF) forecasts of the unemployment
  rate and of real growth in personal consumption expenditures from 1982 to 2017.'
authors:
- affiliation: Johns Hopkins University
  family-names: Edwards
  given-names: Decory
- affiliation: Johns Hopkins University
  family-names: Carroll
  given-names: Christopher D.
  orcid: https://orcid.org/0000-0003-3732-9312
authors-original-paper:
- Carol Corrado
- Arthur Kennickell
- Tomaz Cajner
cff-version: 1.2.0
date-released: '2026-10-13'
doi: 10.5281/zenodo.23352415
github_repo_url: https://github.com/econ-ark/beyond-the-streetlight
identifiers-paper:
- type: doi
  value: 10.17016/FEDS.2025.019
- type: url
  value: https://doi.org/10.17016/FEDS.2025.019
keywords:
- Greenbook
- Survey of Professional Forecasters
- Forecast errors
- Economic measurement
license: Apache-2.0
message: If you use this software, please cite it as below.
notebooks:
- RS100_Discussion_Slides.ipynb
references:
- authors:
  - family-names: Corrado
    given-names: Carol
  - family-names: Kennickell
    given-names: Arthur
  - family-names: Cajner
    given-names: Tomaz
  collection-title: Finance and Economics Discussion Series
  doi: 10.17016/FEDS.2025.019
  institution:
    name: Board of Governors of the Federal Reserve System
  month: 3
  notes: Prepared for the R&S Centennial Conference, November 8, 2023, where Christopher
    Carroll was a discussant.
  number: 2025-019
  title: 'Beyond the Streetlight: Economic Measurement in the Division of Research
    and Statistics at the Federal Reserve'
  type: report
  url: https://doi.org/10.17016/FEDS.2025.019
  year: 2025
remark-name: beyond-the-streetlight
repository-code: https://github.com/econ-ark/beyond-the-streetlight
summary: Christopher Carroll's discussion of Corrado, Kennickell and Cajner at the
  Federal Reserve's R&S Centennial Conference (November 2023), with code showing that
  the errors in Greenbook and SPF forecasts of real consumption growth have trended
  down since 1983, while unemployment forecast errors show no trend.
tags:
- REMARK
- Reproduction
- Notebook
tier: 3
title: Beyond the Streetlight
title-original-paper: 'Beyond the Streetlight: Economic Measurement in the Division
  of Research and Statistics at the Federal Reserve'
type: software
url: https://econ-ark.github.io/beyond-the-streetlight/
version: 1.1.2
---

# Beyond the Streetlight

This REMARK contains Christopher Carroll's discussion, at the Federal Reserve
Board's R&S Centennial Conference on November 6-8, 2023, of the paper by Carol
Corrado and Arthur Kennickell, together with the code and data behind the
discussion's figures. The paper's final version, with Tomaz Cajner as a third
author, is Corrado, Kennickell and Cajner (2025), "Beyond the Streetlight:
Economic Measurement in the Division of Research and Statistics at the Federal
Reserve", Finance and Economics Discussion Series 2025-019,
<https://doi.org/10.17016/FEDS.2025.019>. The conference draft was titled "100
years of Economic Measurement in the Division of Research & Statistics: Beyond
the Streetlight".

## The argument

The discussion treats measurement as information production. Beyond primary
data (such as the Survey of Consumer Finances) and secondary data (such as
industrial production), the Fed produces "tertiary" information: the staff
forecasts in the Greenbook and Tealbook, staff memos, and similar work. The
Greenspan Fed's call of a "new economy" in the mid-1990s is the leading example
of that information being used well. The discussion asks whether the Fed was
just lucky then, or whether forecasting has improved over time, at the Fed and
elsewhere, as better measurement would imply.

## What the code does

The analysis compares two sets of forecasts with what actually happened:

- **Greenbook/Tealbook (GB)**: the Federal Reserve Board staff forecasts,
  from the Federal Reserve Bank of Philadelphia's Greenbook data set;
- **Survey of Professional Forecasters (SPF)**: the mean private-sector
  forecast, also from the Philadelphia Fed;
- **Realized values**: the unemployment rate (FRED series `UNRATE`) and real
  personal consumption expenditures (`DPCERA3Q086SBEA`).

For each quarter it builds a year-ahead forecast of the change in unemployment
and of real consumption growth, computes the absolute forecast error, and
regresses the error on a time trend with heteroskedasticity-robust (HC3)
standard errors, over the full sample (144 quarters, labeled 1983Q1-2018Q4)
and from 1995 on.

## Findings

Errors in forecasts of real consumption growth have fallen significantly, for
both forecasters. Over the full sample the trend is -0.039 percentage points a
year for the Greenbook and -0.031 for the SPF (both p < 0.001), and it remains
negative after 1995. Errors in forecasts of the change in unemployment show no
significant trend. The two figures in the slides show the consumption results.

## Reproducing the results

`./reproduce.sh` regenerates every table and figure from the raw data, checks
them against the committed versions, and renders the slides; it takes about 30
seconds once the environment (pinned in `uv.lock`) is installed. It needs no
network access or API key: the realized values come from a committed snapshot of
the FRED data used for the published results. See `README.md` for Docker, conda
and Binder instructions and for a description of every output.
