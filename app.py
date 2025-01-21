from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("downtime_model.pkl")

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data from the request
    
    # Convert JSON data into a pandas DataFrame
    input_data = pd.DataFrame([data])
    
    # Make a prediction using the model
    prediction = model.predict(input_data)[0]  # Predict the downtime (0 or 1)
    confidence = max(model.predict_proba(input_data)[0])  # Confidence score
    
    # Prepare the response as a JSON object
    response = {
        "Downtime": "Yes" if prediction == 1 else "No",
        "Confidence": round(confidence, 2)
    }
    
    return jsonify(response)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
