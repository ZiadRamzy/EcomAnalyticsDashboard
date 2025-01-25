import pandas as pd

orders_df = pd.read_csv('orders.csv')
customers_df = pd.read_csv('customers.csv')
products_df = pd.read_csv('products.csv')
sales_df = pd.read_csv('sales.csv')

orders_df['Order.Date'] = pd.to_datetime(orders_df['Order.Date'], format='%Y-%m-%d')

merged_df = orders_df.merge(customers_df, on="Customer.ID", how="inner")

merged_df = merged_df.merge(products_df, on="Product.ID", how="inner")

merged_df = merged_df.merge(sales_df, on="Order.ID", how="inner")

merged_df.to_csv('merged_dataset.csv', index=False)
