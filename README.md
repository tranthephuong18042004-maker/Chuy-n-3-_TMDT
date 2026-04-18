# 📊 ĐỒ ÁN PHÂN TÍCH DỮ LIỆU TMĐT

## 📌 Giới thiệu

Dự án xây dựng hệ thống **phân tích dữ liệu thương mại điện tử (TMĐT)** bằng Python, bao gồm:

* Làm sạch dữ liệu
* Phân tích và trực quan hóa
* Xây dựng dashboard
* Dự báo doanh thu

---

## 📂 Cấu trúc project

```
Chuyen de 3_TMDT/
│── clean.py                # Làm sạch dữ liệu
│── analysis.py             # Phân tích dữ liệu
│── dashboard.py            # Dashboard Streamlit
│── superstore_cleaned.csv  # Dữ liệu gốc
│── superstore_final.csv    # Dữ liệu sau xử lý
│── report_2026-04-13.pdf   # Báo cáo kết quả
│── README.md
```

---
📂 Dataset
Nguồn: Kaggle (Superstore Dataset)
Số lượng bản ghi ban đầu: 9994 dòng
Số lượng sau khi làm sạch: 9994 dòng
Số dòng bị loại bỏ: 0 dòng
Tỷ lệ dữ liệu giữ lại: 100%

👉 Nhận xét:
Dataset có chất lượng tốt, không có dữ liệu thiếu hoặc trùng lặp đáng kể, phù hợp để phân tích trực tiếp.
## ⚙️ Công nghệ sử dụng

## ⚙️ Công nghệ sử dụng

### 🐍 Python

Ngôn ngữ lập trình chính của dự án. Python được lựa chọn nhờ:

* Cú pháp đơn giản, dễ đọc
* Hỗ trợ mạnh mẽ cho phân tích dữ liệu
* Có nhiều thư viện phục vụ Data Science

👉 Toàn bộ hệ thống (cleaning, analysis, dashboard, model) đều được xây dựng bằng Python.

---

### 📊 Pandas & NumPy

#### 🔹 Pandas

Thư viện xử lý dữ liệu dạng bảng (DataFrame), được sử dụng để:

* Đọc và ghi file CSV
* Làm sạch dữ liệu (dropna, drop_duplicates)
* Xử lý thời gian (datetime)
* Nhóm dữ liệu (groupby) để tính toán doanh thu

#### 🔹 NumPy

Thư viện xử lý số học, hỗ trợ:

* Tạo biến thời gian cho mô hình (`np.arange`)
* Tính toán nhanh và tối ưu hiệu suất

---

### 📈 Matplotlib & Seaborn

Hai thư viện trực quan hóa dữ liệu:

#### 🔹 Matplotlib

* Vẽ biểu đồ cơ bản
* Tùy chỉnh chi tiết (trục, tiêu đề, legend)

#### 🔹 Seaborn

* Xây dựng trên Matplotlib
* Giao diện đẹp, chuyên nghiệp hơn
* Dùng để vẽ:

  * Line chart (xu hướng doanh thu)
  * Bar chart (top sản phẩm)
  * Boxplot (nếu mở rộng)

👉 Giúp chuyển dữ liệu thành hình ảnh dễ hiểu.

---

### 🤖 Scikit-learn (Machine Learning)

Thư viện Machine Learning phổ biến trong Python.

#### Mô hình sử dụng:

* **Linear Regression**

  * Dùng để dự đoán xu hướng doanh thu theo thời gian
  * Dễ triển khai, phù hợp dữ liệu cơ bản

* (Mở rộng) Random Forest

  * Mô hình nâng cao giúp cải thiện độ chính xác

👉 Giúp hệ thống không chỉ phân tích mà còn dự đoán.

---

### 📊 Streamlit (Dashboard)

Framework tạo web app bằng Python.

Được sử dụng để:

* Xây dựng dashboard tương tác
* Hiển thị:

  * KPI (doanh thu, đơn hàng)
  * Biểu đồ
  * Bảng dữ liệu
* Tạo bộ lọc:

  * Theo năm
  * Theo khu vực
  * Theo sản phẩm

👉 Giúp người dùng dễ dàng tương tác với dữ liệu mà không cần code.

---

### 📄 ReportLab (Xuất PDF)

Thư viện tạo file PDF tự động.

Được sử dụng để:

