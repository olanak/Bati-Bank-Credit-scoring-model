import os
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load your trained model
model = joblib.load('models/best_rf_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = pd.DataFrame(data)
        required_features = ['Recency', 'Frequency', 'Monetary', 'Amount_WoE']
        if not all(feature in input_data.columns for feature in required_features):
            return jsonify({'error': 'Missing required features'}), 400
        
        predictions = model.predict(input_data[required_features])
        probabilities = model.predict_proba(input_data[required_features])[:, 1]
        
        return jsonify({'predictions': predictions.tolist(), 'probabilities': probabilities.tolist()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
