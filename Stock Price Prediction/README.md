# 📈 Stock Price Prediction using Machine Learning & LSTM

An end-to-end **Machine Learning + Deep Learning project** that predicts stock prices using real-time financial data.
This project combines **traditional ML models (Linear Regression, Random Forest)** with **LSTM neural networks** and an **interactive Streamlit web app**.

---

## 🚀 Features

* 📊 Fetches real-time stock data using Yahoo Finance API
* 🤖 Implements Machine Learning models:

  * Linear Regression
  * Random Forest Regressor
* 🧠 Implements Deep Learning model:

  * LSTM (Long Short-Term Memory)
* 📈 Feature Engineering:

  * Moving Averages (MA10, MA50)
  * Relative Strength Index (RSI)
* 🔮 Predicts stock closing prices
* 🌐 Interactive UI built using Streamlit

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Deep Learning:** TensorFlow / Keras
* **Visualization/UI:** Streamlit
* **Data Source:** yFinance API

---

## 📸 Screenshots

### 🖥️ Web App Interface

![App UI](screenshots/app.png)

### 🤖 Model Training Output

![Training Output](screenshots/train.png)

### 🧠 LSTM Training

![LSTM Output](screenshots/lstm.png)

---

## 📂 Project Structure

```
stock-price-prediction/
│
├── src/
│   ├── train.py          # Train ML models
│   ├── predict.py        # Make predictions
│   ├── lstm_model.py     # LSTM deep learning model
│   ├── features.py       # Data loading & feature engineering
│
├── models/
│   └── stock_model.pkl   # Saved ML model
│
├── screenshots/
│   ├── app.png
│   ├── train.png
│   ├── lstm.png
│
├── app.py                # Streamlit web app
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 Train Machine Learning Models

```bash
python src/train.py
```

---

### 🔹 Run Prediction Script

```bash
python src/predict.py
```

---

### 🔹 Train LSTM Model

```bash
python src/lstm_model.py
```

---

### 🔹 Launch Web Application

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 📊 Results

* 📈 Linear Regression R² Score: **~0.9998**
* 🌳 Random Forest R² Score: **~0.9997**
* 🧠 LSTM trained on historical stock sequences

---

## ⚠️ Important Note

* Very high R² values indicate potential **overfitting**
* This occurs because models predict **same-day prices**
* More realistic approach: predict **future values using shifted targets**

---

## 🚀 Future Improvements

* 📊 Add interactive stock charts
* 🌐 Deploy app using Streamlit Cloud
* 🔄 Predict future prices (multi-step forecasting)
* 📉 Improve LSTM performance
* 📊 Add multiple stock comparison

---

## 💡 Key Learnings

* End-to-end ML pipeline development
* Feature engineering for time-series data
* Deep learning with LSTM
* Model evaluation using R² score
* Building ML-powered web applications

---

## 👩‍💻 Author

**Anshika Singh**
B.Tech IT Student | Aspiring ML Engineer

---

## ⭐ Support

If you found this project useful:

👉 Star this repository
👉 Share with others

---
