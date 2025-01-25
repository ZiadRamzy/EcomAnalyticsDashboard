import pandas as pd

merged_df = pd.read_csv('merged_dataset.csv')

merged_df['Order.Date'] = pd.to_datetime(merged_df['Order.Date'])

# group and sum the sales by year and month
merged_df['YearMonth'] = merged_df['Order.Date'].dt.to_period('M')
sales_trends = merged_df.groupby('YearMonth')['Sales'].sum().reset_index()

sales_trends.to_csv('sales_trends.csv', index=False)
print(f"Sales Trends: {sales_trends.head()}")
