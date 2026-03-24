import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import json


history = None 
with open("patients_history.json", "r") as f:
    history = json.load(f)


# Create data frame for history patients
history_df = pd.DataFrame(history)

history_df["date"] = pd.date_range(end=pd.Timestamp.today(), periods=len(history_df))
history_df["date"] = history_df["date"].dt.strftime("%d %b %Y")

# Visualize the history patients
st.title("Patient History")
st.dataframe(history_df.drop(columns=["signals"]), hide_index=True)

col1, col2 = st.columns([1, 2])
with col1:
    selected_id = st.selectbox("Select Patient", history_df["id"])

with col2:
    selected_row = history_df[history_df["id"] == selected_id].iloc[0]
    
    fig = px.line(y=selected_row["signals"])
    st.plotly_chart(fig)
    
    st.write("Class:", selected_row["class"])
    st.write("Confidence:", selected_row["confidence"])
