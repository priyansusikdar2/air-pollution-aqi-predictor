import pandas as pd

def load_data(file_path):
    df = pd.read_csv(r"C:\Users\Priyansu Sikdar\Downloads\air pollution\data\archive\global air pollution dataset.csv")
    
    # Clean column names
    df.columns = df.columns.str.strip().str.lower()
    
    print("✅ Data loaded successfully")
    return df


if __name__ == "__main__":
    df = load_data('../data/raw/air_quality.csv')
    print(df.head())