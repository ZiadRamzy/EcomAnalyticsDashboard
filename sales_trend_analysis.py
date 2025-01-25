import pandas as pd
import matplotlib.pyplot as plt


merged_df = pd.read_csv('merged_dataset.csv')

merged_df['Order.Date'] = pd.to_datetime(merged_df['Order.Date'])

# group and sum the sales by year and month
merged_df['YearMonth'] = merged_df['Order.Date'].dt.to_period('M')
sales_trends = merged_df.groupby('YearMonth')['Sales'].sum().reset_index()

#sales_trends.to_csv('sales_trends.csv', index=False)
print(f"Sales Trends: {sales_trends.head()}")

sales_trends['YearMonth'] = sales_trends['YearMonth'].dt.to_timestamp()

# plotting the sales trends
plt.figure(figsize=(12, 6))
plt.plot(sales_trends['YearMonth'], sales_trends['Sales'], marker='o', label='Total Sales')
plt.title("Monthly Sales Trends (2020-2023)", fontsize=16)
plt.xlabel("Year-Month", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig('sales_trends_plot.png')
plt.show()

print("Sales trends graph has been saved as 'sales_trends_plot.png'")

