"""
Train a Logistic Regression model to predict student pass/fail
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# ===== STEP 1: Load the dataset =====
print("Loading dataset...")
df = pd.read_csv('dataset.csv')
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}\n")

# ===== STEP 2: Prepare features and target =====
# Features (all columns except 'pass')
X = df.drop('pass', axis=1)
# Target (what we want to predict: 0 = fail, 1 = pass)
y = df['pass']

print(f"Features: {list(X.columns)}")
print(f"Target values: 0 = Fail, 1 = Pass")
print(f"Class distribution:\n{y.value_counts()}\n")

# ===== STEP 3: Encode categorical features =====
# 'class_participation' is categorical (Low, Medium, High)
# We need to convert it to numbers
label_encoders = {}
categorical_columns = ['class_participation']

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le
    print(f"Encoded '{col}': {dict(zip(le.classes_, le.transform(le.classes_)))}")

print()

# ===== STEP 4: Split data into training and testing sets =====
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}\n")

# ===== STEP 5: Train the model =====
print("Training Logistic Regression model...")
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)
print("Model trained successfully!\n")

# ===== STEP 6: Evaluate the model =====
print("Evaluating model...")

# Predict on test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2%}")
print()

# Show detailed classification report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Fail', 'Pass']))

# Show confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(f"                 Predicted")
print(f"                 Fail  Pass")
print(f"Actual Fail       {cm[0][0]}    {cm[0][1]}")
print(f"       Pass       {cm[1][0]}    {cm[1][1]}\n")

# ===== STEP 7: Save the model =====
print("Saving model as 'model.pkl'...")
joblib.dump(model, 'model.pkl')
print("Model saved successfully!")
