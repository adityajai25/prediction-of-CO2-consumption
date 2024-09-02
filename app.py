#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    co2_emission = round(prediction[0], 2)

    if co2_emission < 113:
        result_class = 'green'
        prediction_text = f'CO2 Emission: {co2_emission} g/km (Low Emissions)'
    elif 113 <= co2_emission <= 130:
        result_class = 'yellow'
        prediction_text = f'CO2 Emission: {co2_emission} g/km (Moderate Emissions)'
    else:
        result_class = 'red'
        prediction_text = f'CO2 Emission: {co2_emission} g/km (High Emissions)'

    return render_template('index.html', prediction_text=prediction_text, result_class=result_class)

if __name__ == "__main__":
    app.run(debug=True)