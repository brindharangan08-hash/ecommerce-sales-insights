import pandas as pd
import matplotlib.pyplot as plt

# -------- Settings --------
DATA_PATH = "ecommerce_sales.csv"

# -------- Load & Prep --------
df = pd.read_csv(DATA_PATH)
df["Revenue"] = df["Quantity"] * df["Price"]
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

# -------- Basic EDA --------
print("Rows, Columns:", df.shape)
print("\nColumns:", list(df.columns))
print("\nNulls per column:\n", df.isna().sum())
print("\nSample rows:\n", df.head())

# -------- KPIs --------
total_revenue = df["Revenue"].sum()
orders = df["OrderID"].nunique()
customers = df["Customer"].nunique()

print(f"\nTotal Revenue: {total_revenue}")
print(f"Total Orders: {orders}")
print(f"Unique Customers: {customers}")

# -------- Aggregations --------
product_sales = df.groupby("Product", as_index=True)["Revenue"].sum().sort_values(ascending=False)
category_sales = df.groupby("Category", as_index=True)["Revenue"].sum().sort_values(ascending=False)
monthly_sales = df.groupby("Month", as_index=True)["Revenue"].sum().sort_values()

print("\nRevenue by Product:\n", product_sales)
print("\nRevenue by Category:\n", category_sales)
print("\nMonthly Revenue:\n", monthly_sales)

# -------- Visualizations (saved as PNGs) --------
# 1) Bar chart: Top-selling products
plt.figure()
product_sales.plot(kind="bar")
plt.title("Top-Selling Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("product_revenue_bar.png")
plt.close()

# 2) Pie chart: Category-wise revenue share
plt.figure()
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category-wise Revenue Share")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_revenue_pie.png")
plt.close()

# 3) Line chart: Monthly revenue trend
plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png")
plt.close()

print("\nSaved figures: product_revenue_bar.png, category_revenue_pie.png, monthly_revenue_trend.png")
