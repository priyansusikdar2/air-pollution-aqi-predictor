import pandas as pd

def preprocess_data(df):
    # Handle missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)
    
    # Encode categorical columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category').cat.codes
    
    print("✅ Data preprocessing completed")
    return df


if __name__ == "__main__":
    from data_ingestion import load_data
    
    df = load_data(r"C:\Users\Priyansu Sikdar\Downloads\air pollution\data\archive\global air pollution dataset.csv")
    df = preprocess_data(df)
    
    print(df.head())