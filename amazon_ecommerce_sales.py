import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import os

# -------------------- DATABASE CONNECTION --------------------
def create_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@123",
        database="amazon_project"
    )

# -------------------- LOAD DATA --------------------
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['revenue'] = df['price'] * df['quantity']
    df['month'] = df['order_date'].dt.month
    return df

sns.set_theme(
    style="whitegrid",
    palette="Set2",
    font_scale=1.1
)

plt.rcParams["figure.figsize"] = (10,5)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

# -------------------- EDA FUNCTIONS --------------------
def plot_monthly_sales(df):
    monthly_sales = df.groupby("month")["revenue"].sum()
    plt.figure()
    monthly_sales.plot()
    plt.title("Monthly Sales Trend",fontsize=15)
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()

def plot_category_revenue(df):
    top_category = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)
    plt.figure()
    sns.barplot(x=top_category.index, y=top_category.values)
    plt.xticks(rotation=45)
    plt.title("Revenue by Product Category",fontsize=15)
    plt.ylabel("Total Revenue")
    plt.show()

def plot_rating_distribution(df):
    plt.figure()
    sns.histplot(df['rating'], bins=10)
    plt.title("Customer Rating Distribution",fontsize=15)
    plt.show()

def plot_violin_revenue(df):
    plt.figure(figsize=(10,5))
    sns.violinplot(x="product_category", y="revenue", data=df,
    inner="quartile",cut=0,hue="gender")
    plt.xticks(rotation=45)
    plt.title("Revenue Distribution by Product Category",fontsize=15)
    plt.show()

def plot_payment_box(df):
    plt.figure(figsize=(10,5))
    sns.boxplot(x="payment_mode", y="revenue", data=df,
    showfliers=True)
    plt.xticks(rotation=45)
    plt.title("Revenue by Payment Mode",fontsize=15)
    plt.show()

def plot_gender_count(df):
    plt.figure()
    sns.countplot(x="gender", data=df)
    plt.title("Orders by Gender",fontsize=15)
    plt.show()

def plot_heatmap(df):
    pivot = df.pivot_table(values="revenue", index="product_category", columns="month", aggfunc="sum")
    plt.figure(figsize=(12,6))
    sns.heatmap(pivot, cmap="YlGnBu",linewidth=0.5,fmt=".0f")
    plt.title("Monthly Revenue Heatmap by Category",fontsize=15)
    plt.show()

def plot_price_revenue(df):
    plt.figure()
    sns.scatterplot(x="price", y="revenue", hue="product_category",
     data=df,alpha=0.7)
    plt.title("Price vs Revenue Relationship",fontsize=15)
    plt.show()

# -------------------- MAIN FUNCTION --------------------
def main():
    FILE_PATH = r"D:\Amazon_sales\amazon_ecommerce_sales_dataset.csv"
    df = load_data(FILE_PATH)

    plot_monthly_sales(df)
    plot_category_revenue(df)
    plot_rating_distribution(df)
    plot_violin_revenue(df)
    plot_payment_box(df)
    plot_gender_count(df)
    plot_heatmap(df)
    plot_price_revenue(df)

    df.to_csv("D:\Amazon_sales\clean_amazon_data.csv", index=False)

if __name__ == "__main__":
    main()
