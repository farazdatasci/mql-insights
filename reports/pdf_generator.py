from fpdf import FPDF
import matplotlib.pyplot as plt
import os

def create_graph_image(df, field):

    data = df[field].value_counts().head(10)

    plt.figure(figsize=(8, 4))
    data.plot(kind="barh", color="steelblue")

    plt.title(f"MQLs by {field}")
    plt.xlabel("Count")
    plt.tight_layout()

    img_path = "temp_chart.png"
    plt.savefig(img_path, dpi=300)
    plt.close()

    return img_path


def create_pdf(df, field, insights):

    pdf = FPDF()
    pdf.add_page()

    # TITLE
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="MQL INSIGHTS REPORT", ln=True, align="C")

    pdf.ln(5)

    # KPI SECTION
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Analysis Field: {field}", ln=True)

    pdf.ln(5)

    # INSIGHTS SECTION
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="SMART INSIGHTS:", ln=True)

    pdf.set_font("Arial", size=11)

    for i in insights:
        pdf.cell(200, 8, txt=f"- {i}", ln=True)

    pdf.ln(5)

    # GRAPH IMAGE
    img_path = create_graph_image(df, field)

    pdf.image(img_path, x=10, w=180)

    # SAVE PDF
    output_path = "MQL_Report.pdf"
    pdf.output(output_path)

    # CLEAN TEMP IMAGE
    os.remove(img_path)

    return output_path