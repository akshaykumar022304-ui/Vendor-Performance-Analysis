\# Vendor Performance Analysis



\## Project Overview



This project analyzes vendor performance using purchasing, sales, inventory, and profitability data to identify key business trends and opportunities for improving procurement and inventory management.



The analysis combines Python-based data analysis with SQL and an interactive Power BI dashboard to evaluate vendor contribution, purchasing efficiency, inventory turnover, sales performance, and profitability.



\## Objectives



\- Identify vendors and brands with the highest sales performance.

\- Measure the contribution of top vendors to total procurement.

\- Analyze the relationship between bulk purchasing and unit purchase prices.

\- Identify vendors with low inventory turnover and potentially slow-moving stock.

\- Estimate capital tied up in unsold inventory.

\- Compare profit margins between top-performing and low-performing vendors.

\- Statistically test whether the difference in profit margins is significant.



\## Key Analysis



\### Sales Performance



The project identifies the top vendors and brands based on total sales dollars and visualizes their contribution to overall sales.



\### Procurement Concentration



The analysis measures how much of total procurement is dependent on the top vendors.



\### Bulk Purchasing



Purchase quantities are divided into Small, Medium, and Large order sizes to examine whether larger purchasing volumes are associated with lower unit purchase prices.



\### Inventory Turnover



Vendors with low stock turnover are identified to highlight potential excess inventory and slow-moving products.



\### Unsold Inventory



The project estimates the value of capital tied up in unsold inventory and identifies vendors contributing the most to this amount.



\### Profitability Analysis



Profit margins are compared between top-performing and low-performing vendors using confidence intervals and a two-sample statistical hypothesis test.



\## Tools \& Technologies



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- SciPy

\- SQL

\- Jupyter Notebook

\- Power BI

\- Git \& GitHub



\## Project Structure



```text

Vendor-Performance-Analysis/

│

├── dashboard/

│   └── Vendor\_Performance\_Dashboard.pbix

│

├── data/

│   └── vendor\_performance\_final.csv

│

├── notebooks/

│   ├── Vendor Performance Analysis.ipynb

│   └── Exploratory data analysis.ipynb

│

├── src/

│   ├── ingestion\_db.py

│   └── get\_vendor\_summary.py

│

├── .gitignore

└── README.md

