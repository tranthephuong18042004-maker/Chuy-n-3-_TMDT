# ========================================================
# CLEAN DATA - TMDT (PRO) - FINAL FULL FIXED VERSION
# ========================================================

import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

# =========================
# 1. CREATE RUN FOLDER
# =========================
def create_run_folder(base_dir):
    run_id = datetime.now().strftime("run_%Y%m%d_%H%M%S")
    path = os.path.join(base_dir, run_id)
    os.makedirs(path, exist_ok=True)
    return path

# =========================
# 2. SAVE TABLE IMAGE (FIXED OVERLAPPING)
# =========================
def save_table_image(df, path):
    df_show = df.head(10)
    
    # Tang kich thuoc ngang (figsize) len cuc rong de chua du cot
    fig, ax = plt.subplots(figsize=(28, 8)) 
    ax.axis('off')

    table = ax.table(
        cellText=df_show.values,
        colLabels=df_show.columns,
        cellLoc='center',
        loc='center'
    )

    table.auto_set_font_size(False)
    table.set_fontsize(8) 
    
    # Tu dong tinh toan do rong cot dua tren noi dung
    table.auto_set_column_width(col=list(range(len(df_show.columns))))
    table.scale(1.2, 2.5) 

    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"--- [OK] Da xuat anh bang du lieu: {path}")

# =========================
# 3. EXPORT PDF (FIXED COLUMN WIDTH & AUTO WRAP)
# =========================
def export_pdf(df, save_path):
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT

    # 1. Giam le trai/phai xuong muc toi thieu (10) de tranh bi mat chu o hai bien
    doc = SimpleDocTemplate(save_path, pagesize=landscape(A4), 
                            leftMargin=10, rightMargin=10, topMargin=20, bottomMargin=20)
    styles = getSampleStyleSheet()
    
    cell_body_style = ParagraphStyle(
        'cell_body',
        parent=styles['Normal'],
        fontSize=6,      # Giam nhe font size de cac cot hien thi du hon
        leading=7,
        alignment=TA_LEFT
    )
    
    cell_header_style = ParagraphStyle(
        'cell_header',
        parent=styles['Normal'],
        fontSize=6.5,
        fontName='Helvetica-Bold',
        textColor=colors.whitesmoke,
        alignment=TA_CENTER
    )

    content = []
    content.append(Paragraph("BAO CAO LAM SACH DU LIEU", styles["Title"]))
    content.append(Spacer(1, 15))
    content.append(Paragraph(f"Thoi gian thuc hien: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["Normal"]))
    content.append(Paragraph(f"So dong sau khi lam sach: {len(df)}", styles["Normal"]))
    content.append(Spacer(1, 20))

    # 2. CAN CHINH LAI DO RONG CAC COT (Tang cho bien, giam nhe o giua)
    total_width = 820 # Tang tong do rong hien thi
    columns = df.columns.tolist()
    col_widths = []

    for col in columns:
        c = col.lower()
        if 'product name' in c: col_widths.append(total_width * 0.18) # Giam nhe tu 0.22 xuong 0.18
        elif 'customer name' in c: col_widths.append(total_width * 0.10)
        elif 'id' in c: col_widths.append(total_width * 0.08)
        # Tang nhe cac cot so lieu o bien de khong bi mat chu
        elif any(x in c for x in ['sales', 'profit', 'quantity', 'year', 'month']): col_widths.append(total_width * 0.05) 
        else: col_widths.append(total_width * 0.06)

    table_data = []
    header_row = [Paragraph(str(col), cell_header_style) for col in columns]
    table_data.append(header_row)
    
    for row in df.head(10).values.tolist():
        data_row = [Paragraph(str(item), cell_body_style) for item in row]
        table_data.append(data_row)

    table = Table(table_data, colWidths=col_widths, repeatRows=1)
    
    table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#3498db")), 
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))

    content.append(table)
    doc.build(content)
    print(f"---  PDF da duoc luu : {save_path}")

# =========================
# 4. MAIN CLEANING LOGIC
# =========================
def clean_data(input_file, output_file):
    print("Bat dau quy trinh xu ly du lieu...")

    if not os.path.exists(input_file):
        print(f"Loi: Khong tim thay file {input_file}")
        return

    # Doc du lieu
    df = pd.read_csv(input_file, encoding='utf-8-sig')
    print(f"Du lieu ban dau: {df.shape[0]} dong, {df.shape[1]} cot")

    # Xu ly co ban
    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()
    df = df.dropna()

    # Ep kieu du lieu
    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    if "Sales" in df.columns:
        df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

    # Loc dong loi
    df = df.dropna(subset=["Order Date", "Sales"])
    df = df[df["Sales"] > 0]

    # Tao Feature
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month

    print(f"Sau khi lam sach: {df.shape[0]} dong")

    # Luu CSV
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False, encoding='utf-8-sig')

    # Xuat bao cao hinh anh va PDF
    img_dir = create_run_folder("images")
    report_dir = create_run_folder("reports")

    save_table_image(df, os.path.join(img_dir, "table.png"))
    export_pdf(df, os.path.join(report_dir, "clean_report.pdf"))

    print("\n" + "="*40)
    print("HOAN TAT THANH CONG")
    print(f"CSV Final: {output_file}")
    print(f"Anh bang: {img_dir}")
    print(f"Bao cao PDF: {report_dir}")
    print("="*40)

# =========================
# RUN ENGINE
# =========================
if __name__ == "__main__":
    clean_data(
        "data/superstore_cleaned.csv",
        "data/superstore_final.csv"
    )
