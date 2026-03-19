import pandas as pd
import os
import joblib
from sklearn.preprocessing import StandardScaler


def calculate_aqi(row):
    """
    Simplified AQI calculation (max pollutant method)
    You can later replace with CPCB standard formula
    """
    return max(row['pm2_5'], row['pm10'], row['no2'], row['so2'])


def feature_engineering(df):

    # ✅ Clean column names
    df.columns = df.columns.str.strip().str.lower()
    print("📌 Columns:", df.columns.tolist())

    # ✅ Rename columns to standard format
    rename_map = {
        'pm2.5': 'pm2_5',
        'pm25': 'pm2_5',
        'rspm': 'pm10'   # Important fix
    }
    df.rename(columns=rename_map, inplace=True)

    # ✅ Required features (based on your dataset)
    features = ['pm2_5', 'pm10', 'no2', 'so2']
    
    # ✅ Check if required columns exist
    for col in features:
        if col not in df.columns:
            raise ValueError(f"❌ Missing column: {col}")

    # ✅ Select only needed columns
    df = df[features].copy()

    # ✅ Convert to numeric
    df = df.apply(pd.to_numeric, errors='coerce')

    # ✅ Drop missing values
    df = df.dropna()

    # ✅ Remove extreme outliers (basic filtering)
    df = df[
        (df['pm2_5'] >= 0) & (df['pm2_5'] <= 500) &
        (df['pm10'] >= 0) & (df['pm10'] <= 600) &
        (df['no2'] >= 0) & (df['no2'] <= 200) &
        (df['so2'] >= 0) & (df['so2'] <= 200)
    ]

    # ✅ Create AQI (target variable)
    df['aqi'] = df.apply(calculate_aqi, axis=1)

    print("📊 Cleaned Data Shape:", df.shape)

    # ✅ Split features & target
    X = df[features]
    y = df['aqi']

    # ✅ Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_scaled = pd.DataFrame(X_scaled, columns=features)

    # ✅ Create folders if not exist
    os.makedirs('../models', exist_ok=True)
    os.makedirs('../data/processed', exist_ok=True)

    # ✅ Save scaler & feature columns
    joblib.dump(scaler, '../models/scaler.pkl')
    joblib.dump(features, '../models/feature_columns.pkl')

    # ✅ Save processed dataset
    processed_df = pd.concat([X_scaled, y.reset_index(drop=True)], axis=1)
    processed_df.to_csv('../data/processed/processed_data.csv', index=False)

    print("✅ Feature Engineering Completed Successfully!")


if __name__ == "__main__":
    df = pd.read_csv(
        r"C:\Users\Priyansu Sikdar\Downloads\air pollution\data\archive\data.csv",
        encoding='latin1',
        low_memory=False
    )

    feature_engineering(df)