* Xuất báo cáo từ dashboard
* Chèn:

  * KPI
  * Biểu đồ
  * Nội dung phân tích
* Tự động đặt tên file theo ngày

👉 Giúp tự động hóa báo cáo giống hệ thống doanh nghiệp.

---

## 🎯 Tổng kết

Các công nghệ được kết hợp tạo thành một hệ thống hoàn chỉnh:

```text
Python → Xử lý dữ liệu
Pandas → Làm sạch & phân tích
Seaborn → Trực quan hóa
Scikit-learn → Dự báo
Streamlit → Dashboard
ReportLab → Báo cáo PDF
```

👉 Hệ thống đáp ứng đầy đủ quy trình:
**Data Cleaning → Analysis → Visualization → Modeling → Reporting**

---

## 🧹 1. Làm sạch dữ liệu

## 🧹 Data Cleaning – Giải thích chi tiết

### 📄 File: `clean.py`

### 🎯 Mục tiêu

Biến dữ liệu thô (raw data) thành dữ liệu sạch (clean data) để phục vụ phân tích và xây dựng mô hình.

---

## 🔄 QUY TRÌNH BIẾN ĐỔI DỮ LIỆU

---

### 🔹 Bước 1: Dữ liệu ban đầu

Dữ liệu gốc (`superstore_cleaned.csv`) có dạng:

| Order ID | Order Date | Product Name | Region | Sales |
| -------- | ---------- | ------------ | ------ | ----- |

👉 Vấn đề có thể gặp:

* Có dòng trùng
* Có giá trị thiếu
* Dữ liệu ngày dạng chuỗi (string)
* Sales có thể không phải số

---

### 🔹 Bước 2: Làm sạch dữ liệu

#### ✔ Xóa dữ liệu trùng

```python
df = df.drop_duplicates()
```

👉 Loại bỏ các dòng bị lặp lại

---

#### ✔ Xóa dữ liệu thiếu

```python
df = df.dropna()
```

👉 Loại bỏ các dòng có giá trị null

---

#### ✔ Chuẩn hóa kiểu dữ liệu

```python
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
```

👉 Sau bước này:

| Cột        | Trước        | Sau      |
| ---------- | ------------ | -------- |
| Order Date | string       | datetime |
| Sales      | string/float | numeric  |

---

#### ✔ Xóa dữ liệu lỗi

```python
df = df.dropna(subset=["Order Date", "Sales"])
df = df[df["Sales"] > 0]
```

👉 Loại bỏ:

* Ngày lỗi (không parse được)
* Sales ≤ 0

---

### 🔹 Bước 3: Tạo cột mới (Feature Engineering)

👉 Đây là bước QUAN TRỌNG nhất 🔥

---

#### ✔ Tạo cột Year

```python
df["Year"] = df["Order Date"].dt.year
```

👉 Ví dụ:

| Order Date | Year |
| ---------- | ---- |
| 2017-06-12 | 2017 |

👉 Mục đích:

* Lọc dữ liệu theo năm
* Dùng trong dashboard

---

#### ✔ Tạo cột Month

```python
df["Month"] = df["Order Date"].dt.month
```

👉 Ví dụ:

| Order Date | Month |
| ---------- | ----- |
| 2017-06-12 | 6     |

👉 Mục đích:

* Phân tích doanh thu theo tháng
* Vẽ biểu đồ xu hướng

---

### 🔹 Bước 4: Dữ liệu sau khi làm sạch

👉 Dataset cuối cùng (`superstore_final.csv`) có dạng:

| Order ID | Order Date | Product Name | Region | Sales | Year | Month |
| -------- | ---------- | ------------ | ------ | ----- | ---- | ----- |

---

## 🎯 TÓM TẮT THAY ĐỔI

```text
Trước:
5 cột (raw data)

Sau:
7 cột (clean + feature)
```

---

## 💡 Ý NGHĨA CỦA VIỆC THÊM CỘT

| Cột   | Vai trò                      |
| ----- | ---------------------------- |
| Year  | Lọc dữ liệu theo năm         |
| Month | Phân tích xu hướng doanh thu |

👉 Nếu không có 2 cột này:

* ❌ Không vẽ được biểu đồ theo tháng
* ❌ Dashboard không lọc được

---

## 🏆 KẾT LUẬN

Quá trình Data Cleaning đã:

