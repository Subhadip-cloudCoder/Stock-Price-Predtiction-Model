# 📈 Deep Learning Stock Trend Predictor

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B.svg?logo=streamlit&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Deep_Learning-D00000.svg?logo=keras&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-Backend-EE4C2C.svg?logo=pytorch&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg?logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Preprocessing-orange.svg?logo=scikit-learn&logoColor=white)

## 📌 What is this Project?
Stock market forecasting is the process of attempting to determine the future trajectory of a company stock or financial instrument based on historical data. The primary challenge in this domain is **extreme volatility and random walk behavior**—past prices do not always cleanly dictate future movements, and chaotic market shocks are difficult to anticipate. 

This project is an end-to-end Deep Learning pipeline and interactive web dashboard designed to tackle this exact problem. It utilizes live data extraction, sliding-window sequence engineering, and a Long Short-Term Memory (LSTM) neural network to evaluate how deep learning models behave when analyzing complex financial time-series data.

### The Data Challenge
Financial data is notoriously noisy. To make accurate predictions, models must be trained to recognize broader historical trends rather than overfitting to erratic, daily price spikes.

![Original Closing Price](images/Closing%20price%20chart.png)

---

## 🛠️ Tech Stack & Tools Used
* **Programming Language:** Python
* **Web Framework & UI:** Streamlit
* **Data Extraction & API:** Yahoo Finance (`yfinance`)
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Data Visualization:** Matplotlib
* **Deep Learning Engine:** Keras (Configured with a lightweight PyTorch backend)
* **Data Scaling & Preprocessing:** Scikit-Learn (`MinMaxScaler`)

### Applying Technical Indicators (Moving Averages)
To allow the algorithm and the end-user to understand macro-trends, 100-day and 200-day Moving Averages were mathematically calculated and overlaid onto the dataset to establish dynamic support and resistance baselines.

![Closing Price vs MA 100 & 200](images/closing%20price%20vs%20ma%20100%20vs%20ma%20200%20chart.png)

---

## 🧠 Deep Learning Architecture & Engineering
To deeply analyze the sequential nature of the stock market, I deployed a specialized neural network architecture requiring strict data engineering:

1. **MinMax Scaling:** Stock prices vary wildly. The data was mathematically normalized to a strict `0` to `1` range to ensure computational stability within the neural network.
2. **3D Sequence Formatting (Sliding Window):** Neural networks cannot read plain flat tables for time-series forecasting. The data was re-engineered into 100-day chronological batches, allowing the model to "remember" the momentum of the past 100 days before attempting to predict the 101st day.
3. **Keras LSTM Network:** A specialized Recurrent Neural Network (RNN) equipped with internal memory gates, designed specifically to solve the vanishing gradient problem in long-term sequential data.

---

## 📊 Evaluation Criteria & Model Judgment
In financial forecasting, standard "Accuracy" is a deceptive metric. Therefore, this model was evaluated based on the following:
* **Root Mean Squared Error (RMSE):** Measuring the standard deviation of the prediction errors.
* **Macro-Trend Alignment:** How accurately the model captures the overall trajectory and turning points of the asset over an 8-year period.

### Comparative Analysis: The "LSTM Lag" Reality Check
Rather than claiming the model perfectly predicts the future, this project documents the mathematical reality of LSTMs on stock data. As visualized in the dashboard, the model successfully learns the overall trend and keeps predictions in a tight, accurate range. However, it exhibits the classic **"LSTM Lag"**—optimizing its error rate by acting as an advanced smoothing function rather than anticipating sudden, chaotic market crashes before they happen.

![Actual vs Predicted Price](images/original%20price%20vs%20predicted%20price%20chart.png)

---

## 🚀 Installation & Usage
Want to run this prediction model on your local machine?

**1. Clone the repository & enter the directory:**
```bash
git clone https://github.com/Subhadip-cloudCoder/Stock-Price-Predtiction-Model.git
cd Stock-Price-Predictioin-Model
```

**2. Install the required dependencies:**
```bash
pip install -r requirements.txt
```

**1. Launch the Streamlit Web App:**
```bash
streamlit run app.py
```

Once launched, simply type any valid stock ticker (e.g., AAPL, TSLA, RELIANCE.NS) into the dashboard and press enter to dynamically generate the Deep Learning predictions!

---

## 💡 Conclusion
Forecasting financial markets requires a delicate intersection of rigorous data engineering and deep learning architecture. This project successfully demonstrates that deploying an LSTM neural network can accurately track complex, long-term market trajectories. By building a dynamic, full-stack pipeline with Streamlit, we can objectively observe how artificial intelligence processes sequential momentum, providing a highly professional foundation for algorithmic trading analysis.

---

## 📬 Let's Connect!

I enjoy discussing Data Science, Machine Learning, and innovative tech projects. Whether you have a question about this model, some feedback, or just want to connect, feel free to reach out!

<br>

**Subhadip Biswas**

[![Email](https://img.shields.io/badge/Email-subhadip2622%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:subhadip2622@gmail.com)

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Subhadip-cloudCoder)

[![X (Twitter)](https://img.shields.io/badge/X-Profile-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/subhadipcodes?s=11)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/subhadip-biswas-ba0a5a419)

<br>

<p align="center">

  <b>⭐️ If you found this project helpful or interesting, please consider giving it a star! ⭐️</b>

</p>
