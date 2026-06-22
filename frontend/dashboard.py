import streamlit as st
import pandas as pd
import plotly.express as px
from backend.smart_analytics import smart_insights

def dashboard():

    st.title("📊 MQL Insights Dashboard")

    file = st.file_uploader("Upload Excel File", type=["xlsx"])

    if file:

        df = pd.read_excel(file)
        df.columns = df.columns.str.strip()

        field = st.selectbox("Select Field", df.columns)

        if field:

            data = df[field].fillna("Blank").value_counts().reset_index()
            data.columns = [field, "MQLs"]

            fig = px.bar(data, x="MQLs", y=field, orientation="h", text="MQLs")
            fig.update_traces(textposition="outside")

            st.plotly_chart(fig, use_container_width=True)

            # 🔥 STORE EVERYTHING (IMPORTANT FIX)
            st.session_state["df"] = df
            st.session_state["field"] = field
            st.session_state["insights"] = smart_insights(df, field)

            st.subheader("🧠 Insights")
            for i in st.session_state["insights"]:
                st.write("✔", i)

            # 🔥 BUTTON ONLY TRIGGERS ACTION
            if st.button("📄 Generate PDF Report"):
                st.switch_page("pages/report.py")