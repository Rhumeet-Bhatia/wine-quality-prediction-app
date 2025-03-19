# 🍷 Wine Quality Prediction

## 🚀 Overview
A **Machine Learning Web App** that predicts **wine quality** based on its chemical properties. Built with **Flask API** for model inference and **Streamlit UI** for seamless interaction.

## 📌 Features
- **End-to-End ML Pipeline** – Data preprocessing, feature selection, model training & evaluation.
- **Flask API** – Handles real-time predictions via JSON requests.
- **Streamlit UI** – User-friendly web interface for input & results.
- **Automated Data Processing** – Handles missing values, encoding, and scaling.
- **Model Training & Persistence** – Uses **Linear Regression**, saves trained model for future use.

## 🛠️ Tech Stack
- **Backend:** Flask (API)
- **Frontend:** Streamlit (UI)
- **Machine Learning:** Scikit-learn (Linear Regression)
- **Data Processing:** Pandas, NumPy, Statsmodels
- **Performance Metrics:** MAE, MSE, RMSE, R² Score

## 📂 Project Structure
- `api.py`: Flask API for predictions
- `app.py`: Streamlit UI
- `data_preprocess.py`: Data cleaning & transformation
- `feature_engg.py`: Feature selection & correlation analysis
- `model.py`: Model training & saving
- `main.py`: Runs the ML pipeline
- `README.md`: Project documentation



## 📡 API Usage

### 🎯 Endpoint: `/predict`
- **Method:** POST
- **Request (JSON):**
json{"features": [5.1, 3.5, 1.4, 0.2, 10, 15, 1, 23, 1]}

- **Response:**
json
{
  "prediction": [4.24]
}


## 📜 **License**  
This project is open-source under the MIT License.



### ⭐ **Star this Repository** if you found it useful! 🚀