* Loại bỏ dữ liệu không hợp lệ
* Chuẩn hóa dữ liệu
* Tạo thêm đặc trưng (feature)

👉 Giúp dữ liệu sẵn sàng cho:

* Phân tích (EDA)
* Trực quan hóa
* Xây dựng mô hình dự báo

---

## 📊 2. Phân tích dữ liệu

## 📊 Data Analysis – Giải thích chi tiết

### 📄 File: `analysis.py`

---

## 🎯 Mục tiêu

Thực hiện phân tích dữ liệu (EDA) và xây dựng mô hình dự báo nhằm:

* Hiểu xu hướng bán hàng
* Xác định sản phẩm nổi bật
* Phân tích khu vực hiệu quả
* Dự đoán doanh thu trong tương lai

---

# 🔍 1. Phân tích doanh thu theo tháng

### ✔ Cách thực hiện:

```python
monthly_sales = df.groupby("Month")["Sales"].sum()
```

👉 Nhóm dữ liệu theo tháng và tính tổng doanh thu

---

### 📊 Kết quả:

* Biểu đồ đường (Line chart)
* Trục X: Tháng (1 → 12)
* Trục Y: Doanh thu

---

### 🎯 Ý nghĩa:

* Xác định tháng bán chạy nhất
* Phát hiện xu hướng theo thời gian
* Hỗ trợ quyết định kinh doanh (khuyến mãi, nhập hàng)

---

---

# 🔥 2. Top sản phẩm bán chạy

### ✔ Cách thực hiện:

```python
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
```

---

### 📊 Kết quả:

* Biểu đồ cột (Bar chart)
* Hiển thị Top 10 sản phẩm

---

### 🎯 Ý nghĩa:

* Xác định sản phẩm chủ lực
* Tập trung marketing vào sản phẩm bán tốt
* Loại bỏ sản phẩm kém hiệu quả

---

---

# 🌍 3. Doanh thu theo khu vực

### ✔ Cách thực hiện:

```python
region_sales = df.groupby("Region")["Sales"].sum()
```

---

### 📊 Kết quả:

* Biểu đồ tròn (Pie chart)
* Tỷ lệ doanh thu theo từng khu vực

---

### 🎯 Ý nghĩa:

* Biết khu vực nào mang lại doanh thu cao
* Tối ưu chiến lược phân phối
* Phát hiện thị trường tiềm năng

---

---

# 🤖 4. Dự báo doanh thu (Machine Learning)

---

## ✔ Chuẩn bị dữ liệu

```python
df = df.sort_values("Order Date")
df["Time"] = np.arange(len(df))
```

👉 Tạo biến `Time` để biểu diễn dòng thời gian

---

## ✔ Xây dựng mô hình

```python
model = LinearRegression()
model.fit(X, y)
```

* X = Time (biến độc lập)
* y = Sales (biến phụ thuộc)

---

## ✔ Dự đoán

```python
pred = model.predict(X)
```

---

## 📊 Kết quả:

* Biểu đồ:

  * Đường thực tế
  * Đường dự đoán

---

## 🎯 Ý nghĩa:

* Dự đoán xu hướng doanh thu
* Hỗ trợ lập kế hoạch kinh doanh
* Hiểu xu hướng tăng/giảm

---

---

# 📏 5. Đánh giá mô hình

---

## ✔ MAE (Mean Absolute Error)

```python
MAE = mean_absolute_error(y, pred)
```

👉 Công thức:

```text
MAE = trung bình |y - y_pred|
```

### 🎯 Ý nghĩa:

* Sai số trung bình giữa giá trị thực và dự đoán
* Dễ hiểu, trực quan

👉 Ví dụ:

```text
MAE = 50 → sai lệch trung bình 50 đơn vị doanh thu
```

---

## ✔ RMSE (Root Mean Squared Error)

```python
RMSE = sqrt(mean_squared_error(y, pred))
```

👉 Công thức:

```text
RMSE = sqrt((y - y_pred)^2)
```

---

### 🎯 Ý nghĩa:

* Phạt nặng sai số lớn
* Đánh giá độ chính xác mô hình tốt hơn MAE

---

## 🔍 So sánh MAE vs RMSE

| Chỉ số | Ý nghĩa           |
| ------ | ----------------- |
| MAE    | Sai số trung bình |
| RMSE   | Nhạy với lỗi lớn  |

---

# 🏆 KẾT LUẬN

