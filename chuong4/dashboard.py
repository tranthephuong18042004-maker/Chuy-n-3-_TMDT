import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(layout="wide")
sns.set(style="whitegrid")

st.title("Dashboard phân tích dữ liệu TMĐT")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df_raw = pd.read_csv("superstore_cleaned.csv")
    df_clean = pd.read_csv("superstore_final.csv")

    df_clean["Order Date"] = pd.to_datetime(df_clean["Order Date"])
    df_clean["Year"] = df_clean["Order Date"].dt.year
    df_clean["Month"] = df_clean["Order Date"].dt.month

    return df_raw, df_clean

df_raw, df = load_data()

# =========================
# FILTER
# =========================
st.sidebar.header("Bộ lọc")

years = sorted(df["Year"].unique())
selected_year = st.sidebar.selectbox("Chọn năm", years)

regions = sorted(df["Region"].unique())
selected_regions = st.sidebar.multiselect(
    "Chọn khu vực",
    regions,
    default=regions
)

temp_df = df[
    (df["Year"] == selected_year) &
    (df["Region"].isin(selected_regions))
]

products = sorted(temp_df["Product Name"].unique())
selected_product = st.sidebar.selectbox(
    "Chọn sản phẩm",
    ["All"] + list(products)
)

filtered_df = temp_df.copy()

if selected_product != "All":
    filtered_df = filtered_df[
        filtered_df["Product Name"] == selected_product
    ]

# =========================
# TABS
# =========================
tab1, tab2, tab3 = st.tabs(["Data Cleaning", "Dashboard", "Model"])

# =========================
# TAB 1
# =========================
with tab1:
    st.subheader("Dữ liệu trước khi làm sạch")
    st.dataframe(df_raw.head())

    st.subheader("Dữ liệu sau khi làm sạch")
    st.dataframe(df.head())

    col1, col2, col3 = st.columns(3)
    col1.metric("Ban đầu", df_raw.shape[0])
    col2.metric("Sau clean", df.shape[0])
    col3.metric("Đã xóa", df_raw.shape[0] - df.shape[0])

    st.write("Tỷ lệ giữ lại:", round(len(df)/len(df_raw)*100,2), "%")

# =========================
# TAB 2
# =========================
with tab2:

    total_sales = int(filtered_df["Sales"].sum())
    total_orders = filtered_df["Order ID"].nunique()
    avg_sales = int(filtered_df["Sales"].mean())

    col1, col2, col3 = st.columns(3)
    col1.metric("Tổng doanh thu", f"{total_sales:,}")
    col2.metric("Số đơn", total_orders)
    col3.metric("TB/đơn", f"{avg_sales:,}")

    # Trend
    trend = filtered_df.groupby("Month")["Sales"].sum().reset_index()
    fig1, ax1 = plt.subplots()
    sns.lineplot(data=trend, x="Month", y="Sales", marker="o", ax=ax1)
    st.pyplot(fig1)
    fig1.savefig("trend.png")

    # Top product
    top_products = (
        filtered_df.groupby("Product Name")["Sales"]
        .sum().sort_values(ascending=False).head(10).reset_index()
    )
    fig2, ax2 = plt.subplots()
    sns.barplot(data=top_products, x="Sales", y="Product Name", ax=ax2)
    st.pyplot(fig2)
    fig2.savefig("top.png")

    # Region
    region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()
    fig3, ax3 = plt.subplots()
    ax3.pie(region_sales["Sales"], labels=region_sales["Region"], autopct="%1.1f%%")
    st.pyplot(fig3)
    fig3.savefig("region.png")

    st.dataframe(filtered_df.head(20))

# =========================
# TAB 3
# =========================
with tab3:
    df_model = filtered_df.sort_values("Order Date").copy()
    df_model["Time"] = np.arange(len(df_model))

    X = df_model[["Time"]]
    y = df_model["Sales"]

    lr = LinearRegression().fit(X, y)
    rf = RandomForestRegressor().fit(X, y)

    pred_lr = lr.predict(X)
    pred_rf = rf.predict(X)

    fig4, ax4 = plt.subplots()
    ax4.plot(y.values)
    ax4.plot(pred_lr)
    ax4.plot(pred_rf)
    st.pyplot(fig4)
    fig4.savefig("forecast.png")

# =========================
# EXPORT PDF
# =========================
st.subheader("Xuất báo cáo PDF")

if st.button("Tạo PDF Report"):

    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"report_{today}.pdf"

    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("BÁO CÁO PHÂN TÍCH TMĐT", styles["Title"]))
    content.append(Spacer(1,10))

    content.append(Paragraph(f"Tổng doanh thu: {total_sales:,}", styles["Normal"]))
    content.append(Paragraph(f"Số đơn hàng: {total_orders}", styles["Normal"]))
    content.append(Paragraph(f"Trung bình đơn: {avg_sales:,}", styles["Normal"]))
    content.append(Spacer(1,20))

    content.append(Paragraph("Xu hướng doanh thu", styles["Heading2"]))
    content.append(Image("trend.png", width=400, height=200))

    content.append(Paragraph("Top sản phẩm", styles["Heading2"]))
    content.append(Image("top.png", width=400, height=200))

    content.append(Paragraph("Doanh thu theo khu vực", styles["Heading2"]))
    content.append(Image("region.png", width=400, height=200))

    content.append(Paragraph("Dự báo doanh thu", styles["Heading2"]))
    content.append(Image("forecast.png", width=400, height=200))

    doc.build(content)

    st.success(f"Đã tạo {file_name}")