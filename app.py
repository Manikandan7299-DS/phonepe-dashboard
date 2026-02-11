import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

st.set_page_config(layout="wide")

st.title("PhonePe Analytics Dashboard")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mani123",
    database="phonepe"
)

transactions = pd.read_sql("SELECT * FROM transactions", conn)
users = pd.read_sql("SELECT * FROM users", conn)
insurance = pd.read_sql("SELECT * FROM insurance", conn)

conn.close()

tab1, tab2, tab3 = st.tabs(["Transactions", "Users", "Insurance"])

with tab1:
    st.header("Transactions")
    fig = px.bar(transactions, x="state", y="amount")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Users")
    fig = px.bar(users, x="state", y="count")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Insurance")
    fig = px.bar(insurance, x="state", y="total_insurance")
    st.plotly_chart(fig, use_container_width=True)