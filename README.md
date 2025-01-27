# EcomAnalyticsDashboard

Interactive dashboard for e-commerce sales analysis.

**[👉 View the Live Dashboard Here](https://ecomanalyticsdashboardgit-h9htr7ynzyqfdbubyh3zlh.streamlit.app)**

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

![Monthly Sales Trends](Graphs/sales_trends_plot.png)

1. **Seasonal Peaks:** Sales consistently peak in November and December, aligning with holiday shopping seasons like Black Friday and Christmas.
2. **Growth Trend:** There is a steady increase in overall sales over the years, with 2023 having the highest sales figures.
3. **Off-Season Dips:** Sales are typically lower in January and February, likely due to post-holiday slowdowns.

## Profitability Analysis

The `profitability_analysis.py` script calculates the profitability of categories, regions, and products based on the provided e-commerce dataset.

### Output Files

1. `profitable_categories.csv`: Lists the total profit by product category (e.g., Office Supplies, Technology, Furniture).
2. `profitable_regions.csv`: Lists the total profit by country, highlighting the most and least profitable regions.
3. `profitable_products.csv`: Lists individual product names and their respective profits.

### Usage

To run the analysis:

```bash
python profitability_analysis.py
```

#### Visualizations:

1. **Profitable Categories:**
   - Saved as `profitable_categories_chart.png`.
   - Highlights the most profitable product categories.

![Profitable Categories](Graphs/profitable_categories_chart.png)

- **Office Supplies** has the highest profit ($531,066.31), which may indicate consistent sales, lower costs, or better profit margins in this category.

- **Technology** comes second ($239,528.96), likely due to high-value items (e.g., laptops, smartphones). However, its lower rank compared to Office Supplies could imply narrower margins or higher costs.

- **Furniture** has a significantly lower profit ($41,720.21). This might be due to higher shipping costs, bulkier items, or lower demand.

2. **Profitable Regions:**
   - Saved as `profitable_regions_chart.png`.
   - Highlights the top 10 most profitable regions.

![Profitable Regions](Graphs/profitable_regions_chart.png)

- **United States** ($150,725.36), **China** ($123,995.01), and **India** ($84,221.24) are the top regions.

- **Negative profits** in countries like **Vietnam** ($-842.06) and **Pakistan** (-$1,139.99) highlight regions that are underperforming, where profitability could be improved.

## Shipping Cost Analysis

This analysis focuses on evaluating the average shipping cost and total profit for each shipping mode. The `shipping_costs_analysis.py` script groups data by `Ship.Mode` and calculates:

- `avg_shipping_cost`: The mean shipping cost for each mode.
- `total_profit`: The total profit generated by each shipping mode.

![Shipping Profitability](Graphs/shipping_profitability_analysis.png)

#### Key Trends:

1. **Standard Class (Lowest Cost, Highest Profit):**:
   - Since customers pay the lowest shipping cost, it likely makes this option the most popular. High usage translates to the highest total profit, not because of shipping costs but because of the higher volume of orders using this mode.
2. **Second Class (Moderate Cost and Profit):**:
   - Second Class has a higher shipping cost but generates moderate profits. This might suggest that a segment of customers prioritizes faster delivery but isn’t as price-sensitive as Standard Class users.
3. **First Class (High Cost, Lower Profit):**
   - First Class shipping has significantly higher costs to customers, which likely limits its usage
4. **Same Day (High Cost, Lowest Profit):**
   - Same Day shipping has the highest cost to customers but generates the lowest total profit. This suggests it is rarely chosen.

## Customer Analysis

This analysis focuses on understanding customer behavior, identifying high-value customers (top 10% by sales), and repeat customers (with more than one order).

#### Key Files:

1. `customer_behavior.csv`: Complete dataset of customers with total sales, profits, and order counts.
2. `repeat_customers.csv`: Repeat customers ranked by order count.
3. `high_value_customers.csv`: High-value customers ranked by total sales.

#### Visualizations:

1. **High-Value Customers Analysis:**

![High  Valued Customers ](Graphs/high_value_customers_analysis.png)

- Customers like `Sean Miller` contribute significantly to sales but show negative profits. Such Customers should be analyzed for inefficiencies like discounts, low-margin products, or high operational costs.
- Customers such as `Adrian Barton` and `Cynthia Arntzen` exhibit a good balance between high sales and profitability.

2. **Repeat Customers:**

![Repeat Customers ](Graphs/repeat_customers_analysis.png)

- Many customers with high order counts (e.g., 30–40) have moderate profits, represented by the denser cluster in the middle.
- Larger bubbles (representing high sales) are spread unevenly across the profit spectrum, meaning that not all high sales translate to high profitability.

## Country Specific Metrics:

### Top 10 Countries by Sales and Profit:

![Top 10 Countries by Sales and Profit](Graphs/country_metrics_visualization.png)

1. The **United States** and **China** are the top-performing countries in terms of total sales. This indicates that they are primary markets driving sales.
2. The profits are proportionally small compared to the total sales across countries, reasons might be for example high operational costs or small margins.
3. Countries like **India**, **Mexico**, and **France** hold a significant share in sales compared to others but still lag behind the top two. They could represent growing markets.
4. While the **U.S**. and **China** are leading, boosting profitability in other regions (e.g., Europe or South America) may provide balanced revenue distribution.

### Top 10 Cities by Product Demand with Products:

![Top 10 Cities by Product Demand with Products](Graphs/product_demand_by_city_and_product.png)

1. **City-Level Demand:**
   - **Los Angeles** has the highest total sales by a significant margin, suggesting it is a key city driving product demand. It outpaces other cities by a wide margin, potentially due to its economic scale or purchasing power.
2. **Product-Specific Demand:**
   - **High-demand products include:**
     - **Cisco TelePresence System EX90** in Los Angeles.
     - Products like **Canon Advanced Copier** and **3D Printers** dominate other cities' demands, reflecting diverse needs across locations.
   - Tech and office-related products appear to dominate sales in major cities, which may reflect the industries or consumer base there.
3. **Opportunities for Tailored Marketing:**
   - Different cities favor specific product categories, indicating potential for targeted marketing and distribution strategies.
4. **Growth Potential in Smaller Cities:**
   - Cities like **Beijing**, **Shanghai**, or **Gennvilliers** have lower total sales compared to top performers. These could represent markets with room for growth.

## Dashboard

This repository contains an interactive **Streamlit** dashboard that visualizes and analyzes e-commerce sales data. The dashboard helps derive actionable insights for optimizing sales strategies, identifying high-value customers, and analyzing shipping modes and regional trends.

---

### Features

- **Filters**: Interactive filters for date range and countries.
- **Visualizations**:
  - **Sales & Profit by Country**: Top-performing countries by sales and profits.
  - **Product Demand**: Analyze the most popular products by cities.
  - **High-Value Customers**: Identify repeat and high-value customers.
  - **Shipping Analysis**: Compare average shipping costs and profitability by mode.
- **Download Filtered Data**: Export the filtered dataset as a CSV file.

---

### Running Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ZiadRamzy/EcomAnalyticsDashboard.git

   cd EcomAnalyticsDashboard/
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard:**

   ```bash
   streamlit run dashboard.py
   ```

4. **Open the app in your browser (default: `http://localhost:8501`).**
