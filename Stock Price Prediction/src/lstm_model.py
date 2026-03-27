import numpy as np
import yfinance as yf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

print("Downloading data...")

data = yf.download("AAPL",start="2015-01-01")

close = data["Close"].values.reshape(-1,1)

scaler = MinMaxScaler()

scaled = scaler.fit_transform(close)

X = []
y = []

for i in range(60,len(scaled)):
    X.append(scaled[i-60:i])
    y.append(scaled[i])

X = np.array(X)
y = np.array(y)

print("Building LSTM model...")

model = Sequential()

model.add(LSTM(50,return_sequences=True,input_shape=(X.shape[1],1)))
model.add(LSTM(50))
model.add(Dense(1))

model.compile(optimizer="adam",loss="mse")

print("Training LSTM...")

model.fit(X,y,epochs=3,batch_size=32)

print("LSTM Training Completed")