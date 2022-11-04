import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the student route it is great!"


    @app.route('/student')
    def predict():
        #use entries from the query string here but could also use json
        reason = request.args.get('reason')
        studyTime = request.args.get('studyTime')
        activities = request.args.get('activities')
        dalc = request.args.get('Dalc')
        freetime = request.args.get('freetime')
        absences = request.args.get('absences')
        G1 = request.args.get('G1')
        G2 = request.args.get('G2')
        G3 = request.args.get('G3')
        data = [[reason], [studyTime], [activities], [dalc], [freetime], [absences], [G1], [G2], [G3]]
        query_df = pd.DataFrame({
            'reason': pd.Series(reason),
            'studyTime': pd.Series(studyTime),
            'dalc': pd.Series(dalc)
            'freetime': pd.Series(freetime)
            'absences': pd.Series(absences)
            'G1': pd.Series(G1)
            'G2': pd.Series(G2)
            'G3': pd.Series(G3)
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.asscalar(prediction))
