# Downtime Prediction API

This project predicts machine downtime based on input parameters like temperature and run time using a trained machine learning model.

## Features
- **Endpoint:** `/predict`
- **Method:** POST
- **Input:** JSON (e.g., `{ "Temperature": 85, "Run_Time": 300 }`)
- **Output:** JSON (e.g., `{ "Downtime": "No", "Confidence": 0.91 }`)

## How to Set Up
1. Clone or download the project folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
