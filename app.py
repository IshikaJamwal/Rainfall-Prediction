import numpy as np
import pickle
import math
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="template", static_folder="staticfiles")
model= pickle.load(open('build.pkl','rb'))

@app.route('/')
def abc():
    return render_template('index.html')

@app.route('/predict', methods = ['Post'])

def predict():
    float_feauters = [float(x) for x in request.form.values()]
    final_features = [np.array(float_feauters)]
    prediction= model.predict(final_features)
    if prediction ==0:
        return render_template('index.html', prediction_text = "There will be no rain").format(prediction)
    else:
        return render_template('index.html', prediction_text = "There will be rain").format(prediction)
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
