import streamlit as st
from reports.pdf_generator import create_pdf

st.title("📄 Report Page")

# CHECK DATA EXISTS
if "df" not in st.session_state:
    st.warning("No data found. Please upload file first.")
    st.stop()

df = st.session_state["df"]
field = st.session_state["field"]
insights = st.session_state["insights"]

# GENERATE PDF ONLY HERE
pdf_path = create_pdf(df, field, insights)

with open(pdf_path, "rb") as f:
    st.download_button(
        label="⬇ Download PDF Report",
        data=f,
        file_name="MQL_Report.pdf",
        mime="application/pdf"
    )