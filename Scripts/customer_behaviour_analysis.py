import pandas as pd
import matplotlib.pyplot as plt


merged_df = pd.read_csv('merged_dataset.csv')

# total sales and profit by customer
customer_behavior = merged_df.groupby('Customer.Name').agg(
    total_sales=('Sales', 'sum'),
    total_profit=('Profit', 'sum'),
    order_count=('Order.ID', 'count')
).reset_index().sort_values(by='total_sales', ascending=False)


repeat_customers = customer_behavior[customer_behavior['order_count'] > 1].sort_values(by='order_count', ascending=False)
high_value_customers = customer_behavior[
    customer_behavior['total_sales'] > customer_behavior['total_sales'].quantile(0.9)
].sort_values(by='total_sales', ascending=False)

customer_behavior.to_csv('customer_behavior.csv', index=False)
repeat_customers.to_csv('repeat_customers.csv', index=False)
high_value_customers.to_csv('high_value_customers.csv', index=False)

print(f"Top Customers by Sales: \n{customer_behavior.head()}")
print(f"Top Reapeating Customesr by Order Count: \n{repeat_customers.head()}")
print(f"High Valued Customer by Sales: \n{high_value_customers.head()}")


# bar chart for the high value customers
plt.figure(figsize=(12, 6))
plt.bar(high_value_customers['Customer.Name'][:10], high_value_customers['total_sales'][:10], label='Total Sales', color='skyblue')
plt.plot(high_value_customers['Customer.Name'][:10], high_value_customers['total_profit'][:10], label='Total Profit', color='red', marker='o')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Customer Name')
plt.ylabel('Amount ($)')
plt.title('Top High-Value Customers: Sales vs Profit')
plt.legend()
plt.tight_layout()
plt.savefig('high_value_customers_analysis.png')
plt.show()

#scatter plot for  the repeat cust.
plt.figure(figsize=(10, 6))
plt.scatter(repeat_customers['order_count'], repeat_customers['total_profit'], s=repeat_customers['total_sales'] / 100, alpha=0.7, color='green')
plt.xlabel('Order Count')
plt.ylabel('Total Profit ($)')
plt.title('Repeat Customers: Order Count vs Profit')
plt.grid(visible=True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('repeat_customers_analysis.png')
plt.show()