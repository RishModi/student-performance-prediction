import os
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_models(X_train, X_test, y_train, y_test):
    models = {
        "Logistic Regression": LogisticRegression(max_iter=500),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(random_state=42)
    }

    best_model = None
    best_acc = -1
    best_name = None

    for name, model in models.items():
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        acc = accuracy_score(y_test, predictions)

        print(f"{name} Accuracy: {acc * 100:.2f}%")

        if acc > best_acc:
            best_acc = acc
            best_model = model
            best_name = name

    print(f"\nBest Model: {best_name} with Accuracy: {best_acc * 100:.2f}%")

    # FORCE REAL SAVE DIRECTORY
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    save_dir = os.path.join(base_dir, "saved_models")
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, "best_model.pkl")

    joblib.dump(best_model, save_path)
    print("MODEL SAVED TO:", save_path)

    print("\nClassification Report:")
    print(classification_report(y_test, best_model.predict(X_test), target_names=['Fail', 'Pass']))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, best_model.predict(X_test)))