Quá trình phân tích đã:

✔ Xác định xu hướng doanh thu theo thời gian
✔ Tìm ra sản phẩm bán chạy nhất
✔ Phân tích hiệu quả theo khu vực
✔ Xây dựng mô hình dự báo doanh thu

👉 Hệ thống giúp:

* Hỗ trợ ra quyết định kinh doanh
* Tối ưu chiến lược bán hàng
* Dự đoán xu hướng tương lai

---

## 🔥 TỔNG QUY TRÌNH

```text
Data Cleaning → EDA → Visualization → Modeling → Evaluation
```


---

## 📈 3. Dashboard (Giao diện)

## 📊 Dashboard – Giải thích chi tiết

### 📄 File: `dashboard.py`

---

## 🎯 Mục tiêu

Xây dựng hệ thống dashboard tương tác giúp:

* Theo dõi tình hình kinh doanh
* Phân tích dữ liệu trực quan
* Hỗ trợ ra quyết định
* Xuất báo cáo tự động

---

# ⚙️ Công nghệ sử dụng

* **Streamlit**: xây dựng giao diện web
* **Pandas**: xử lý dữ liệu
* **Seaborn / Matplotlib**: vẽ biểu đồ
* **Scikit-learn**: mô hình dự báo
* **ReportLab**: xuất báo cáo PDF

---

# 🎛️ 1. Bộ lọc dữ liệu (Filter)

### ✔ Chức năng:

Cho phép người dùng lựa chọn dữ liệu cần phân tích:

* Năm (`Year`)
* Khu vực (`Region`)
* Sản phẩm (`Product Name`)

---

### ✔ Cách hoạt động:

```python
filtered_df = df[
    (df["Year"] == selected_year) &
    (df["Region"].isin(selected_regions))
]
```

👉 Sau đó lọc tiếp theo sản phẩm

---

### 🎯 Ý nghĩa:

* Tăng tính tương tác
* Phân tích theo từng nhóm dữ liệu cụ thể
* Giống dashboard thực tế doanh nghiệp

---

# 📊 2. KPI (Chỉ số tổng quan)

### ✔ Bao gồm:

| Chỉ số         | Ý nghĩa                    |
| -------------- | -------------------------- |
| Tổng doanh thu | Tổng Sales                 |
| Số đơn hàng    | Số Order ID                |
| Trung bình đơn | Giá trị trung bình mỗi đơn |

---

### ✔ Cách tính:

```python
total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()
avg_sales = df["Sales"].mean()
```

---

### 🎯 Ý nghĩa:

* Cung cấp cái nhìn nhanh về hiệu suất kinh doanh
* Hỗ trợ ra quyết định nhanh

---

# 📈 3. Biểu đồ trực quan

---

## 🔹 Xu hướng doanh thu

* Biểu đồ: Line chart
* Trục X: Tháng
* Trục Y: Doanh thu

👉 Dùng để:

* Phát hiện xu hướng tăng/giảm
* Xác định mùa cao điểm

---

## 🔹 Top sản phẩm

* Biểu đồ: Bar chart
* Hiển thị Top 10 sản phẩm

👉 Dùng để:

* Xác định sản phẩm bán chạy
* Tối ưu chiến lược kinh doanh

---

## 🔹 Doanh thu theo khu vực

* Biểu đồ: Pie chart

👉 Dùng để:

* So sánh hiệu suất giữa các khu vực
* Tìm thị trường tiềm năng

---

## 🔹 Dự báo doanh thu

* Biểu đồ:

  * Đường thực tế
  * Đường dự đoán

👉 Dùng để:

* Nhìn xu hướng tương lai
* Hỗ trợ lập kế hoạch

---

# 🤖 4. Mô hình dự báo

### ✔ Sử dụng:

* Linear Regression
* Random Forest

---

### ✔ Quy trình:

1. Sắp xếp dữ liệu theo thời gian
2. Tạo biến `Time`
3. Huấn luyện mô hình
4. Dự đoán

---

### 🎯 Ý nghĩa:

* Dự đoán doanh thu
* So sánh độ chính xác giữa các mô hình

---

# 📄 5. Xuất báo cáo PDF

### ✔ Chức năng:

* Xuất báo cáo tự động từ dashboard
* Tự động đặt tên theo ngày

---

### ✔ Nội dung báo cáo:

