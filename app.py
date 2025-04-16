from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained Random Forest model
model = joblib.load("rf_model.pkl")

@app.route("/")
def home():
    return "Random Forest Model API is up and running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Expecting JSON input with 'data' as a list of input features
        data = request.get_json().get("data")
        # Convert to numpy array, adjust shape as needed (e.g., [[feature1, feature2,...]])
        input_data = np.array(data).reshape(1, -1)
        prediction = model.predict(input_data)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
