# - project_folder/
#   - app.py
#   - templates/
#     - index.html
#     - result.html  # For displaying ML results
#   - static/
#     - style.css   # CSS styles for your templates
#   - ml_model/
#     - linear_regression_model.py  # Your ML model code



from flask import Flask, render_template, request
import requests
from ml_model.linear_regression_model import predict_suitability

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Community Garden Optimizer!'

@app.route('/index')
def index():
    # Make API request to Open Meteo
    api_key = 'YOUR_OPEN_METEO_API_KEY'
    response = requests.get(f'https://api.open-meteo.com/weather?apiKey={api_key}&latitude=YOUR_LATITUDE&longitude=YOUR_LONGITUDE')
    
    # Process the data as needed
    weather_data = response.json()

    # Pass data to the frontend
    return render_template('index.html', weather_data=weather_data)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract weather data from the form or API
        weather_data = request.form.get('weather_data')  # Adjust based on your form input names

        # Call your ML model function
        predicted_suitabilities = predict_suitability(weather_data)

        # Render the results page with predicted data
        return render_template('result.html', predicted_suitabilities=predicted_suitabilities)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
