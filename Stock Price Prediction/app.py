import streamlit as st
import joblib
from src.features import load_data

st.title("📈 Stock Price Prediction App")

st.write("Enter a stock symbol (Example: AAPL, TSLA, MSFT)")

# Load model
try:
    model = joblib.load("models/stock_model.pkl")
except:
    st.error("Model not found. Please run train.py first.")
    st.stop()

# Input
symbol = st.text_input("Stock Symbol", "AAPL")

if st.button("Predict"):

    st.write("Fetching data...")

    data = load_data(symbol)

    features = ["Open","High","Low","Volume","MA10","MA50","RSI"]

    latest = data[features].tail(1)

    prediction = model.predict(latest)

    st.success("Prediction Complete ✅")

    st.subheader("Predicted Closing Price:")
    st.write(prediction[0])