# ==========================================
# KỊCH BẢN PHÂN TÍCH DỮ LIỆU THƯƠNG MẠI ĐIỆN TỬ
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Thiết lập phong cách chung cho các biểu đồ
sns.set_theme(style="whitegrid")

# =========================
# 0. TẢI VÀ KIỂM TRA DỮ LIỆU
# =========================
file_path = "superstore_final.csv"
print(f"Đang tải dữ liệu từ: {file_path}")

df = pd.read_csv(file_path)

# Đảm bảo cột ngày tháng đúng định dạng datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

print("Kích thước dữ liệu:", df.shape)
print(df.head())

# =========================
# 1. PHÂN TÍCH DOANH THU THEO THÁNG TRONG NĂM
# =========================
# Nhóm dữ liệu theo tháng (1 đến 12) để xem tính mùa vụ
monthly_seasonality = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_seasonality.index, y=monthly_seasonality.values, marker="o", color="blue")
plt.title("Xu Hướng Doanh Thu Mùa Vụ Theo Tháng", fontsize=14, pad=15)
plt.xlabel("Tháng", fontsize=12)
plt.ylabel("Tổng Doanh Thu", fontsize=12)
plt.xticks(range(1, 13)) # Đảm bảo trục x hiển thị đủ 12 tháng
plt.tight_layout()
plt.show()

# =========================
# 2. PHÂN TÍCH TOP SẢN PHẨM BÁN CHẠY NHẤT
# =========================
top_10_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_products.values, y=top_10_products.index, palette="viridis")
plt.title("Top 10 Sản Phẩm Đóng Góp Doanh Thu Cao Nhất", fontsize=14, pad=15)
plt.xlabel("Tổng Doanh Thu", fontsize=12)
plt.ylabel("Tên Sản Phẩm", fontsize=12)
plt.tight_layout()
plt.show()

# =========================
# 3. PHÂN BỔ DOANH THU THEO KHU VỰC
# =========================
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7, 7))
plt.pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%", startangle=140, cmap="Set3")
plt.title("Tỷ Trọng Doanh Thu Theo Khu Vực", fontsize=14, pad=15)
plt.tight_layout()
plt.show()

# =========================
# 4. MÔ HÌNH DỰ BÁO XU HƯỚNG DOANH THU (THEO THÁNG)
# =========================
print("\nĐang xây dựng mô hình dự báo...")

# BƯỚC A: Tiền xử lý dữ liệu chuỗi thời gian (Gom nhóm theo từng tháng/năm cụ thể)
# Chuyển đổi 'Order Date' thành định dạng chu kỳ tháng (VD: 2023-01)
monthly_trends = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()

# Tạo biến thời gian liên tục (0, 1, 2...) để đưa vào mô hình hồi quy
monthly_trends["Time_Index"] = np.arange(len(monthly_trends))

X = monthly_trends[["Time_Index"]]
y = monthly_trends["Sales"]

# BƯỚC B: Chia tập dữ liệu (80% Huấn luyện, 20% Kiểm thử)
train_size = int(len(monthly_trends) * 0.8)
X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

# BƯỚC C: Huấn luyện mô hình Hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# BƯỚC D: Dự đoán trên tập kiểm thử
y_pred = model.predict(X_test)

# Đánh giá độ lỗi của mô hình trên dữ liệu chưa từng thấy
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("=== ĐÁNH GIÁ MÔ HÌNH (TẬP TEST) ===")
print(f"Chỉ số MAE  : {mae:,.2f}")
print(f"Chỉ số RMSE : {rmse:,.2f}")

# BƯỚC E: Trực quan hóa kết quả dự báo
plt.figure(figsize=(12, 6))
# Vẽ đường dữ liệu thực tế
plt.plot(monthly_trends["Time_Index"], monthly_trends["Sales"], label="Doanh Thu Thực Tế", marker="o", color="blue")
# Vẽ đường xu hướng mà mô hình dự báo
plt.plot(X_test["Time_Index"], y_pred, label="Doanh Thu Dự Báo (Test Set)", linestyle="--", color="red", linewidth=2)

plt.title("Dự Báo Xu Hướng Tổng Doanh Thu Hàng Tháng", fontsize=14, pad=15)
plt.xlabel("Trục Thời Gian (Tháng tăng dần)", fontsize=12)
plt.ylabel("Tổng Doanh Thu", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()
