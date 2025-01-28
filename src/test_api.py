import requests
import json

# Define the API URL
url = 'http://127.0.0.1:5000/predict'

# Define the input data (replace with your data)
input_data = {
    'Recency': [0.5, 0.3, 0.8],
    'Frequency': [0.7, 0.4, 0.6],
    'Monetary': [0.6, 0.5, 0.9],
    'Amount_WoE': [0.2, 0.1, 0.3]
}

# Convert input data to JSON
input_json = json.dumps(input_data)

# Send POST request to the API
response = requests.post(url, json=input_data)

# Print the response
print(response.json())