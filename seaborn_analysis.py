import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- GLOBAL STYLE ----------------
sns.set_theme(style="whitegrid", palette="Set2")
plt.rcParams["figure.figsize"] = (10,5)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

# ---------------- DATA ----------------
df = pd.read_csv(r"D:\Seaborn\large_ecommerce_sales_data.csv").head(200)
df["order_date"] = pd.to_datetime(df["order_date"])


# BAR PLOT – Revenue by Category

cat_rev = df.groupby("product_category")["revenue"].sum().reset_index()

ax = sns.barplot(data=cat_rev, x="product_category", y="revenue")
plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=30)

# value labels
for i, v in enumerate(cat_rev["revenue"]):
    ax.text(i, v, f"{int(v)}", ha="center", va="bottom")

plt.show()


# BOX PLOT – City-wise Revenue

sns.boxplot(data=df, x="city", y="revenue",
            hue="gender", showfliers=False)
plt.title("City-wise Revenue Distribution")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()


# SCATTER PLOT – Age vs Revenue

sns.scatterplot(
    data=df, x="age", y="revenue",
    hue="gender", size="quantity",
    sizes=(40, 300), alpha=0.7
)
plt.title("Age vs Revenue by Gender")
plt.xlabel("Age")
plt.ylabel("Revenue")
plt.show()


# COUNT PLOT – Payment Mode

sns.countplot(data=df, x="payment_mode", hue="gender")
plt.title("Payment Mode Preference")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Orders")
plt.show()


# LINE PLOT – Monthly Revenue Trend
df["month"] = df["order_date"].dt.to_period("M").astype(str)
monthly = df.groupby("month")["revenue"].sum().reset_index()

sns.lineplot(data=monthly, x="month", y="revenue",
             marker="o", linewidth=2)
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()


# HEATMAP – Correlation

corr = df[["price","quantity","rating","revenue","age"]].corr()

sns.heatmap(
    corr, annot=True, fmt=".2f",
    cmap="coolwarm", linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.show()


# PAIR PLOT – Numerical Relations

sns.pairplot(
    df[["price","quantity","rating","revenue"]],
    diag_kind="kde"
)
plt.show()


# STRIP PLOT – Quantity vs Revenue

sns.stripplot(
    data=df, x="quantity", y="revenue",
    hue="gender", jitter=True,
    dodge=True, alpha=0.6
)
plt.title("Quantity vs Revenue by Gender")
plt.xlabel("Quantity")
plt.ylabel("Revenue")
plt.show()
