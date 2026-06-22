import streamlit as st
from auth.login import login_page
from frontend.dashboard import dashboard

st.set_page_config(page_title="MQL Insights", layout="wide")

if "user" not in st.session_state:
    login_page()
else:
    dashboard()