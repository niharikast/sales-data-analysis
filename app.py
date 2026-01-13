import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Total Sales'] = df['Units Sold'] * df['Unit Price']

st.title("Sales Data Analysis")

# Sidebar filters
product = st.sidebar.selectbox("Select Product", df['Product'].unique())
region = st.sidebar.selectbox("Select Region", df['Region'].unique())

filtered_df = df[(df['Product']==product) & (df['Region']==region)]

st.write(f"Showing sales for {product} in {region} region")
st.dataframe(filtered_df)

# Plot total sales over time
sales_over_time = filtered_df.groupby('Date')['Total Sales'].sum().reset_index()
st.line_chart(sales_over_time.set_index('Date'))
