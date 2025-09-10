# 🌱 ProGro – Crop & Fertilizer Recommendation System

ProGro is a web-based system that helps farmers make better agricultural decisions by predicting the most suitable **crops** and recommending the best **fertilizers**.  
The system is built using **Logistic Regression models** trained on agricultural datasets and presented through a web interface with multiple HTML templates.

---

## 📂 Project Structure

main.py # Application entry point
crop.ipynb # Jupyter Notebook – Crop prediction model training
fertilizer.ipynb # Jupyter Notebook – Fertilizer recommendation model training
crop.csv # Dataset for crop prediction
Fertilizer Prediction.csv# Dataset for fertilizer recommendation
crop.pkl # Trained model for crop prediction
fert.pkl # Trained model for fertilizer recommendation
vect.pkl # Vectorizer for fertilizer features
requirements.txt # Project dependencies
templates/ # HTML templates for user interface


---

## 📖 Project Summary

### 🌾 Crop Prediction
- **Goal:** Suggest the best crop to grow under specific environmental and soil conditions.  
- **Dataset:** `crop.csv`  
- **Algorithm:** Logistic Regression  
- **Inputs:** Soil nutrients (N, P, K), temperature, humidity, pH, rainfall  
- **Output:** Recommended crop name  
- **Model File:** `crop.pkl`  

### 🧪 Fertilizer Recommendation
- **Goal:** Recommend the most appropriate fertilizer for a given crop and soil condition.  
- **Dataset:** `Fertilizer Prediction.csv`  
- **Algorithm:** Logistic Regression  
- **Inputs:** Crop type, soil health, nutrient values  
- **Output:** Fertilizer type (e.g., Urea, DAP, NPK, etc.)  
- **Model Files:** `fert.pkl`, `vect.pkl`  

---

## 🖥️ Features

- Data-driven decision support for farmers  
- Crop recommendation based on soil and climate conditions  
- Fertilizer suggestion to improve crop yield  
- Multiple pre-built web templates for user interaction (`home.html`, `fertilizer.html`, `result.html`)  
- Logistic Regression models for transparent, interpretable predictions  

---

## 🛠️ Tech Stack

- **Python 3.9+**  
- **Flask** (web framework)  
- **Pandas, NumPy** (data processing)  
- **Scikit-learn** (Logistic Regression models)  
- **Matplotlib, Seaborn** (visualizations during training)  
- **Pickle / Joblib** (model persistence)  
- **HTML, CSS, JS** (frontend templates)  

---

## 📜 License

This project is licensed under the MIT License.  

---

## ✨ Author

Developed by **Bhushan Bhande** 🧑‍💻
