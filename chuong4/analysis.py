# =========================
# ANALYSIS - TMĐT
# =========================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

sns.set(style="whitegrid")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("superstore_final.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

print("Dữ liệu:", df.shape)
print(df.head())

# =========================
# 1. DOANH THU THEO THÁNG
# =========================
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10,5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker="o")
plt.title("Xu hướng doanh thu theo tháng")
plt.xlabel("Tháng")
plt.ylabel("Doanh thu")
plt.show()

# =========================
# 2. TOP SẢN PHẨM
# =========================
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(8,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top sản phẩm bán chạy")
plt.xlabel("Doanh thu")
plt.show()

# =========================
# 3. DOANH THU THEO KHU VỰC
# =========================
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(6,6))
plt.pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%")
plt.title("Doanh thu theo khu vực")
plt.show()

# =========================
# 4. MODEL DỰ BÁO
# =========================
df = df.sort_values("Order Date")
df["Time"] = np.arange(len(df))

X = df[["Time"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

pred = model.predict(X)

# Đánh giá
mae = mean_absolute_error(y, pred)
rmse = np.sqrt(mean_squared_error(y, pred))

print("\nĐánh giá model:")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))

# Vẽ
plt.figure(figsize=(10,5))
plt.plot(y.values, label="Thực tế")
plt.plot(pred, label="Dự đoán")
plt.legend()
plt.title("Dự báo doanh thu")
plt.show()