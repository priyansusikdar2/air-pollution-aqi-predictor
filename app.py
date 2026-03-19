# streamlit_app.py
import streamlit as st
import requests

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Air Pollution AQI Predictor",
    page_icon="🌫️",
    layout="centered"
)

st.title("🌫️ Air Pollution AQI Predictor")
st.markdown(
    """
    Enter the pollutant values below to predict the Air Quality Index (AQI).
    The model is trained using PM2.5, PM10, NO2, and SO2.
    """
)

# =========================
# USER INPUT
# =========================
pm2_5 = st.number_input("PM2.5 (µg/m³)", min_value=0.0, max_value=500.0, value=120.0)
pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, max_value=600.0, value=180.0)
no2 = st.number_input("NO2 (µg/m³)", min_value=0.0, max_value=200.0, value=40.0)
so2 = st.number_input("SO2 (µg/m³)", min_value=0.0, max_value=200.0, value=20.0)

# =========================
# PREDICTION BUTTON
# =========================
if st.button("Predict AQI"):

    # Prepare payload
    payload = {
        "pm2_5": pm2_5,
        "pm10": pm10,
        "no2": no2,
        "so2": so2
    }

    try:
        # Replace with your FastAPI endpoint URL
        API_URL = "http://127.0.0.1:8000/predict"
        response = requests.post(API_URL, json=payload)
        result = response.json()

        predicted_aqi = result.get("predicted_aqi", None)

        if predicted_aqi is not None:
            st.subheader("🌫️ Predicted AQI")
            st.metric(label="AQI Value", value=f"{predicted_aqi:.2f}")

            # =========================
            # AQI CATEGORY
            # =========================
            if predicted_aqi <= 50:
                category = "Good ✅"
                color = "green"
            elif predicted_aqi <= 100:
                category = "Satisfactory 🙂"
                color = "lightgreen"
            elif predicted_aqi <= 200:
                category = "Moderate ⚠️"
                color = "orange"
            elif predicted_aqi <= 300:
                category = "Poor 🔴"
                color = "red"
            elif predicted_aqi <= 400:
                category = "Very Poor 🟣"
                color = "purple"
            else:
                category = "Severe 🟤"
                color = "brown"

            st.markdown(f"<h3 style='color:{color}'>{category}</h3>", unsafe_allow_html=True)

        else:
            st.error("❌ Could not get prediction from API.")

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.stop()