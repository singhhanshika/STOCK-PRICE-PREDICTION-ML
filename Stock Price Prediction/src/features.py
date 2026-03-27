import yfinance as yf
import pandas as pd

def load_data(symbol="AAPL"):

    print("Downloading stock data...")

    data = yf.download(symbol, start="2015-01-01")

    # Feature Engineering
    data["MA10"] = data["Close"].rolling(window=10).mean()
    data["MA50"] = data["Close"].rolling(window=50).mean()

    data["RSI"] = 100 - (100 / (1 + data["Close"].pct_change(fill_method=None).rolling(14).mean()))

    data = data.dropna()

    print("Data ready")

    return data