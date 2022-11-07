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
        Dalc = request.args.get('Dalc')
        G1 = request.args.get('G1')
        G2 = request.args.get('G2')
        studytime = request.args.get('studytime')

        # keep parameters in this exact order (order in which they were fitted)
        query_df = pd.DataFrame({
            'Dalc': pd.Series(Dalc),
            'G1': pd.Series(G1),
            'G2': pd.Series(G2),
            'studytime': pd.Series(studytime) 
        })

        prediction = clf.predict(query_df)

        return jsonify(np.ndarray.item(prediction))
