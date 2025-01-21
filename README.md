# Downtime Prediction API

This project is a Flask-based RESTful API that predicts machine downtime using a trained machine learning model. The API accepts input parameters like temperature and runtime, and returns a prediction along with a confidence score.

---

## Features
- **Prediction Endpoint:** `/predict`
- **Request Method:** POST
- **Input Format:** JSON
- **Output Format:** JSON

---

## Example Input and Output

### **Example Request**:
POST `http://127.0.0.1:5000/predict`

#### Input JSON:
```json
{
    "Temperature": 85,
    "Run_Time": 300
}
```

### **Example Response**:
```json
{
    "Downtime": "No",
    "Confidence": 0.91
}
```

---

## How to Set Up and Test Locally

### **1. Clone the Repository**
- Clone this repository to your local machine using the following command:
  ```bash
  git clone <repository-url>
  cd Downtime-Prediction-API
  ```

### **2. Install Required Dependencies**
- Make sure you have Python installed (preferably version 3.8 or later).
- Install the dependencies listed in `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

### **3. Ensure Model File is Present**
- Verify that the trained model file (`downtime_model.pkl`) is in the project directory.

### **4. Run the Flask App**
- Start the Flask server by running:
  ```bash
  python app.py
  ```
- Once the server is running, you should see output like this:
  ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

### **5. Test the API**

#### **Using Postman**:
1. Open Postman and create a new request.
2. Set the request method to **POST**.
3. Enter the URL: `http://127.0.0.1:5000/predict`.
4. Go to the **Body** tab, select **raw**, and set the format to **JSON**.
5. Enter the input data, e.g.,
   ```json
   {
       "Temperature": 85,
       "Run_Time": 300
   }
   ```
6. Click **Send**. You should see a response like:
   ```json
   {
       "Downtime": "No",
       "Confidence": 0.91
   }
   ```

## Project Files

1. **`app.py`**: The Flask application code.
2. **`downtime_model.pkl`**: The trained machine learning model.
3. **`requirements.txt`**: List of dependencies to run the project.
4. **`README.md`**: Documentation for setup and usage.
5. **`sample_dataset.csv`**: A sample dataset used for training the model (optional).

---


## Contact
If you have any issues or questions, feel free to open an issue in the repository or contact me directly.


