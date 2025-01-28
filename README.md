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

