import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Sample data generator
def sample_data(periods=200, start_price=1.30):
    idx = pd.date_range(end=datetime.utcnow(), periods=periods, freq="60min")
    np.random.seed(42)
    returns = np.random.normal(0, 0.001, len(idx))
    price = start_price + np.cumsum(returns)
    openp = price
    closep = price + np.random.normal(0, 0.0003, len(idx))
    highp = np.maximum(openp, closep) + np.abs(np.random.normal(0, 0.0005, len(idx)))
    lowp = np.minimum(openp, closep) - np.abs(np.random.normal(0, 0.0005, len(idx)))
    return pd.DataFrame({'Open': openp, 'High': highp, 'Low': lowp, 'Close': closep}, index=idx)

# Run Streamlit app
def run_app():
    st.title("🦄 Keyinpay Unicorn Strategy Bot")
    df = sample_data()
    st.line_chart(df['Close'])
    st.success("Bot is running successfully!")

if __name__ == "__main__":
    run_app()
