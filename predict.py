"""
Make predictions using the trained student performance model
"""

import joblib
from sklearn.preprocessing import LabelEncoder

# ===== STEP 1: Load the trained model =====
print("Loading trained model...")
model = joblib.load('model.pkl')
print("Model loaded successfully!\n")

# ===== STEP 2: Set up label encoder for class_participation =====
# We need the same encoding as used during training
le = LabelEncoder()
le.fit(['Low', 'Medium', 'High'])
participation_encoding = dict(zip(['Low', 'Medium', 'High'], le.transform(['Low', 'Medium', 'High'])))
print(f"Class participation encoding: {participation_encoding}\n")

# ===== STEP 3: Get user input =====
print("=" * 60)
print("STUDENT PERFORMANCE PREDICTION SYSTEM")
print("=" * 60)
print("\nEnter student information:")
print("(Valid participation levels: Low, Medium, High)\n")

try:
    study_hours = float(input("Study hours per day (e.g., 3.5): "))
    attendance = float(input("Attendance percentage (e.g., 85): "))
    previous_score = float(input("Previous exam score (e.g., 75): "))
    sleep_hours = float(input("Sleep hours per night (e.g., 7): "))
    social_media = float(input("Social media hours per day (e.g., 2): "))
    participation = input("Class participation (Low/Medium/High): ").capitalize()
    assignments = int(input("Assignments completed (e.g., 8): "))
    
    # Validate participation level
    if participation not in ['Low', 'Medium', 'High']:
        print("\n❌ Error: Participation must be Low, Medium, or High!")
        exit()
    
    # Create student dictionary
    student = {
        'study_hours_per_day': study_hours,
        'attendance_percentage': attendance,
        'previous_exam_score': previous_score,
        'sleep_hours': sleep_hours,
        'social_media_hours': social_media,
        'class_participation': participation,
        'assignments_completed': assignments
    }
    
except ValueError:
    print("\n❌ Error: Please enter valid numbers!")
    exit()

# ===== STEP 4: Make predictions =====
def predict_student(student_data, student_name):
    """
    Make prediction for a single student
    """
    print(f"\n{student_name}:")
    print("-" * 60)
    
    # Display student info
    for key, value in student_data.items():
        print(f"  {key}: {value}")
    
    # Encode class_participation
    encoded_participation = le.transform([student_data['class_participation']])[0]
    
    # Prepare data for prediction (order matters - must match training features)
    student_features = [
        student_data['study_hours_per_day'],
        student_data['attendance_percentage'],
        student_data['previous_exam_score'],
        student_data['sleep_hours'],
        student_data['social_media_hours'],
        encoded_participation,
        student_data['assignments_completed']
    ]
    
    # Get prediction
    prediction = model.predict([student_features])[0]
    probability = model.predict_proba([student_features])[0]
    
    # Display results
    print()
    if prediction == 1:
        result = "✓ PASS"
    else:
        result = "✗ FAIL"
    
    print(f"  Prediction: {result}")
    print(f"  Fail Probability:  {probability[0]:.2%}")
    print(f"  Pass Probability:  {probability[1]:.2%}")


# ===== STEP 5: Make prediction for the entered student =====
print("\n" + "=" * 60)
print("PREDICTION RESULT")
print("=" * 60)
predict_student(student, "Your Student")

print("\n" + "=" * 60)
print("Prediction complete!")
print("=" * 60)
