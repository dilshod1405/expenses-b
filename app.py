from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/api/monthly-expenses')
def monthly_expenses():
    df = pd.read_csv("company_expenses.csv")
    df_grouped = df.groupby("month")["amount ($)"].sum().reset_index()
    
    data = {
        "labels": df_grouped["month"].tolist(),
        "values": df_grouped["amount ($)"].tolist()
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
