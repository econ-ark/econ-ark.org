---
abstract: This repository provides an analysis of the trend in forecast errors made
  by the Tealbook/Greenbook(GB) and the Survey of Professional Forecasters(SPF) for
  measures of the unemployment rate and real growth in personal consumption expenditures
  from 1982 to 2017.
authors:
- family-names: Edwards
  given-names: Decory
- family-names: Carroll
  given-names: Christopher
  orcid: https://orcid.org/0000-0003-3732-9312
cff-version: 1.2.0
date-released: 2023-11-06
keywords:
- Econ-ARK
- Greenbook
- Forecast errors
message: If you use this software, please cite it as below.
notebooks:
- RS100_Discussion_Slides.ipynb
references:
- authors:
  - family-names: Corrado
    given-names: Carol
  - family-names: Kennickell
    given-names: Arthur
  date: 2023-10-24
  publisher: R&S Centennial Conference
  title: '100 years of Economic Measurement in the Division of Research & Statistics:
    Beyond the streetlight'
  type: article
remark-name: beyond-the-streetlight
repository-code: https://github.com/econ-ark/beyond-the-streetlight
tags:
- REMARK
- Notebook
title: Beyond the streetlight
title-original-paper: '100 years of Economic Measurement in the Division of Research
  & Statistics: Beyond the streetlight'
version: 1.0.4
---

# Abstract

This repository provides an analysis of the trend in forecast errors made by the Tealbook/Greenbook(GB) and the Survey of Professional Forecasters(SPF) for measures of the unemployment rate and real growth in personal consumption expenditures from 1982 to 2017. The data on forecasts for unemployment and consumption made by the Federal Reserve (Tealbook/Greenbook) and the mean across private forecasters are provided by the Philadelphia Fed. Data on realized values of the forecasted variables are provided by the St. Louis Fed.

---

## Website-specific metadata for enhanced display and discoverability

learning_objectives:

- "Understand the limitations of traditional data sources in economic research"
- "Explore how Google Books data can supplement conventional economic indicators"
- "Apply web scraping and text analysis techniques to economic research"
- "Assess the validity of alternative data sources through replication studies"
- "Compare forecast accuracy between traditional and unconventional data approaches"

prerequisites:

- "Intermediate knowledge of macroeconomics and economic indicators"
- "Basic Python programming skills"
- "Familiarity with data manipulation (pandas) and visualization (matplotlib)"
- "Understanding of statistical concepts and forecast evaluation"
- "Knowledge of web APIs and data scraping concepts"

jupyter_notebooks:

- path: "RS100_Discussion_Slides.ipynb"
    description: "Main presentation slides and interactive analysis"
    type: "presentation"
    estimated_runtime: "10-15 minutes"

related_materials:

- "data-analysis-techniques"
- "economic-forecasting"
- "web-scraping-methods"
- "alternative-data-sources"

methodology_tags:

- "alternative data"
- "web scraping"
- "forecast evaluation"
- "text analysis"
- "economic indicators"
- "google books ngram"
- "replication study"

difficulty_level: "intermediate"

estimated_completion_time: "2-3 hours for full analysis"

research_context: |
  This project demonstrates the exploration of unconventional data sources for economic research,
  specifically using Google Books Ngram data to track economic concepts over time. It serves as
  both a methodological contribution and a replication study, showing how alternative data can
  complement traditional economic indicators.

educational_value: |
  Students and researchers will learn how to think creatively about data sources, implement
  web scraping techniques for research, and critically evaluate the validity of alternative
  data through rigorous comparison with established sources.

policy_relevance: |
  The methods demonstrated here are relevant for real-time economic monitoring, early warning
  systems, and situations where traditional data may be delayed or unavailable. This is
  particularly valuable for emerging economies or during crisis periods.

computational_requirements:
  python_version: "3.8+"
  key_packages:
    - "pandas"
    - "matplotlib"
    - "requests"
    - "beautifulsoup4"
    - "numpy"
    - "jupyter"
  memory_requirements: "Moderate (< 4GB RAM)"
  runtime_estimates:
    full_reproduction: "30-45 minutes"
    quick_demonstration: "5-10 minutes"

data_sources:

- name: "Google Books Ngram Viewer"
    description: "Historical frequency of words/phrases in books"
    url: "<https://books.google.com/ngrams>"
    access_method: "Web scraping"

