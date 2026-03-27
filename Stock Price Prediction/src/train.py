import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from features import load_data

print("Loading data...")

data = load_data()

print("Data loaded successfully")

features = ["Open","High","Low","Volume","MA10","MA50","RSI"]

X = data[features]

y = data["Close"]

x_train,x_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2
)

# Linear Regression
lr = LinearRegression()
lr.fit(x_train,y_train)

lr_pred = lr.predict(x_test)

lr_r2 = r2_score(y_test,lr_pred)

print("Linear Regression R2:",lr_r2)

# Random Forest
rf = RandomForestRegressor()
rf.fit(x_train,y_train)

rf_pred = rf.predict(x_test)

rf_r2 = r2_score(y_test,rf_pred)

print("Random Forest R2:",rf_r2)

# Save best model
joblib.dump(rf,"../models/stock_model.pkl")

print("Model training completed")