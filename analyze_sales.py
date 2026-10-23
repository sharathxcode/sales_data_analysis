
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the sales dataset
df = pd.read_csv("sales_data.csv")

# 2. Display the first five rows
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# 3. Check dataset information
print("\n--- DATASET INFORMATION ---")
print(df.info())

# 4. Check for missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 5. Calculate revenue for each order
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# 6. Calculate total revenue
total_revenue = df["Revenue"].sum()
print("\nTotal Revenue: Rs.", total_revenue)

# 7. Calculate total quantity sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# 8. Find revenue by product
product_sales = df.groupby("Product")["Revenue"].sum()
print("\n--- REVENUE BY PRODUCT ---")
print(product_sales.sort_values(ascending=False))

# 9. Find revenue by country
country_sales = df.groupby("Country")["Revenue"].sum()
print("\n--- REVENUE BY COUNTRY ---")
print(country_sales.sort_values(ascending=False))

# 10. Save the analyzed dataset
df.to_csv("analyzed_sales.csv", index=False)

print("\nAnalysis completed successfully!")
print("Saved file: analyzed_sales.csv")



# 11. Create a bar chart: Revenue by Product
product_sales = df.groupby("Product")["Revenue"].sum()
product_sales = product_sales.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("revenue_by_product.png")
plt.show()


# 12. Create a bar chart: Revenue by Country
country_sales = df.groupby("Country")["Revenue"].sum()
country_sales = country_sales.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
country_sales.plot(kind="bar")

plt.title("Revenue by Country")
plt.xlabel("Country")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("revenue_by_country.png")
plt.show()

print("Charts created successfully!")
