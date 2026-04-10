from modules.data_loader import load_dataset
from modules.process import preprocess
from modules.train import train_models
from modules.predict import predict

df = load_dataset()
X_train, X_test, y_train, y_test = preprocess(df)
train_models(X_train, X_test, y_train, y_test)

# Example prediction
student_features = [67, 16, 5, 39, 1]  # [attendance, study_hours, assignments, internal_marks, extracurricular]
feature_names = ['Attendance', 'Study Hours', 'Assignments Completed', 'Internal Marks', 'Extracurricular']

print("\n" + "="*60)
print("STUDENT PERFORMANCE PREDICTION")
print("="*60)
for name, value in zip(feature_names, student_features):
    print(f"{name}: {value}")

prediction = predict(student_features)
print("\n" + "-"*60)
print(f"\u2192 PREDICTION RESULT:")
print(f"   Pass: {prediction['Pass']:>6.2f}%")
print(f"   Fail: {prediction['Fail']:>6.2f}%")
print("="*60)