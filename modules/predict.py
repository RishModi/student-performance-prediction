import joblib
import numpy as np
import pandas as pd

def predict(new_data):
    model = joblib.load("saved_models/best_model.pkl")
    
    # Create DataFrame with proper feature names to avoid warnings
    feature_names = ['attendance', 'study_hours', 'assignments_completed', 'internal_marks', 'extracurricular']
    df_data = pd.DataFrame([new_data], columns=feature_names)
    
    # Get probabilities
    probabilities = model.predict_proba(df_data)[0]
    
    # Get Pass and Fail percentages (class 0 = Fail, class 1 = Pass)
    fail_percent = probabilities[0] * 100
    pass_percent = probabilities[1] * 100
    
    return {
        "Pass": round(pass_percent, 2),
        "Fail": round(fail_percent, 2)
    }