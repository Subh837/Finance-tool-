import streamlit as st
import math
import pandas as pd
import numpy as np

# ========== PAGE CONFIG ==========
st.set_page_config(page_title="Finance Report", layout="wide")

# ========== TITLE ==========
st.title("📊 Finance Report Dashboard")

# ========== HEADER ==========
st.header("Financial Data Analysis")

# ========== 1. SIDEBAR INPUTS ==========
st.sidebar.header("User Inputs")

name = st.sidebar.text_input("Enter your name:", "User")
amount = st.sidebar.number_input("Enter amount (₹):", min_value=0, value=10000)
rate = st.sidebar.slider("Interest Rate (%):", 1, 20, 10)
years = st.sidebar.slider("Years:", 1, 30, 5)

# ========== 2. MAIN CONTENT ==========
st.subheader(f"Hello {name} 👋")

# ========== 3. PI VALUE ==========
st.subheader("3. PI Value")
st.write(f"🔢 PI = {math.pi}")

# ========== 4. SIMPLE INTEREST CALCULATION ==========
st.subheader("4. Simple Interest Calculation")

simple_interest = (amount * rate * years) / 100
total_amount = amount + simple_interest

col1, col2, col3 = st.columns(3)
col1.metric("💰 Principal", f"₹{amount:,.0f}")
col2.metric("📈 Interest", f"₹{simple_interest:,.0f}")
col3.metric("💵 Total", f"₹{total_amount:,.0f}")

# ========== 5. COMPOUND INTEREST ==========
st.subheader("5. Compound Interest Growth")

compound_interest = amount * ((1 + rate/100) ** years) - amount
total_compound = amount + compound_interest

st.write(f"**Compound Interest:** ₹{compound_interest:,.0f}")
st.write(f"**Total with Compound:** ₹{total_compound:,.0f}")

# ========== 6. TABLE ==========
st.subheader("6. Year-wise Breakdown")

data = []
for y in range(1, years + 1):
    ci = amount * ((1 + rate/100) ** y) - amount
    total = amount + ci
    data.append({"Year": y, "Interest": f"₹{ci:,.0f}", "Total": f"₹{total:,.0f}"})

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# ========== 7. CHART ==========
st.subheader("7. Growth Chart")

growth_data = []
for y in range(years + 1):
    total = amount * ((1 + rate/100) ** y)
    growth_data.append({"Year": y, "Total Amount": total})

df_chart = pd.DataFrame(growth_data)
st.line_chart(df_chart.set_index("Year"))

# ========== 8. FOOTER ==========
st.markdown("---")
st.caption(f"📅 Report generated for {name} | Rate: {rate}% | Years: {years}")
