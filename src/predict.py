import pandas as pd
import joblib
import os


def load_artifacts():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_DIR = os.path.join(BASE_DIR, "..", "models")

    model = joblib.load(os.path.join(MODEL_DIR, "trained_model.pkl"))
    scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
    features = joblib.load(os.path.join(MODEL_DIR, "feature_columns.pkl"))

    print("✅ Loaded model & artifacts")
    print("📌 Features:", features)

    return model, scaler, features


def prepare_input(input_dict, features, scaler):

    df = pd.DataFrame([input_dict])

    # ✅ Ensure all required features exist
    for col in features:
        if col not in df.columns:
            df[col] = 0

    # ✅ Correct order
    df = df[features]

    # ✅ Convert numeric
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)

    print("🚨 INPUT DF:\n", df)

    # ✅ Scale
    df_scaled = scaler.transform(df)

    return df_scaled


def predict_aqi(input_data):

    model, scaler, features = load_artifacts()

    X = prepare_input(input_data, features, scaler)

    prediction = model.predict(X)[0]

    print(f"\n🌫️ Predicted AQI: {round(prediction, 2)}")

    return prediction


# =========================
# TEST
# =========================
if __name__ == "__main__":

    # ✅ MUST MATCH TRAINING FEATURES
    sample_input = {
        "pm2_5": 120,
        "pm10": 180,
        "no2": 40,
        "so2": 20
    }

    predict_aqi(sample_input)