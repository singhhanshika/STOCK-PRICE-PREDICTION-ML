import joblib
from features import load_data

print("Loading model...")

model = joblib.load("../models/stock_model.pkl")

data = load_data()

features = ["Open","High","Low","Volume","MA10","MA50","RSI"]

latest = data[features].tail(1)

prediction = model.predict(latest)

print("Predicted next closing price:")
print(prediction)