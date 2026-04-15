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
Chuy-n-3-_TMDT/
│── clean.py                # Làm sạch dữ liệu
│── analysis.py             # Phân tích dữ liệu
│── dashboard.py            # Dashboard Streamlit
│── superstore_cleaned.csv  # Dữ liệu gốc
│── superstore_final.csv    # Dữ liệu sau xử lý
│── report_2026-04-13.pdf   # Báo cáo kết quả
│── README.md
```

---

## ⚙️ Công nghệ sử dụng

* Python
* Pandas, Numpy
* Matplotlib, Seaborn
* Scikit-learn (Linear Regression)
* Streamlit (Dashboard)
* ReportLab (Xuất PDF)

---

## 🧹 1. Làm sạch dữ liệu

File: `clean.py`

Chức năng:

* Xóa dữ liệu trùng, thiếu
* Chuẩn hóa kiểu dữ liệu
* Xử lý lỗi ngày và giá trị
* Tạo thêm cột:

  * Year
  * Month

👉 Sau khi xử lý:

* Dữ liệu sạch được lưu vào: `superstore_final.csv` 

---

## 📊 2. Phân tích dữ liệu

File: `analysis.py`

Bao gồm:

* Doanh thu theo tháng
* Top sản phẩm bán chạy
* Doanh thu theo khu vực
* Dự báo doanh thu bằng Linear Regression

👉 Model được đánh giá bằng:

* MAE
* RMSE 

---

## 📈 3. Dashboard (Giao diện)

File: `dashboard.py`

Chạy bằng Streamlit với các chức năng:

* Lọc theo năm, khu vực, sản phẩm
* Hiển thị:

  * Tổng doanh thu
  * Số đơn hàng
  * Trung bình đơn
* Biểu đồ:

  * Xu hướng doanh thu
  * Top sản phẩm
  * Doanh thu theo khu vực
  * Dự báo doanh thu

👉 Có thể export báo cáo PDF tự động 

---

## 📑 4. Báo cáo

File:

* report_2026-04-13.pdf

Nội dung gồm:

* Tổng doanh thu: 484,247
* Số đơn hàng: 969
* Trung bình đơn: 242
* Biểu đồ phân tích & dự báo 

---

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

## 👨‍💻 Tác giả

* Trần Thế Phương

---

## ⭐ Ghi chú

Dự án phục vụ mục đích học tập và nghiên cứu môn **Phân tích dữ liệu TMĐT**
