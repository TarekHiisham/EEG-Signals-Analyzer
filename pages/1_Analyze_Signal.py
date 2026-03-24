import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import joblib 

file = st.file_uploader("Upload Signal Records", type=["csv", "xsxl"])
std_scaler = StandardScaler()
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

# @st.cache_resource to cash machine learning models
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

model = load_model()
if file is not None:
    # Load signal records and transform to numpy array
    signal = load_data(file).values

    # Standarize the signal
    signal_std = std_scaler.fit_transform(signal.reshape(-1, 1))

    # Flatten the signal into 1D vector
    signal_std = signal_std.flatten()

    # Plot the Signal 
    figure = px.line(y=signal_std, title='Signal Standarized')
    st.plotly_chart(figure)

    # Analyze The Signal
    button = st.button("Analyze")
    if button:
        with st.spinner("In progress..."):
            prediction = model.predict(signal_std.reshape(1, -1))
            cls = prediction.squeeze()
            cls_idx = list(model.classes_).index(cls)

            probs = model.predict_proba(signal_std.reshape(1, -1))[:, cls_idx].squeeze()
            
            st.write("Class: ", int(cls))
            st.write("Confidence: ", f"{probs*100:.2f}%")

    # To b implementd
    #AI Insights:
    #"High abnormal activity detected"
    #"Possible seizure pattern" 
    # n_rows = st.slider("Choose number of Rows to display",
                    #    min_value=5, max_value=len(df), step=1)
    # columns_to_show = st.multiselect("Select Columns", df.columns, default=list(df.columns))
    # st.write(df[: n_rows][columns_to_show])
    # signal = df[list(columns_to_show)].iloc[4]
