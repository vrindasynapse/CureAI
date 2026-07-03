from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("models/disease_model.pkl")

# Load dataset
df = pd.read_csv("data/Training.csv")

# Get symptom names
symptoms = list(df.columns[:-1])


@app.route("/")
def home():
    return render_template("index.html", symptoms=symptoms)


@app.route("/predict", methods=["POST"])
def predict():
    
    try:
        selected = request.form.getlist("symptoms")

        input_data = [0] * len(symptoms)

        for symptom in selected:
            if symptom in symptoms:
                input_data[symptoms.index(symptom)] = 1

        prediction = model.predict([input_data])[0]

        return render_template(
            "index.html",
            symptoms=symptoms,
            prediction=prediction
        )

    except Exception as e:
        print(f"Failed to run prediction: {e}")

        return render_template(
            "index.html",
            symptoms=symptoms,
            prediction="Prediction failed"
        )
if __name__ == "__main__":
    app.run(debug=True)    
