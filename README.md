# Vendor Performance Analysis

## Project Overview

This project analyzes vendor performance using purchasing, sales, inventory, and profitability data to identify key business trends and opportunities for improving procurement and inventory management.

The analysis combines Python-based data analysis with SQL and an interactive Power BI dashboard to evaluate vendor contribution, purchasing efficiency, inventory turnover, sales performance, and profitability.

## Objectives

- Identify vendors and brands with the highest sales performance.
- Measure the contribution of top vendors to total procurement.
- Analyze the relationship between bulk purchasing and unit purchase prices.
- Identify vendors with low inventory turnover and potentially slow-moving stock.
- Estimate capital tied up in unsold inventory.
- Compare profit margins between top-performing and low-performing vendors.
- Statistically test whether the difference in profit margins is significant.


## Project Structure

```text
Vendor-Performance-Analysis/
│
├── dashboard/
│   └── Vendor_Performance_Dashboard.pbix
│
├── data/
│   └── vendor_performance_final.csv
│
├── notebooks/
│   ├── Vendor Performance Analysis.ipynb
│   └── Exploratory data analysis.ipynb
│
├── src/
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── .gitignore
└── README.md