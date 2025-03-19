'''Explanation:
Sending Data to Flask API

python
Copy
Edit
response = requests.post("http://127.0.0.1:5000/predict", json={"features": features})
This line sends a POST request to the Flask API endpoint (/predict).
The features (a list of input values) are sent as JSON data.
Flask receives this JSON, processes the request, and returns a prediction.
Displaying Prediction in Streamlit

python
Copy
Edit
st.write("Prediction:", response.json()["prediction"])
This extracts the prediction from the API response.
Displays it in the Streamlit app using st.write().
How It Works?
When the user inputs feature values in the UI and clicks submit, the Streamlit app:
Sends the data to the Flask model.
Waits for the API to return a response.
Displays the predicted output in the UI.
✅ Make sure the Flask API is running before testing!'''


import subprocess

# Start Flask API in the background
subprocess.Popen(["python", "api.py"])
import streamlit as st
import requests
import time
import pandas as pd

# Set Page Configuration
st.set_page_config(page_title="🍷 Wine Quality Predictor", layout="wide")

# Navigation State
if "page" not in st.session_state:
    st.session_state.page = "home"

# Custom CSS Styling
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #1f1c2c, #928DAB);
            font-family: 'Arial', sans-serif;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #FF4B4B;
            text-shadow: 3px 3px 12px rgba(255,75,75,0.6);
            margin-bottom: 15px;
        }
        .subtitle {
            font-size: 22px;
            text-align: center;
            color: #DDDDDD;
            margin-bottom: 30px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #FF4B4B, #ff7878);
            color: white;
            border: none;
            border-radius: 20px;
            padding: 16px 32px;
            font-size: 22px;
            font-weight: bold;
            transition: 0.4s ease-in-out;
            box-shadow: 0px 6px 20px rgba(255,75,75,0.8);
            cursor: pointer;
        }
        .stButton>button:hover {
            transform: scale(1.1);
            background: linear-gradient(90deg, #ff7878, #FF4B4B);
        }
        .result {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            color: #4CAF50;
            padding: 20px;
            border-radius: 15px;
            background: rgba(76, 175, 80, 0.2);
            box-shadow: 0px 0px 20px rgba(76, 175, 80, 0.6);
            text-shadow: 2px 2px 12px rgba(76, 175, 80, 0.8);
            margin-top: 25px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='color:#FF4B4B; text-align:center;'>🔍 About</h2>", unsafe_allow_html=True)
    st.write("This AI-powered app predicts wine quality based on its chemical properties. Enter values and click 'Predict' to get results.")
    if st.session_state.page != "home":
        if st.button("🏠 Back to Home"):
            st.session_state.page = "home"
            st.rerun()

# Home Page
if st.session_state.page == "home":
    st.markdown("<h1 class='title'>🍷 Wine Quality Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>Choose an option to proceed:</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Predict from Features"):
            st.session_state.page = "features"
            st.rerun()
    with col2:
        if st.button("📂 Predict from File"):
            st.session_state.page = "file"
            st.rerun()

# Features Prediction Page
elif st.session_state.page == "features":
    st.markdown("<h4 style='color: #FF4B4B;'>📌 Enter Wine Features:</h4>", unsafe_allow_html=True)
    features = [st.number_input(f"Feature {i+1}", key=i) for i in range(9)]
    if st.button("✨ Predict Now"):
        with st.spinner("⏳ Analyzing the wine quality..."):
            time.sleep(2)
            response = requests.post("http://127.0.0.1:5000/predict", json={"features": features})
            predicted_quality = response.json()["prediction"][0]
        st.markdown(f"<div class='result'>✅ Predicted Wine Quality: <strong>{predicted_quality}</strong></div>", unsafe_allow_html=True)

# File Upload Prediction Page
elif st.session_state.page == "file":
    st.markdown("<h4 style='color: #FF4B4B;'>📂 Upload CSV File for Batch Prediction:</h4>", unsafe_allow_html=True)
    file = st.file_uploader("Upload a CSV file containing wine features", type=["csv"])
    if file is not None:
        if st.button("📊 Predict from File"):
            with st.spinner("⏳ Processing file predictions..."):
                time.sleep(2)
                response = requests.post("http://127.0.0.1:5000/predict_file", files={"file": file})
                predictions = response.text
            st.markdown(f"<div class='result'>✅ Predicted Wine Quality for Uploaded File:<br>{predictions}</div>", unsafe_allow_html=True)