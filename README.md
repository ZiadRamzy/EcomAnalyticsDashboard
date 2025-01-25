# EcomAnalyticsDashboard

Interactive dashboard for e-commerce sales analysis.

## Prerequisites

Before running the scripts, ensure you have the required Python modules installed.

### Setting up the Environment

1. Create a virtual environment using Conda:
   ```bash
   conda create --name ecommerce_env python=3.9 -y
   conda activate ecommerce_env
   ```
2. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Sales Trends Analysis

This repository includes a script to analyze monthly sales trends based on e-commerce data.

- **Script**: `sales_trends_analysis.py`
- **Output**: `sales_trends.csv`

### Functionality

- Processes the `merged_dataset.csv` file to calculate total sales for each month.
- Generates a CSV file (`sales_trends.csv`) with two columns:
  - `YearMonth`: Year and month of sales data.
  - `Sales`: Total sales for the corresponding month.

### Usage

1. Ensure the `merged_dataset.csv` file is present in the root directory.

2. Run the script:
   ```bash
   python sales_trends_analysis.py
   ```
3. The output will include:
   - A CSV file (`sales_trends.csv`) with monthly sales data.
   - A PNG image (`sales_trends_plot.png`) of the graph.

### Example Output

```yaml
YearMonth,Sales
2020-01,48625.5
2020-02,38631.0
2020-03,102718.5
---
2023-12,338601.0
```

### Observations

The following graph illustrates the monthly sales trends from January 2020 to December 2023.

![Monthly Sales Trends](sales_trends_plot.png)

1. **Seasonal Peaks:** Sales consistently peak in November and December, aligning with holiday shopping seasons like Black Friday and Christmas.
2. **Growth Trend:** There is a steady increase in overall sales over the years, with 2023 having the highest sales figures.
3. **Off-Season Dips:** Sales are typically lower in January and February, likely due to post-holiday slowdowns.
