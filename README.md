# Student Performance Prediction (ML Project)

## Overview
A Machine Learning model that predicts whether a student will **Pass or Fail** based on academic behavior. The model returns probability percentages for Pass and Fail predictions.

## Prediction Output
Instead of discrete categories, the model now provides probability-based predictions:
- **Pass %**: Probability of passing
- **Fail %**: Probability of failing

Example: `Pass: 85.5% | Fail: 14.5%`

## Features
- Binary classification (Pass/Fail)
- Probability-based predictions
- Dataset generation and loading
- Preprocessing pipeline
- Model training (Logistic Regression, Decision Tree, Random Forest)
- Best model selection with automatic comparison
- Pickle model saving/loading
- High accuracy (95%+)

## Tech Stack
- Python 3.8+
- Pandas, NumPy
- Scikit-learn
- Joblib

## How to Run

### 1. Clone Repository
```bash
git clone <repository-url>
cd student-performance-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Project

**Generate dataset:**
```bash
python gen_dataset.py
```

**Train model and make prediction:**
```bash
python main.py
```

## Data Features Used For Training

| Feature | Range |
|---------|-------|
| attendance | 40–100 |
| study_hours | 1–30 |
| assignments_completed | 2–10 |
| internal_marks | 20–50 |
| extracurricular | 0–1 |

## Example Prediction

**Input:**
- Attendance: 80
- Study hours: 16
- Assignments completed: 5
- Internal marks: 39
- Extracurricular: 1

**Output:**
```
Pass: X.XX% | Fail: Y.YY%
```

## Model Performance

The model achieves high accuracy in binary classification:
- Logistic Regression: ~100%
- Decision Tree: ~95%
- Random Forest: ~94%

Best model is automatically selected and saved.

## Classification Logic
- **Pass**: Score > 155
- **Fail**: Score ≤ 155

Score calculation:
```
score = (0.3 × attendance) + (1.5 × study_hours) + (3 × assignments) + (2 × internal_marks)
```

## Project Structure
```
student-performance-prediction/
├── data/
│   └── dataset.csv          # Dataset for training
├── modules/
│   ├── data_loader.py       # Load CSV dataset
│   ├── process.py           # Preprocessing & train-test split
│   ├── train.py             # Model training & selection
│   └── predict.py           # Prediction with probabilities
├── saved_models/
│   └── best_model.pkl       # Trained model
├── gen_dataset.py           # Dataset generation script
├── main.py                  # Main entry point
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Usage Example

```python
from modules.predict import predict

# Provide student data: [attendance, study_hours, assignments, internal_marks, extracurricular]
student_data = [80, 16, 5, 39, 1]
prediction = predict(student_data)

print(f"Pass: {prediction['Pass']}% | Fail: {prediction['Fail']}%")
```

## Future Improvements
- Add more features (previous grades, activity participation, etc.)
- Real-time prediction API
- Web interface for predictions
- Cross-validation for better model evaluation

│── data  
│── modules  
│── saved_models   
│── main.py  
│── README.md  
│── statement.md  
│── requirements.txt

## Accuracy
- Logistic Regression: 99%
- Decision Tree: 96%
- Random Forest: 97%

## Future Scope
- Use real datasets
- Add more student parameters
- Deploy online
- Use Streamlit to build gui









