    python -m http.server 8000
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data (replace with your actual data)
height = np.array([150, 160, 170, 180, 190]).reshape(-1, 1)  # Height in cm
weight = np.array([50, 60, 70, 80, 90])  # Weight in kg


# Create a linear regression model
model = LinearRegression()

# Train the model using height as input and weight as output
model.fit(height, weight)

# Predict weight for a new height
new_height = np.array([175]).reshape(-1, 1)
predicted_weight = model.predict(new_height)

print("Predicted weight for height", new_height[0][0], "cm:", predicted_weight[0], "kg")

    from flask import Flask, request, jsonify
    import pickle
    import numpy as np
    
    app = Flask(__name__)
    
    # Load the model
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.get_json()
        input_data = np.array(data['input']).reshape(1, -1)
        prediction = model.predict(input_data).tolist()
        return jsonify({'prediction': prediction})
    
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(response['Body'].read().decode('utf-8'))

    transformed_data = []
    for record in data:
        transformed_record = {
            'field1': record['field1'].upper(),
            'field2': record['field2'] * 2
        }
        transformed_data.append(transformed_record)
    
    s3.put_object(Bucket='processed-data-bucket', Key=key, Body=json.dumps(transformed_data))

    return {
        'statusCode': 200,
        'body': json.dumps('Data transformation complete')
    }