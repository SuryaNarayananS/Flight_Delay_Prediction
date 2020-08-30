from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == "POST":

        MONTH = int(request.form["MONTH"])
        DAY = int(request.form["DAY"])
        DAY_OF_WEEK = int(request.form["DAY_OF_WEEK"])
        AIRLINE = float(request.form["AIRLINE"])
        ORIGIN_AIRPORT = int(request.form["ORIGIN_AIRPORT"])
        DESTINATION_AIRPORT = int(request.form["DESTINATION_AIRPORT"])
        SCHEDULED_DEPARTURE = float(request.form["SCHEDULED_DEPARTURE_HOUR"])
        DEPARTURE_TIME = float(request.form["DEPARTURE_TIME_HOUR"])
        TAXI_IN = float(request.form["TAXI_IN"])
        TAXI_OUT = float(request.form["TAXI_OUT"])
        SCHEDULED_ARRIVAL = float(request.form["SCHEDULED_ARRIVAL_HOUR"])
        ARRIVAL_TIME = float(request.form["ARRIVAL_TIME_HOUR"])
        ARRIVAL_DELAY = float(request.form["ARRIVAL_DELAY"])
        SCHEDULED_TIME = float(request.form["SCHEDULED_TIME"])
    prediction=model.predict([[MONTH, DAY, DAY_OF_WEEK, AIRLINE, ORIGIN_AIRPORT, DESTINATION_AIRPORT,
        SCHEDULED_DEPARTURE, DEPARTURE_TIME, TAXI_IN, TAXI_OUT, SCHEDULED_ARRIVAL, ARRIVAL_TIME, ARRIVAL_DELAY,
        SCHEDULED_TIME]])
    # output='{0:.{1}f}'.format(prediction[0][1], 2)

    return render_template('index.html',pred='Flight will be Delayed by min= {}'.format(prediction))

if __name__ == '__main__':
    app.run(debug=True)