# equity_return_factor_analysis
This is a mini project that I've started over winter break on factor analysis on equity return drivers.

## Project Overview
For this project I will implement CAPM, Fama-French, and PCA over AAPL, JPM, and XOM, analyzing their daily returns to understand the different drivers.

**Goal:** To identify factors that explain why stocks outperform or underperform over time. This can help investors make informed decisions, optimize portfolios, or even manage risk.

### Why Factor Models Matter
The CAPM and Fama-French three-factor model are essential in finance. These models help break down stock returns into systematic and nonsystematic risks. Factor models show specific drivers that impact returns (e.g. beta, size, book value). Which can help:

- Portfolio construction
- Risk management
- and evaluation

## Data
- **Source:** yfinance
- **Frequency:** Daily
- **Time Period:** January 1, 2015 - January 1, 2025

## Methodology
- **CAPM:**  
  Estimates each asset’s sensitivity to market returns (beta) and abnormal returns (alpha).

- **Fama-French 3-Factor Model:**  
  Extends CAPM by including size and value factors to better explain return variation.

- **Principal Component Analysis (PCA):**  
  Extracts latent factors that explain the majority of variance in asset returns.

- **Risk Metrics:**  
  - Volatility  
  - Value-at-Risk (VaR)  
  - Maximum drawdown  

  ## **NOTE**:
  **The CSVs are not kept due to the size. If you would like to replicate my findings, please use scripts (scr) 1-3 and follow my notebook!!** 