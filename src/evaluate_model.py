import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test):
    
    preds = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)
    
    print("📊 Model Performance:")
    print("RMSE:", rmse)
    print("R2 Score:", r2)


if __name__ == "__main__":
    from src.train_model import train_model
    
    model, X_test, y_test = train_model('../data/processed/processed_data.csv')
    evaluate_model(model, X_test, y_test)