# ⚡ Germany Load Forecasting Dashboard

An interactive dashboard built with **Streamlit**, **XGBoost**, and **Plotly** to forecast Germany’s electricity load over the next 7 days.

### 📊 Data Source
The load data used in this project is sourced from the [Open Power System Data (OPSD)](https://data.open-power-system-data.org/time_series/) platform.

> License: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

Citation:
Open Power System Data. (2020). Time series. https://data.open-power-system-data.org/time_series/


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