* KPI
* Biểu đồ:

  * Xu hướng doanh thu
  * Top sản phẩm
  * Khu vực
  * Dự báo

---

### 🎯 Ý nghĩa:

* Tự động hóa báo cáo
* Giống hệ thống BI thực tế
* Tiết kiệm thời gian

---

# 🧩 6. Luồng hoạt động

```text
Load Data → Filter → KPI → Chart → Model → Export PDF
```

---

# 🏆 KẾT LUẬN

Dashboard đã xây dựng thành công hệ thống:

✔ Tương tác dữ liệu
✔ Trực quan hóa chuyên nghiệp
✔ Tích hợp Machine Learning
✔ Xuất báo cáo tự động

👉 Hệ thống có thể áp dụng thực tế trong doanh nghiệp TMĐT để:

* Theo dõi doanh thu
* Phân tích hiệu quả sản phẩm
* Dự báo xu hướng kinh doanh

---

# 🚀 ĐIỂM MẠNH

* Giao diện trực quan (Streamlit)
* Dễ sử dụng
* Tích hợp đầy đủ pipeline Data Analytics
* Có khả năng mở rộng


## 📑 4. Báo cáo (Report)

### 📄 File:

`report_2026-04-13.pdf`

---

## 🎯 Mục tiêu

Báo cáo được xuất tự động từ hệ thống dashboard nhằm:

* Tổng hợp các chỉ số quan trọng
* Trình bày kết quả phân tích dữ liệu
* Hỗ trợ ra quyết định kinh doanh

---

## 📊 Nội dung báo cáo

### 🔹 1. Chỉ số tổng quan (KPI)

* **Tổng doanh thu:** 484,247
* **Số đơn hàng:** 969
* **Trung bình mỗi đơn:** 242

👉 Ý nghĩa:

* Tổng doanh thu phản ánh hiệu suất kinh doanh
* Số đơn hàng thể hiện mức độ hoạt động
* Giá trị trung bình giúp đánh giá sức mua khách hàng

---

### 🔹 2. Phân tích dữ liệu

Báo cáo bao gồm các biểu đồ trực quan:

#### 📈 Xu hướng doanh thu

* Thể hiện doanh thu theo từng tháng
* Giúp nhận diện xu hướng tăng/giảm

---

#### 🔥 Top sản phẩm

* Hiển thị các sản phẩm bán chạy nhất
* Hỗ trợ quyết định về chiến lược sản phẩm

---

#### 🌍 Doanh thu theo khu vực

* So sánh hiệu suất giữa các khu vực
* Xác định thị trường tiềm năng

---

### 🔹 3. Dự báo doanh thu

* Sử dụng mô hình **Linear Regression** và **Random Forest**
* Biểu đồ gồm:

  * Đường dữ liệu thực tế
  * Đường dự đoán

👉 Ý nghĩa:

* Dự đoán xu hướng doanh thu trong tương lai
* Hỗ trợ lập kế hoạch kinh doanh

---

## ⚙️ Đặc điểm nổi bật

* Báo cáo được tạo **tự động từ dashboard**
* Cập nhật theo dữ liệu mới nhất
* Định dạng rõ ràng, dễ đọc
* Tích hợp đầy đủ:

  * KPI
  * Biểu đồ
  * Dự báo

---

## 🏆 Kết luận

Báo cáo cung cấp cái nhìn toàn diện về hoạt động kinh doanh TMĐT, giúp:

* Theo dõi hiệu suất
* Phân tích xu hướng
* Hỗ trợ ra quyết định

👉 Đây là bước cuối trong quy trình:

```text
Data Cleaning → Analysis → Dashboard → Reporting
```


## ▶️ Cách chạy project

### 1. Cài thư viện

```bash
pip install pandas matplotlib seaborn numpy scikit-learn streamlit reportlab
```

---

### 2. Làm sạch dữ liệu

```bash
python clean.py
```

---

### 3. Phân tích dữ liệu

```bash
python analysis.py
```

---

### 4. Chạy dashboard

```bash
streamlit run dashboard.py
```

---

## 📌 Kết quả đạt được

* Xây dựng pipeline xử lý dữ liệu hoàn chỉnh
* Trực quan hóa dữ liệu rõ ràng
* Dự báo doanh thu cơ bản
* Tạo dashboard tương tác
* Xuất báo cáo PDF tự động

---
