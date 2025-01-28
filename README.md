# Bati Bank Credit Scoring API

This project provides an API for predicting customer creditworthiness using a trained Random Forest model. The API allows users to input customer behavioral features and returns predictions and probabilities for their credit score category.

---

## Features

- **Prediction Endpoint**: Provides creditworthiness predictions based on customer data.
- **Input Validation**: Ensures the required fields are present in the input JSON.
- **Machine Learning Model**: Leverages a pre-trained Random Forest model for accurate predictions.
- **Deployed on Render**: The API is hosted at [Bati Bank Credit Scoring API](https://bati-bank-credit-scoring-model.onrender.com).

---

## API Overview

### Base URL
The API is available at:
https://bati-bank-credit-scoring-model.onrender.com


### Endpoint
- **`POST /predict`**: Accepts customer data and returns predictions.

### Input Format
The API expects a JSON payload with the following fields:

| Field           | Type   | Description                                  |
|------------------|--------|----------------------------------------------|
| `Recency`       | Number | The time since the last transaction (in days). |
| `Frequency`     | Number | The number of transactions in a given period. |
| `Monetary`      | Number | The total monetary value of transactions.     |
| `Amount_WoE`    | Number | Weight of Evidence-transformed transaction amount. |

#### Example Input
```json
[
    {
        "Recency": 5,
        "Frequency": 10,
        "Monetary": 300,
        "Amount_WoE": 0.5
    }
]
```

## Response Format
The API returns a JSON object containing:

predictions: A list of predicted credit categories (e.g., 0 for "Bad", 1 for "Good").
probabilities: A list of probabilities for the "Good" credit category.
Example Response
```json
{
    "predictions": [1],
    "probabilities": [0.85]
}
```
##  How to Use the API
Testing the API with curl
```bash
curl -X POST https://bati-bank-credit-scoring-model.onrender.com/predict \
-H "Content-Type: application/json" \
-d '[{"Recency": 5, "Frequency": 10, "Monetary": 300, "Amount_WoE": 0.5}]'
```
```bash
import requests

url = "https://bati-bank-credit-scoring-model.onrender.com/predict"
data = [
    {"Recency": 5, "Frequency": 10, "Monetary": 300, "Amount_WoE": 0.5}
]

response = requests.post(url, json=data)
print(response.json())
```

## Installation for Local Development
Prerequisites
Python 3.12 or later
Virtual environment (recommended)
Steps
1. Clone the repository:
```bash
git clone https://github.com/olanak/Bati-Bank-Credit-scoring-model
cd Bati-Bank-Credit-scoring-model
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Flask application:
```bash
   python app.py
```
The server will start on http://0.0.0.0:5000/

##  Deployment
This API is deployed on Render at the following URL:
```bash
https://bati-bank-credit-scoring-model.onrender.com
```
To redeploy or update the app:
1. Commit your changes to the GitHub repository.
2. Render will automatically detect the changes and redeploy the app.

## Notes
Ensure the best_rf_model.pkl file is present in the models directory.
Use the correct features as required by the model for accurate predictions.
The app is designed to run both locally and on Render.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the 10 Academy team for their guidance and support throughout this project.





