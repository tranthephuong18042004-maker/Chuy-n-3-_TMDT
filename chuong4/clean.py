# =========================
# CLEAN DATA - TMĐT
# =========================

import pandas as pd

def clean_data(input_file, output_file):
    print("Đang đọc dữ liệu...")

    df = pd.read_csv(input_file, encoding='utf-8-sig')

    print("Dữ liệu ban đầu:", df.shape)

    # =========================
    # 1. CLEANING
    # =========================

    # Xóa khoảng trắng tên cột
    df.columns = df.columns.str.strip()

    # Xóa dòng trùng
    df = df.drop_duplicates()

    # Xóa dữ liệu thiếu
    df = df.dropna()

    # =========================
    # 2. XỬ LÝ KIỂU DỮ LIỆU
    # =========================

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

    # Xóa dòng lỗi
    df = df.dropna(subset=["Order Date", "Sales"])

    # Xóa dữ liệu bất thường
    df = df[df["Sales"] > 0]

    # =========================
    # 3. FEATURE ENGINEERING
    # =========================

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month

    print("Sau khi làm sạch:", df.shape)

    # =========================
    # 4. LƯU FILE
    # =========================

    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Đã lưu file sạch: {output_file}")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    clean_data("superstore_cleaned.csv", "superstore_final.csv")