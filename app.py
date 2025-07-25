from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Dummy ML prediction function for Bawang Merah only
def predict_prices():
    base_price = 30500
    predictions = [base_price + random.randint(-500, 500) for _ in range(5)]
    return predictions

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/predict', methods=['GET'])
def api_predict():
    predicted_prices = predict_prices()
    labels = [f'Hari {i+1}' for i in range(len(predicted_prices))]
    return jsonify({
        "commodity": "Bawang Merah",
        "labels": labels,
        "predicted_prices": predicted_prices
    })

if __name__ == '__main__':
    app.run(debug=True)