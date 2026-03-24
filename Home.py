import streamlit as st

# Page config
st.set_page_config(page_title="BrainLens", layout="wide")

# Custom CSS (fonts + styling)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Inter:wght@300;400;500&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .title {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        font-size: 60px;
        color: #4A90E2;
        margin-top: 20px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #666;
        margin-bottom: 40px;
    }

    .section {
        background-color: #f9f9f9;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">BrainLens</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered EEG Signal Analysis Platform</div>', unsafe_allow_html=True)

# Sections
st.markdown("""
<div class="section">

### Overview  
BrainLens is an intelligent platform designed to analyze EEG (brain signals) using machine learning techniques.  
It helps clinicians and researchers interpret neural data faster and with higher accuracy.

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">

### Key Features  
-  Interactive EEG signal visualization  
-  Automated classification using AI models  
-  Confidence scoring for predictions  
-  Patient history tracking  
-  Detailed case exploration  

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">

### How It Works  
1. Upload or input an EEG signal  
2. The system preprocesses and analyzes the data  
3. A prediction is generated with a confidence score  
4. The case is stored for future reference  

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">

### Purpose  
- Accelerate EEG analysis workflows  
- Support clinical decision-making  
- Provide an intuitive interface for brain signal exploration  

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">

⚠️ *This platform is intended for research and educational purposes only and does not replace professional medical diagnosis.*

</div>
""", unsafe_allow_html=True)