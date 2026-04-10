import joblib
import numpy as np

def predict(new_data):
    model=joblib.load("saved_models/best_model.pkl")

    new_data=np.array(new_data).reshape(1,-1)
    probabilities=model.predict_proba(new_data)[0]
    
    # Get Pass and Fail percentages
    fail_percent = probabilities[0] * 100
    pass_percent = probabilities[1] * 100
    
    return {
        "Pass": round(pass_percent, 2),
        "Fail": round(fail_percent, 2)
    }