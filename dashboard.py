import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


@st.cache_data
def load_data():
    return pd.read_csv('merged_dataset.csv')

merged_df = load_data()
merged_df['Order.Date'] = pd.to_datetime(merged_df['Order.Date'], errors='coerce')
print(f"Order Date Type: {merged_df['Order.Date'].dtype}")

st.title("E-commerce Sales Dashboard")
st.sidebar.header("Filters")

#sidebar filters
date_range = st.sidebar.date_input("Select Date Range", 
                                   [merged_df['Order.Date'].min(), merged_df['Order.Date'].max()])
countries = st.sidebar.multiselect("Select Countries", merged_df['Country'].unique(), merged_df['Country'].unique())

# ensure comparison 
start_date = pd.to_datetime(date_range[0]) if isinstance(date_range[0], datetime.date) else date_range[0]
end_date = pd.to_datetime(date_range[1]) if isinstance(date_range[1], datetime.date) else date_range[1]

#filters
filtered_df = merged_df[
    (merged_df['Order.Date'] >= start_date) &
    (merged_df['Order.Date'] <= end_date) &
    (merged_df['Country'].isin(countries))
]

#ales & profit by country
st.subheader("Sales & Profit by Country")
country_metrics = filtered_df.groupby('Country').agg(
    total_sales=('Sales', 'sum'),
    total_profit=('Profit', 'sum')
).reset_index().sort_values(by='total_sales', ascending=False)

fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.barplot(data=country_metrics.head(10), x='Country', y='total_sales', color='blue', label='Total Sales', ax=ax1)
sns.barplot(data=country_metrics.head(10), x='Country', y='total_profit', color='orange', label='Total Profit', ax=ax1)
ax1.set_title("Top 10 Countries by Sales and Profit")
ax1.legend()
st.pyplot(fig1)

#top products by city
st.subheader("Top Products by City")
product_demand = filtered_df.groupby(['Country', 'City', 'Product Name']).agg(
    total_sales=('Sales', 'sum')
).reset_index().sort_values(by='total_sales', ascending=False)
top_cities_products = product_demand.groupby('City').head(1).reset_index().head(10)

fig2, ax2 = plt.subplots(figsize=(14, 7))
sns.barplot(data=top_cities_products, x='City', y='total_sales', hue='Product Name', dodge=False, palette='viridis', ax=ax2)
ax2.set_title("Top 10 Cities by Product Demand")
st.pyplot(fig2)

#customer behavior
st.subheader("High-Value Customers")
customer_behavior = filtered_df.groupby('Customer.Name').agg(
    total_sales=('Sales', 'sum'),
    total_profit=('Profit', 'sum'),
    order_count=('Order.ID', 'count')
).reset_index()
high_value_customers = customer_behavior[customer_behavior['total_sales'] > customer_behavior['total_sales'].quantile(0.9)]
fig3, ax3 = plt.subplots(figsize=(12, 6))
ax3.bar(high_value_customers['Customer.Name'][:10], high_value_customers['total_sales'][:10], color='skyblue', label='Total Sales')
ax3.plot(high_value_customers['Customer.Name'][:10], high_value_customers['total_profit'][:10], color='red', label='Total Profit')
ax3.set_title("Top High-Value Customers: Sales vs Profit")
st.pyplot(fig3)

#shipping analysis
st.subheader("Shipping Costs vs Profitability")
shipping_profitability = filtered_df.groupby('Ship.Mode').agg(
    avg_shipping_cost=('Shipping.Cost', 'mean'),
    total_profit=('Profit', 'sum')
).reset_index()
fig4, ax4 = plt.subplots(figsize=(10, 6))
ax4.bar(shipping_profitability['Ship.Mode'], shipping_profitability['avg_shipping_cost'], color='skyblue', label='Avg Shipping Cost')
ax4.set_title("Shipping Mode Analysis: Cost vs Profit")
st.pyplot(fig4)

# download feature
st.sidebar.download_button(
    label="Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv"
)
