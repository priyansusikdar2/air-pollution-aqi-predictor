# 🌍 **Air Quality Prediction System (India) 🇮🇳**

An end-to-end **Machine Learning + Full Stack Web Application** that predicts **Air Quality Index (AQI)** using real-world **India Air Quality Data**.
Built with a powerful combination of **ML models, FastAPI backend, and interactive frontends (Streamlit + HTML/CSS/JavaScript)**.

---

# 🚀 **Project Overview**

Air pollution is a major concern in India’s urban environments. This project leverages machine learning to **predict AQI based on pollutant levels** such as PM2.5, PM10, NO2, SO2, and CO.

✨ The system provides:

* Real-time AQI predictions
* Interactive UI for user inputs
* Scalable backend API
* Multiple frontend interfaces

---

# 🧠 **Tech Stack**

### 🔹 Backend

* **FastAPI** ⚡ (High-performance API framework)
* Python 🐍

### 🔹 Frontend

* 🌐 HTML, CSS, JavaScript
* 📊 Streamlit (for quick ML dashboard)

### 🔹 Machine Learning

* XGBoost 🔥
* Scikit-learn
* Pandas, NumPy
* RandomForest Classifier

---

# 📂 **Project Structure**

```
air-pollution-prediction/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Model_Experiments.ipynb
│
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── predict.py
│
├── models/
│   ├── trained_models.pkl
│   ├── scaler.pkl
│   ├── feature_columns.pkl
│
├── api/
│   ├── app.py
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── styles.css
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ **How It Works**

1. 📥 Data is collected from India Air Quality datasets
2. 🧹 Data is cleaned and preprocessed
3. ⚙️ Feature engineering is applied
4. 🤖 ML model (XGBoost) is trained
5. 🚀 Model is served via FastAPI
6. 🌐 Users interact via frontend UI or Streamlit

---

# 🧪 **Run the Project**

## 🔹 1. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔹 2. Run ML Pipeline

```
python src/feature_engineering.py
python src/train_model.py
```

---

## 🔹 3. Start Backend (FastAPI)

```
cd api
uvicorn app:app --reload
```

👉 Open:

```
http://127.0.0.1:8000/docs
```

---

## 🔹 4. Run Frontend (HTML/JS)

```
cd frontend
python -m http.server 5500
http://localhost:5500/index.html
```

👉 Open:

```
http://localhost:5500
```

---

## 🔹 5. Run Streamlit App

```
streamlit run app.py
```

---

# 📊 **Features**

✔️ Real-time AQI Prediction
✔️ Clean & Modern UI
✔️ Dual Frontend (Web + Streamlit)
✔️ High Accuracy Model (XGBoost)
✔️ Scalable API Backend
✔️ Easy to Deploy

---

# 🌡️ **Input Parameters**

* PM2.5
* PM10
* NO2
* SO2
* CO

---

# 🎯 **Output**

* Predicted AQI Value
* AQI Category (Good, Moderate, Hazardous, etc.)

---

# 📸 **Demo Preview**

✨ Interactive dashboard with:

* Dynamic AQI values
* Color-coded pollution levels
* Smooth user experience

---

# 🚀 **Future Enhancements**

* 📍 Location-based AQI prediction
* 🌐 Live API integration (weather + pollution)
* 📊 Data visualization dashboard
* ☁️ Cloud deployment (AWS / Render)
* 📱 Mobile responsive UI

---

# 💯 **Key Learnings**

* End-to-end ML pipeline development
* Feature engineering challenges
* Model deployment using FastAPI
* Frontend-backend integration
* Debugging real-world ML issues

---

# 🤝 **Contributing**

Contributions are welcome!
Feel free to fork the repo and submit a pull request 🚀

---

# 📜 **License**

This project is open-source and available under the MIT License.

---

# ⭐ **Support**

If you found this project helpful:

👉 Give it a ⭐ on GitHub
👉 Share with others
👉 Connect and collaborate

---

# 🌍 **Let’s Build a Cleaner Future Together!**
