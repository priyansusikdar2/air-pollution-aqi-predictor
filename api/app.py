from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# LOAD MODEL
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "models")

model = joblib.load(os.path.join(MODEL_DIR, "trained_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
columns = joblib.load(os.path.join(MODEL_DIR, "feature_columns.pkl"))

print("✅ Model loaded")
print("📌 Expected Features:", columns)


# =========================
# INPUT SCHEMA (MATCH TRAINING)
# =========================
class AQIInput(BaseModel):
    pm2_5: float
    pm10: float
    no2: float
    so2: float


# =========================
# HOME
# =========================
@app.get("/")
def home():
    return {"message": "AQI API Running 🚀"}


# =========================
# PREDICT
# =========================
@app.post("/predict")
def predict(data: AQIInput):

    print("\n🚨 RAW INPUT:", data)

    # ✅ Correct mapping (NO random feature names)
    input_data = {
        "pm2_5": data.pm2_5,
        "pm10": data.pm10,
        "no2": data.no2,
        "so2": data.so2
    }

    df = pd.DataFrame([input_data])

    # ✅ Ensure all features exist
    for col in columns:
        if col not in df.columns:
            df[col] = 0

    # ✅ Correct order
    df = df[columns]

    print("🚨 FINAL INPUT DF:\n", df)

    # ✅ Convert numeric
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)

    # ✅ Scale
    df_scaled = scaler.transform(df)

    # ✅ Predict
    prediction = model.predict(df_scaled)[0]

    print("🌫️ PREDICTED AQI:", prediction)

    return {
        "predicted_aqi": round(float(prediction), 2)
    }