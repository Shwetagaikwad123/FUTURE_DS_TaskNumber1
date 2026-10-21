import pandas as pd
import numpy as np

#Understanding the dataset
data = pd.read_excel("E:/Shweta/PYTHON/Projects/Hello_python/Business Sales Performance Analytics/Product-Sales-Region.xlsx")
print(data.head())
print(data.columns)
print(data.shape)
print(data.info())

#Data cleaning and validation
print(data.isnull().sum())
print(data.duplicated().sum())
print(data["Promotion"].value_counts(dropna=False))
print(data[data["Promotion"].isna()].head(10))
print(data[data["Promotion"].isna()].shape)
print(data.columns.tolist())
missing_promo = data[data["Promotion"].isna()]
print(missing_promo[["Promotion","Discount","Quantity","UnitPrice"]].head(20))
print(missing_promo["Discount"].value_counts(dropna=False))
print(data.isnull().sum())
data["Promotion_clean"] = data["Promotion"].fillna("Not Recorded")
print(data["Promotion_clean"].value_counts())
print(data[["Quantity","UnitPrice","Discount","TotalPrice"]].head(10))
print(data.describe())
data["CalculatedPrice"] = (data["Quantity"]*data["UnitPrice"]*(1-data["Discount"]))
print(data["CalculatedPrice"])
print((data["TotalPrice"] - data["CalculatedPrice"]).abs().describe())
total_revenue = data["TotalPrice"].sum()
print("Total Revenue: ",total_revenue)
print(f"Total Revenue: ₹{total_revenue:,.2f}")
total_orders = data["OrderID"].nunique()
average_order_value = total_revenue / total_orders
print("Total Orders: ",total_orders)
print(f"Average Order Value: ₹ {average_order_value:,.2f}")
data["Revenue"] = data["Quantity"]*data["UnitPrice"]*(1-data["Discount"])
print(data[["Quantity","UnitPrice","Discount","TotalPrice"]].head(10))
print("TotalPrice and Revenue match: ")
print((data["TotalPrice"]-data["Revenue"]).abs().max())
print(data["OrderDate"].dtype)
data["OrderDate"] = pd.to_datetime(data["OrderDate"])

#Monthly sales trend analysis
import matplotlib.pyplot as plt
#line chart for showing sales trend
data["Month"] = data["OrderDate"].dt.to_period("M")
monthly_sales = data.groupby("Month")["Revenue"].sum()
print(monthly_sales )
monthly_sales.plot(kind="line",marker="o",figsize=(12,6),color= "blue",linewidth=2)
plt.title("Monthly Sales Trend",fontsize=16)
plt.xlabel("Month",fontsize=12)
plt.ylabel("Revenue",fontsize=12)
plt.grid(True, linestyle="--",alpha=0.5)
plt.tight_layout()
plt.savefig("Charts/monthly_trend.png",bbox_inches="tight")
plt.show()
product_quantity = data.groupby("Product")["Quantity"].sum()
print(product_quantity.sort_values(ascending=False))
product_revenue = data.groupby("Product")["Revenue"].sum()
print(product_revenue.sort_values(ascending=False))

#Product performance analysis
#product wise quantity sold
product_quantity.sort_values(ascending=False).plot(
    kind="bar",
    color="skyblue"
)
plt.title("Product-wise Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.ylim(0,3000)
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.savefig("Charts/product_sold.png",bbox_inches="tight")
plt.show()

#product wise revenue
product_revenue.sort_values(ascending=False).plot(
    kind="bar",
    color="orange"
)
plt.title("Product-wise Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.savefig("Charts/product_revenue.png",bbox_inches="tight")
plt.show()

#Regional performance analysis
region_revenue = data.groupby("Region")["Revenue"].sum()
print(region_revenue)
print("Highest Revenue Region: ")
print(region_revenue.idxmax())
print("\nLowest Revenue Region: ")
print(region_revenue.idxmin())
print(region_revenue.sort_values(ascending=False))
plt.figure(figsize=(8,5))
region_revenue.plot(kind="bar",color="teal")
plt.title("Region-wise Revenue")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.grid(axis="y",alpha=0.3)
plt.savefig("Charts/region_revenue.png",bbox_inches="tight")
plt.show()

#Customer type distribution
print(data["CustomerType"].unique())
customer_count = data["CustomerType"].value_counts()
print(customer_count)
customer_revenue = data.groupby("CustomerType")["Revenue"].sum()
print(customer_revenue)
customer_revenue.plot(kind="bar",color=["blue","orange"])
plt.title("Revenue by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.grid(axis="y",alpha=0.3)
plt.savefig("Charts/revenue_by_customer.png",bbox_inches="tight")
plt.show()

#Discount analysis
print(data["Discount"].unique())
discount_count = data["Discount"].value_counts().sort_index()
print(discount_count)
discount_revenue = data.groupby("Discount")["Revenue"].sum()
print(discount_revenue)
discount_revenue.plot(kind="bar",color=["brown"])
plt.title("Revenue by Discount Levle")
plt.xlabel("Discount Rate")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.grid(axis="y",alpha=0.3)
plt.savefig("Charts/revenue_discount.png",bbox_inches="tight")
plt.show()

#Return Analysis
return_count = data["Returned"].value_counts()
print(return_count)
return_percentage = (data["Returned"].sum()/len(data))*100
print("Return_percentage: ",return_percentage)

