import os

os.environ["KERAS_BACKEND"] = "torch"

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import yfinance as yf
from keras.models import load_model
from datetime import datetime
import streamlit as slt
from sklearn.preprocessing import MinMaxScaler

end = datetime.now().date()
start = datetime(end.year - 8, end.month, end.day)

slt.title("Strong Market Trend Prediction")

user_input = slt.text_input("Enter the Stock to predict", 'AAPL').upper()
df = yf.download(user_input, start, end)

slt.subheader(f"Data from {start.year} to {end.year}")
slt.write(df.describe())

slt.subheader("Closing price chart")
fig = plt.figure(figsize=(12, 6))
plt.plot(df.Close, color='#1a5d94')
slt.pyplot(fig)

slt.title("Close price vs Moving Average 100 days")
ma100 = df.Close.rolling(window=100).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(df.Close, color='#1a5d94')
plt.plot(ma100, color='#ffaf00')
slt.pyplot(fig)

slt.title("Close price vs Moving Average 100 and 200 days")
ma200 = df.Close.rolling(window=200).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(df.Close, color='#1a5d94')
plt.plot(ma100, color='#ffaf00')
plt.plot(ma200, color='#142143')
slt.pyplot(fig)

data_training = pd.DataFrame(df['Close'][0: int(len(df) * 0.80)])
data_testing = pd.DataFrame(df['Close'][int(len(df) * 0.80): int(len(df))])

scaler = MinMaxScaler(feature_range=(0, 1))

data_training_array_scale = scaler.fit_transform(data_training)

model = load_model('model/keras_stock_predictor_model.h5')

past_100_days = data_training.tail(100)
final_data = pd.concat([past_100_days, data_testing], ignore_index=True)

input_data = scaler.fit_transform(final_data)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)

y_predict = model.predict(x_test)

close_data = df[['Close']].values
scale_data = scaler.fit_transform(close_data)
scaler = scaler.scale_

scale_factor = 1 / scaler[0]
y_predict = y_predict * scale_factor
y_test = y_test * scale_factor

slt.title("Actual Price vs Predicted Price")
fig = plt.figure(figsize=(12, 6))
plt.plot(y_test, color='#1a5d94', label='Original price')
plt.plot(y_predict, color='#ffaf00', label='Predicted price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
slt.pyplot(fig)