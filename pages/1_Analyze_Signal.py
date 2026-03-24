import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import joblib 
from pathlib import Path

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
            
            # displat both class and confidence
            st.write("Prediction Result:")
            st.write(f"Class: 2 with confidence: {probs*100:.2f}%")
            st.write(f"Class: 3 with confidence: {(1-probs)*100:.2f}%")
            #st.write("Class: ", int(cls))
            #st.write("Confidence: ", f"{probs*100:.2f}%")

    #Robustness Insights, if more than 250 outliers are detected (above 2 std of training data), then the signal is considered to have high abnormal activity,
    # So we report to the user that abonarmality and that maybe the prediction is not reliable.
    
    base_dir = Path(__file__).resolve().parents[1]
    train_path = base_dir / "train.csv"
    ref_df = pd.read_csv(train_path)
    ref_df = ref_df.drop(columns=[c for c in ref_df.columns if str(c).lower() in ["y", "label", "class", "unnamed: 0"]], errors="ignore")

    # Per-feature mean and std from training data
    ref_means = ref_df.mean(axis=0).to_numpy()
    ref_stds = ref_df.std(axis=0, ddof=0).to_numpy()

    signal_vals = signal.flatten()[:len(ref_means)]
    signal_z = (signal_vals - ref_means) / (ref_stds + 1e-12)

    outlier_count = int(np.sum(np.abs(signal_z) > 2))
    if outlier_count > 250:
        st.warning(f"High abnormal activity detected: {outlier_count} features are outliers vs training data. Prediction may not be reliable.")


    # To b implementd
    
    #"High abnormal activity detected"
    #"Possible seizure pattern" 
    # n_rows = st.slider("Choose number of Rows to display",
                    #    min_value=5, max_value=len(df), step=1)
    # columns_to_show = st.multiselect("Select Columns", df.columns, default=list(df.columns))
    # st.write(df[: n_rows][columns_to_show])
    # signal = df[list(columns_to_show)].iloc[4]
