import pandas as pd
import joblib
import os
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from xgboost import XGBRegressor


def train_model():

    # ✅ Load processed data
    df = pd.read_csv('../data/processed/processed_data.csv')
    df.columns = df.columns.str.strip().str.lower()

    # ✅ Load feature columns (VERY IMPORTANT)
    features = joblib.load('../models/feature_columns.pkl')

    # ✅ Detect target
    target = None
    for col in df.columns:
        if 'aqi' in col:
            target = col
            break

    if target is None:
        raise ValueError("❌ AQI column not found")

    # ✅ Ensure correct feature order
    X = df[features]
    y = df[target]

    print("📊 TARGET DISTRIBUTION:\n", y.describe())
    print("📌 FEATURES:", features)

    # ✅ Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 🔥 ADVANCED XGBOOST MODEL
    model = XGBRegressor(
        n_estimators=1000,
        learning_rate=0.03,
        max_depth=8,
        subsample=0.9,
        colsample_bytree=0.9,
        reg_alpha=0.1,
        reg_lambda=1,
        random_state=42
    )

    print("🚀 Training model...")

    # ✅ Early stopping
    model.fit(
        X_train, y_train,
        eval_set=[(X_test, y_test)],
        verbose=50
    )

    # ✅ Predictions
    preds = model.predict(X_test)

    # ✅ Metrics
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)

    print("\n📊 MODEL PERFORMANCE")
    print("RMSE:", round(rmse, 2))
    print("MAE :", round(mae, 2))
    print("R2  :", round(r2, 3))

    # ✅ Feature Importance
    importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values(by='importance', ascending=False)

    print("\n📌 Feature Importance:\n", importance)

    # ✅ Save everything
    os.makedirs('../models', exist_ok=True)

    joblib.dump(model, '../models/trained_model.pkl')
    importance.to_csv('../models/feature_importance.csv', index=False)

    print("\n✅ Model + Feature Importance saved successfully!")


if __name__ == "__main__":
    train_model()