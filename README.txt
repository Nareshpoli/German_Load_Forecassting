# ⚡ Germany Load Forecasting Dashboard

An interactive dashboard built with **Streamlit**, **XGBoost**, and **Plotly** to forecast Germany’s electricity load over the next 7 days.

## Features

- 📈 Visualizes historical load
- 🔮 Predicts next 7-day hourly load
- 🧠 ML model: XGBoost Regressor

## 🔁 Versions

- `germany_load_forecasting_dashboard.py` — Base version( No 7 day hourly load forecast)
- `germany_load_forecasting_dashboard_V2.py` — Uses improved feature handling and forecast structure
- `germany_load_forecasting_dashboard_V3.py` - addition of sidebar and menu items in streamlit.

🚀 [Click here to try the Live Demo](https://germanloadforecassting-duu7obpqmsfvk4feehuxs9.streamlit.app/)

## How to Run

```bash
pip install -r requirements.txt
streamlit run germany_load_forecasting_dashboard.py
