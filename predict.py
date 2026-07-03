import pandas as pd
import joblib

# Load trained model
try:
    model = joblib.load("models/disease_model.pkl")
except FileNotFoundError:
    print("Model file missing")

# Load dataset to get symptom names
df = pd.read_csv("data/Training.csv")
symptoms = list(df.columns[:-1])

print("="*60)
print("Available Symptoms")
print("="*60)

for i, symptom in enumerate(symptoms):
    print(f"{i+1}. {symptom}")

print("\nEnter symptom numbers separated by comma")
print("Example: 1,5,10")

choices = input("Your symptoms: ")

selected = [int(x)-1 for x in choices.split(",")]

if not selected:
    return render_template("index.html",symptoms=symptoms,predictions="Please select symptoms")

input_data = [0]*len(symptoms)

for index in selected:
    input_data[index] = 1

prediction = model.predict([input_data])

print("\n==============================")
print("Predicted Disease:")
print(prediction[0])
print("==============================")   
