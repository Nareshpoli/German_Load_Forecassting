#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model and data
model = joblib.load("xgb_load_forecast_model.pkl")
data = pd.read_csv("test_predictions.csv", parse_dates=["Time"])

# Streamlit App
st.title("Germany Load Forecasting Dashboard")
st.markdown("This dashboard visualizes predicted vs actual electricity load using an XGBoost model.")

# Plot section
st.subheader("Load Forecasting Results")
selected_date = st.date_input("Select a date to view:", value=data["Time"].dt.date.iloc[0])

# Filter data
day_data = data[data["Time"].dt.date == selected_date]

# Plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(day_data["Time"], day_data["Actual_Load"], label="Actual", marker='o')
ax.plot(day_data["Time"], day_data["Predicted_Load"], label="Predicted", marker='x')
ax.set_title(f"Load Forecasting for {selected_date}")
ax.set_ylabel("Load (MW)")
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

# Metrics
mae = (day_data["Actual_Load"] - day_data["Predicted_Load"]).abs().mean()
st.metric("MAE (Mean Absolute Error)", f"{mae:.2f} MW")


# In[ ]:





# In[ ]:





# In[ ]:




