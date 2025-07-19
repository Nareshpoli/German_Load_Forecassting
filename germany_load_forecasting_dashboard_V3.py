#!/usr/bin/env python
# coding: utf-8

# In[20]:


import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import datetime
import numpy as np


# In[28]:


st.set_page_config(
    page_title=" Germany Load Forecast",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Report a bug": "https://github.com/yourusername/germany-load-forecasting/issues",
        "About": """
        ## ⚡ Germany Load Forecasting App
        Built with Streamlit and XGBoost.
        Provides hourly load forecasting for the next 7 days using historical trends.
        """
    }
)


# In[22]:


st.title("⚡ Germany Load Forecasting Dashboard")
st.write("Welcome! Use the sidebar and buttons to explore the forecasts.")


# In[29]:


with st.sidebar:
    st.title("🔧 Settings")
    st.markdown("Adjust options for load forecasting:")
    show_forecast = st.checkbox("Show 7-day forecast", value=True)
    st.markdown("---")
    st.write("**Author:** [Naresh Poli](https://github.com/Nareshpoli)")


# In[23]:


# Load the saved model and data
model = joblib.load("xgb_load_forecast_model.pkl")
data = pd.read_csv("test_predictions.csv", parse_dates=["Time"])
data["Time"] = pd.to_datetime(data["Time"])



# In[24]:


#Date Filter
st.subheader("Load Forecasting Results")
selected_date = st.date_input("Select a date to view:", value=data["Time"].dt.date.iloc[0])

# Filter selected day's data
filtered_df = data[data["Time"].dt.date == selected_date]


# In[25]:


# ------------------ Plot 1: Actual vs Predicted ------------------
fig = go.Figure()
fig.add_trace(go.Scatter(x=filtered_df["Time"], y=filtered_df["Actual_Load"], mode="lines+markers", name="Actual Load"))
fig.add_trace(go.Scatter(x=filtered_df["Time"], y=filtered_df["Predicted_Load"], mode="lines+markers", name="Predicted Load"))

fig.update_layout(
    title="Actual vs Predicted Load",
    xaxis_title="Time",
    yaxis_title="Load (MW)",
    legend_title="Legend",
    height=500)

st.plotly_chart(fig, use_container_width=True)


# In[26]:


# ------------------ MAE Metric ------------------
mae = (filtered_df["Actual_Load"] - filtered_df["Predicted_Load"]).abs().mean()
st.metric("MAE (Mean Absolute Error)", f"{mae:.2f} MW")


# In[30]:


# ------------------ Future Forecast ------------------

st.subheader("Future Load Forecast")
if st.button("Forecast for next 7 days"):
    st.write("Press the button to see the next 7 day forecast and make sure you enable the show forecast in sidebar")
    future_dates = pd.date_range(start=data["Time"].max() + pd.Timedelta(hours=1), periods=7*24, freq="H")
    
    
    
    future_features = pd.DataFrame({
        "hour": future_dates.hour,
        "day": future_dates.day,
        "weekday": future_dates.dayofweek,
        "month": future_dates.month,
        "lag_1h": 0,         # set all lag_1h to zero
        "lag_24h": 0         # set all lag_24h to zero
    })
    predictions = model.predict(future_features)
    future_df = pd.DataFrame({"Time": future_dates,"Predicted Load": predictions})
    
    if show_forecast:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=future_df["Time"], y=future_df["Predicted Load"], mode="lines+markers", name="Forecasted Load"))
        fig2.update_layout(title="Forecast for Next 7 Days",xaxis_title="Date",yaxis_title="Predicted Load (MW)",height=500)
        st.plotly_chart(fig2, use_container_width=True)
    


# In[ ]:





# In[ ]:





# In[ ]:




