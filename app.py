from flask import render_template, Flask, request, app
import pickle
import numpy as np
from Logger_main import FirePredictLogger
import xgboost as xg
import sklearn
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
# loading the optimized model
model = pickle.load((open('model_xg.pkl', 'rb')))


@app.route('/')
def home():
    try:
        lg = FirePredictLogger.ineuron_scrap_logger()
        lg.info('initialization of home page of html started')
        return render_template('index.html')
    except Exception as e:
        lg.exception('This error occurred: {}'.format(e))


# when user press submit button this function will start executing
@app.route('/predict', methods=['POST'])
def predict():
    """
    This function predicts the output as per requirement and returns output.
    :return:
    """
    try:
        lg = FirePredictLogger.ineuron_scrap_logger()
        lg.info('initialization of prediction started through data received from html forms')
        data = [float(x) for x in request.form.values()]
        lg.info('inputs received from html form converted into list')
        final_features = [np.array(data)]
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(final_features)
        print(scaled_data)
        lg.info('standardization process is completed')
        output = model.predict(scaled_data)[0]
        lg.info('prediction of input is done successfully {}'.format(output))
        # print(output)
        if output == 0:
            text = 'The forest is safe'
            lg.info('prediction result shows: NO FIRE')
        else:
            text = 'The forest is not safe'
            lg.info('prediction result shows: FIRE')
        return render_template('index.html', prediction_text='{} :: chance of fire is {}'.format(text, output))
    except Exception as e:
        lg.exception('This error has occurred: {}'.format(e))
        return render_template('index.html', prediction_text='Kindly check the input again !!')

if __name__ == "__main__":
    app.run(debug=True)