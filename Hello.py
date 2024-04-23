## main library for the data apps

import streamlit as st 

## work on stock data 
import yfinance as yf

## for data handling
import pandas as pd 

## for visualisation
from matplotlib import pyplot as plt 


st.title("My financial dashboard")
st.write("This dashboard is made to display some aggregated stats and price of a stock!")


st.subheader('Datetime slider')

from datetime import datetime

start_time = st.slider("When do you start",
     min_value=datetime(2020, 1, 1, 9, 30),
     max_value=datetime(2022, 1, 1, 9, 30),
     format="MM/DD/YYYY"
    )
st.write("Start time:", start_time)

## Let the user select the stock to display
stock_name = st.selectbox("Stock-Name", 
             ["GOOGL", "AAPL", "TSLA", "AMD"])

st.write(f"You selected {stock_name}!")

## (open, high, low, close, adj.close, volume)
df = yf.download(stock_name, start=start_time)
#st.write(df)

## show the min - max for each column
st.write(stock_name + " Min/Max values:")
summary_df = df.agg(["min", "max", "mean", "std"])
st.write(summary_df) ## detect this is a dataframe --> plot the interactive df

if st.button("Plot"):
    ## plot the open price 
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.plot(df["Open"], color="green", label="Open")
    ax.legend()
    st.pyplot(fig)