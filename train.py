import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("data/Training.csv")

# Features and Target
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("="*50)
print("Model Accuracy:", accuracy)
print("="*50)

# Save model
joblib.dump(model, "models/disease_model.pkl")

print("\n✅ Model saved successfully!")  