- name: "Federal Reserve Economic Data (FRED)"
    description: "Official economic time series data"
    url: "<https://fred.stlouisfed.org/>"
    access_method: "API"

- name: "Survey of Professional Forecasters"
    description: "Professional economic forecasts"
    url: "<https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/survey-of-professional-forecasters>"
    access_method: "Direct download"

reproducibility_notes: |
  This project demonstrates best practices for reproducible research with web-scraped data:

- All data sources are documented with URLs and access dates
- Web scraping code includes error handling and rate limiting
- Results are compared against multiple validation sources
- Environment specifications ensure consistent package versions

extensions_and_variations:

- "Apply similar techniques to other economic concepts or time periods"
- "Explore other alternative data sources (social media, satellite data, etc.)"
- "Develop real-time monitoring systems using these techniques"
- "Compare forecast accuracy across different alternative data sources"
- "Investigate cultural and linguistic biases in text-based economic indicators"

teaching_applications:

- "Data science courses: web scraping and API integration"
- "Economics courses: alternative data and nowcasting"
- "Research methods: validation and replication techniques"
- "Policy analysis: real-time economic monitoring"

### citation_context

- This work builds on and references the broader literature on alternative data in economics, including nowcasting techniques, textual analysis of economic content, and the evaluation of unconventional economic indicators. It serves as both an educational resource and a methodological contribution to the field

---

## Beyond the Streetlight: Alternative Data Sources in Economic Research

## Project Overview

This research project explores the famous methodological challenge in economics: like the drunk man looking for his keys only under the streetlight "because that's where the light is," economists often rely on traditional data sources simply because they are readily available, not because they are necessarily the most informative.

## Research Question

Can alternative data sources, specifically Google Books Ngram data tracking the usage of economic terms over time, provide valuable insights that complement or enhance traditional economic indicators and forecasting methods?

## Methodology

The project employs a rigorous empirical approach:

1. **Data Collection**: Automated scraping of Google Books Ngram data for economic terms
2. **Data Integration**: Combining alternative data with traditional economic indicators from FRED
3. **Comparative Analysis**: Evaluating forecast accuracy using both conventional and unconventional data
4. **Validation**: Cross-checking results against professional forecaster surveys
5. **Reproducibility**: Full documentation and automation of the research pipeline

## Key Findings

The analysis reveals both the potential and limitations of alternative data sources:

- **Complementary Value**: Alternative indicators can provide additional signals not captured in traditional data
- **Timing Advantages**: Some alternative sources may offer earlier signals than official statistics
- **Methodological Challenges**: Validation and interpretation require careful consideration of data generation processes
- **Context Dependency**: Effectiveness varies by economic indicator and time period

## Educational Value

This project serves multiple educational purposes:

- **Methodological Training**: Demonstrates web scraping, API integration, and data validation techniques
- **Critical Thinking**: Encourages questioning of conventional data sources and research approaches
- **Practical Skills**: Provides hands-on experience with real-world data challenges
- **Research Ethics**: Illustrates responsible use of scraped data and proper attribution

## Broader Implications

The "beyond the streetlight" approach has applications across economics and social science:

- **Crisis Monitoring**: Alternative data may be crucial when traditional statistics are delayed
- **Emerging Markets**: Unconventional sources may fill gaps in official data availability
- **Policy Making**: Real-time indicators could inform more timely policy responses
- **Academic Research**: Methodological framework applicable to other research questions

## Interactive Components

The project includes interactive Jupyter notebooks that allow users to:

- Modify search terms and explore different economic concepts
- Adjust time periods and geographical regions
- Experiment with different validation approaches
- Extend the analysis to new data sources

## Reproducibility and Transparency

All code, data, and analysis steps are fully documented and automated:

- Environment specifications ensure consistent results across platforms
- Error handling and logging provide transparency in data collection
- Version control tracks all changes and updates
- Documentation includes both technical details and conceptual explanations

This project exemplifies the REMARK standard's emphasis on computational reproducibility while advancing methodological discussions in economic research. It demonstrates how economists can responsibly explore alternative data sources while maintaining rigorous standards for validation and interpretation.

## Getting Started

To explore this research:

1. **Quick Start**: Run the Jupyter notebook for an interactive overview
2. **Full Reproduction**: Execute the complete analysis pipeline
3. **Experimentation**: Modify parameters to explore different research questions
4. **Extension**: Use the framework as a starting point for your own alternative data research

The project is designed to be both a standalone research contribution and an educational resource for the computational economics community.
