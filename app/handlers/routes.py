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
        G1 = request.args.get('G1')
        G2 = request.args.get('G2')
        Dalc = request.args.get('Dalc')
        data = [[G1], [G2], [Dalc]]
        query_df = pd.DataFrame({
            'G1': pd.Series(G1),
            'G2': pd.Series(G2),
            'Dalc': pd.Series(Dalc)
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.asscalar(prediction))
