# Central Bank Journey: Complete Structure and Content

## Main Page Title
# From Theory to Policy: A HANK Journey
**Master Heterogeneous Agent New Keynesian models for modern monetary policy**

---

## Navigation Structure
1. [Overview](#overview)
2. [Bewley Model Basics](#bewley-model-basics)
3. [Interactive Dashboards](#interactive-dashboards)
4. [Notebooks](#notebooks)
5. [Tools](#tools)
6. [Replications](#replications)

---

## Overview

### Main Content
Central banks worldwide are adopting heterogeneous agent models to better understand monetary policy transmission. This journey guides you through the theory, computational methods, and practical applications of HANK (Heterogeneous Agent New Keynesian) models.

Whether you're a researcher exploring theoretical mechanisms or a policymaker analyzing real-world interventions, you'll find tools and resources tailored to your needs. Start with interactive dashboards for intuition, dive into notebooks for hands-on learning, or use our computational toolkit for your own research.

### What is a Bewley Model?
A Bewley model is a macroeconomic framework where households face uninsurable idiosyncratic income risk and borrowing constraints. Unlike representative agent models, Bewley models capture realistic wealth inequality and marginal propensities to consume, leading to richer policy implications.

### Sections in the Roadmap
- **Model Basics** - Understand the core mechanisms
- **Interactive Dashboards** - Explore policy experiments  
- **Notebooks** - Hands-on implementation
- **Main Tools** - Computational resources
- **Replications** - Learn from research examples

---

## Bewley Model Basics

### Why heterogeneity matters for macro 

Central banks need models that capture how monetary policy affects different households differently. In representative agent models, interest rate changes work through a single channel. In reality, policy impacts vary dramatically across the wealth distribution.

### Monetary Policy Channels Comparison

#### Representative-Agent Model
- **Central Bank** → Interest Rate ↓ → **Representative Agent**
- Single channel: Intertemporal Substitution
- One agent saves more

#### Heterogeneous-Agent Model  
- **Central Bank** → Interest Rate ↓ → **Three Household Types**:
  
  **Low-Wealth Households**
  - High MPC; respond to income
  - Labour Income (hover to see)
  - Cash-Flow (hover to see)
  
  **Middle-Wealth Households**
  - Precautionary motive stifles response
  - Buffer-Stock Savings (hover to see)
  
  **High-Wealth Households**
  - Low MPC; respond to prices
  - Interest Income (hover to see)
  - Asset Prices (hover to see)

### Key Implications
- **Richer Policy Channels** - Beyond simple intertemporal substitution, policy works through income, wealth, and portfolio effects
- **Distributional Effects Matter** - The same policy has different impacts across the wealth distribution, affecting overall effectiveness
- **Calibrated with Real-World Data** - Models match empirical wealth distributions and MPCs, providing quantitatively realistic predictions

### Historical Perspective (Collapsible)
- **1950s: Foundations: PIH & LCH** - Friedman's Permanent Income Hypothesis and Modigliani's Life-Cycle Hypothesis laid groundwork
- **1977: The Bewley Model** - Truman Bewley introduced incomplete markets with borrowing constraints
- **1989-92: First Quantitative Models** - Imrohoroglu, Huggett, and Aiyagari made models computationally tractable
- **1994: General Equilibrium** - Aiyagari embedded incomplete markets in general equilibrium
- **1998: Krusell-Smith** - Aggregate uncertainty enters incomplete market models
- **2010s-Now: Modern HANK** - New Keynesian features added; central banks adopt for policy analysis

### Computing Bewley Models

Solving these models requires sophisticated computational methods, but modern tools make them accessible to researchers and policymakers alike.

#### Three-Step Computational Process
1. **Micro Problem** - Solve HH problem with HARK (EGM, VFI)
2. **Aggregation** - Summarize responses with Jacobians (∂A/∂Z)  
3. **GE Prices** - Find market-clearing prices (w, r)

*Econ-ARK provides modular, open-source implementations of each component in this workflow, from state-of-the-art micro solvers like EGM to cutting-edge macro methods like SSJ. The toolkit's speed and flexibility enable researchers to iterate quickly, explore rich model variations, and connect their work to the broader literature through shared code and replications.*

#### Interactive Solver Methods

**Tab 1: Dynamic Micro Problem**
- **Endogenous Grid Method** - An efficient and accurate method for consumption problems with liquidity constraints
- **Value Function Iteration** - A robust and general-purpose method for solving dynamic programming problems
- **Coleman-Reffett Operator** - An approach that iterates on the policy rule itself, often using interpolation

**Tab 2: Micro Simulation**
- **Simulate Distribution** - Generate a time series of aggregate variables (C, S, L) from the microeconomic decisions

**Tab 3: Estimation**
- **Micro-data Calibration** - Use moments from household surveys (e.g., HFCS, SCF) to calibrate model parameters
- **Likelihood-Based Methods** - Use SSJ for fast, formal estimation (SMM, MLE)
- **New Data Frontiers** - Leverage high-frequency administrative data

**Tab 4: General Equilibrium**
- **Sequence-Space Jacobian** - A fast, linear solver for calculating impulse responses
- **Krusell–Smith** - A non-linear method that approximates the aggregate law of motion
- **Direct Iteration** - A fully non-linear benchmark method

---

## Interactive Dashboards

Explore how heterogeneous agent models change our understanding of policy transmission through interactive visualizations. No coding required - just adjust parameters and see results in real-time.

### Available Dashboards

#### 1. Pandemic Policy Response
- **Pandemic Response Model** - Based on Carroll et al. (2020)
- Adjustable parameters:
  - Spending Reduction During Lockdown
  - Lockdown Duration (Quarters)
  - Stimulus Amount ($1000s)
  - Unemployment Benefits Bonus
- **Key Results**:
  - Peak Unemployment
  - Consumption Drop
  - Policy Effectiveness

#### 2. Impulse Response
- Adjustable parameters:
  - Fiscal Shock Size
  - Household Impatience
- **Key Result**: Peak Response

#### 3. Wealth Distribution
- Adjustable parameters:
  - Wealth Inequality (Gini)
- **Key Result**: Top 10% Share

---

## Notebooks

Dive into the code. These notebooks provide the full implementation and allow for deep customization. Launch them in the cloud with zero local installation required.

### Available Notebooks

#### HANK Model Basics
Introduction to heterogeneous agent modeling with income and wealth inequality.
*Difficulty: Beginner*

#### Monetary Policy Transmission
Explore how interest rate changes affect different household types.
*Difficulty: Intermediate*

#### Fiscal Multipliers
Compare fiscal policy effectiveness across different model specifications.
*Difficulty: Advanced*

#### Crisis Response Models
Analyze unconventional monetary policy tools in HANK frameworks.
*Difficulty: Advanced*

---

## Tools

This journey is powered by several powerful open-source tools. Learn more about the core components of the Econ-ARK ecosystem.

### Core Tools

#### HARK-FED Toolkit
Central bank-specific extensions to the HARK modeling framework.
*Type: Python Library*

#### Policy Simulation Lab
Interactive environment for testing monetary policy scenarios.
*Type: Web Application*

#### Calibration Assistant
Automated parameter estimation for country-specific models.
*Type: R Package*

#### Forecasting Engine
Real-time economic forecasting with heterogeneous agent models.
*Type: API Service*

---

## Replications

Explore how HARK is used to replicate and extend influential papers in the field. These examples demonstrate the practical application of the toolkit for research.

### Featured Replications

#### Kaplan, Moll & Violante (2018)
Monetary policy according to HANK - complete replication with extensions for central bank analysis.
*Source: AER • Complete Code & Data*

#### Bayer, Born & Luetticke (2023)
The liquidity channel of fiscal policy - analyzing government spending multipliers.
*Source: Econometrica • Jupyter Notebooks*

#### Auclert, Bardóczy, Rognlie (2021)
Using the sequence-space Jacobian to solve and estimate heterogeneous agent models.
*Source: NBER WP • Interactive Tools* 