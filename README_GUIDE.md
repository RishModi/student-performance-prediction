# Student Performance Prediction System

A beginner-friendly machine learning project to predict whether students will pass or fail based on their study habits and performance indicators.

## Project Files

- **dataset.csv** - Synthetic dataset with 259+ student records
- **train.py** - Script to train the Logistic Regression model
- **predict.py** - Script to make predictions on new students
- **model.pkl** - Saved trained model (generated after running train.py)

## Features Used for Prediction

1. **study_hours_per_day** - Hours spent studying daily (1-5)
2. **attendance_percentage** - Class attendance rate (60-97%)
3. **previous_exam_score** - Score from last exam (48-92)
4. **sleep_hours** - Hours of sleep per night (4.5-8.5)
5. **social_media_hours** - Hours spent on social media per day (0-6)
6. **class_participation** - Level of classroom participation (Low, Medium, High)
7. **assignments_completed** - Number of assignments completed (3-10)

## Model Overview

### What is Logistic Regression?

Logistic Regression is a simple machine learning algorithm that:
- Learns patterns from the training data
- Assigns a **probability score** between 0 and 1 to each student
- If probability > 0.5 → Predicts **PASS**
- If probability ≤ 0.5 → Predicts **FAIL**

### How It Works (Simple Explanation)

1. **Learning Phase (train.py):**
   - The model reads the dataset
   - It learns which combinations of features typically lead to pass/fail
   - For example: (high study hours + high attendance + high sleep) → more likely to PASS

2. **Prediction Phase (predict.py):**
   - You provide student features
   - The model calculates a probability score
   - It outputs: "PASS with 95% confidence" or "FAIL with 78% confidence"

---

## How to Run

### Step 1: Install Dependencies

```bash
pip install pandas scikit-learn joblib
```

### Step 2: Train the Model

```bash
python train.py
```

**What happens:**
- Loads dataset.csv
- Splits data: 80% for training, 20% for testing
- Trains the Logistic Regression model
- Displays accuracy metrics
- Saves trained model as **model.pkl**

**Expected Output:**
```
Loading dataset...
Training Logistic Regression model...
Model trained successfully!

Accuracy: 100.00%
...
Model saved successfully!
```

### Step 3: Make Predictions

```bash
python predict.py
```

**What happens:**
- Loads the saved model.pkl
- Tests on 2 sample students
- Displays pass/fail prediction with confidence scores

**Expected Output:**
```
Student 1 (Good Student):
  Prediction: ✓ PASS
  Fail Probability:  0.00%
  Pass Probability:  100.00%

Student 2 (Struggling Student):
  Prediction: ✗ FAIL
  Fail Probability:  100.00%
  Pass Probability:  0.00%
```

---

## Code Explanation

### train.py Structure

```
1. Load Dataset (259 students)
   ↓
2. Separate Features (X) and Target (y)
   ↓
3. Encode Categorical Features (class_participation: Low/Medium/High → numbers)
   ↓
4. Split Data (207 training, 52 testing)
   ↓
5. Train Logistic Regression Model
   ↓
6. Evaluate Accuracy (typically 95-100%)
   ↓
7. Save Model as model.pkl
```

### predict.py Structure

```
1. Load Saved Model (model.pkl)
   ↓
2. Prepare Sample Student Data
   ↓
3. Encode Categorical Features (same way as training)
   ↓
4. Get Prediction + Probability
   ↓
5. Display Results
```

---

## How to Modify for Your Own Predictions

Edit the student data in **predict.py**:

```python
student_3 = {
    'study_hours_per_day': 3.5,      # Change this
    'attendance_percentage': 85,      # Change this
    'previous_exam_score': 75,        # Change this
    'sleep_hours': 7,                 # Change this
    'social_media_hours': 2,          # Change this
    'class_participation': 'Medium',  # Change this
    'assignments_completed': 8        # Change this
}

# Add a call to predict
predict_student(student_3, "Student 3 (Custom)")
```

---

## Understanding the Results

### Perfect Predictions (100% Accuracy)

The model achieves 100% accuracy because the dataset has clear patterns:
- **Students who study many hours, attend classes, sleep well, and avoid social media → PASS**
- **Students who study little, skip classes, sleep poorly, and spend time on social media → FAIL**

In real-world scenarios, accuracy is usually 70-90% because student performance has more complex factors.

### Confidence Scores

- **Pass Probability: 95%** = Model is very confident the student will pass
- **Pass Probability: 55%** = Model is uncertain (borderline case)
- **Pass Probability: 5%** = Model is very confident the student will fail

---

## Dataset Information

The dataset contains 259 student records with:
- **Training Data:** 207 students (used to teach the model)
- **Testing Data:** 52 students (used to verify accuracy)
- **Pass Students:** 146
- **Fail Students:** 113
- **Target:** Binary classification (0 = Fail, 1 = Pass)

---

## Key Concepts for Beginners

| Concept | Meaning |
|---------|---------|
| **Model** | The algorithm that learns patterns and makes predictions |
| **Training** | Teaching the model by showing it many examples |
| **Features** | Input variables (study hours, attendance, etc.) |
| **Target** | What we want to predict (pass or fail) |
| **Accuracy** | Percentage of correct predictions (100% = all correct) |
| **Probability** | Confidence score (0 to 1, or 0% to 100%) |

---

## Troubleshooting

**Error: ModuleNotFoundError: No module named 'sklearn'**
→ Run: `pip install scikit-learn pandas joblib`

**Error: FileNotFoundError: dataset.csv**
→ Make sure all files are in the same directory

**Error: FileNotFoundError: model.pkl**
→ Run `train.py` first to generate the model

---

## Possible Extensions (Next Steps)

1. **Add more students** - Edit dataset.csv
2. **Try different models** - Replace LogisticRegression with RandomForest, SVM, etc.
3. **Feature scaling** - Normalize numeric features for better results
4. **Cross-validation** - Use k-fold cross-validation for more reliable accuracy
5. **Hyperparameter tuning** - Adjust model parameters for better performance

---

## Files Generated After Training

```
student-performance-prediction/
├── train.py              (Training script)
├── predict.py            (Prediction script)
├── dataset.csv           (Input data)
├── model.pkl             (Generated after train.py)
└── README.md             (This file)
```

---

## Summary

✅ Train the model: `python train.py`
✅ Make predictions: `python predict.py`
✅ Model accuracy: 100% (on test data)
✅ Ready to use!

Happy learning! 🎓
