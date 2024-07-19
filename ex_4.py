# Create a sample api which takes path of
# csv file as input and return central tendencies if success
import pandas as pd
from pathlib import Path
from flask import Flask, request, jsonify


app = Flask("Central Tendencies")


@app.route("/central-tendencies", methods=["POST"])
def calculate_tendencies():

    file_path = request.json.get("path", None)
    if file_path is None or not Path(file_path).exists():
        return jsonify({"status": "File Path not found"}), 404

    data = pd.read_csv(file_path)
    result = {}

    for column in data.select_dtypes(include=["number"]).columns:
        column_data = data[column].dropna()
        result[column] = {
            "mean": column_data.mean(),
            "median": column_data.median(),
            "mode": column_data.mode().tolist()
        }

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
