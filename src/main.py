from flask import Flask, jsonify, render_template, request
from numpy import bool_, e, float64, round
import joblib
import json

app = Flask(__name__)
with open("mappers.json", "r") as f:
  mappers = json.load(f)
model = joblib.load("model.pkl")

@app.route("/", methods=["GET"])
def home():
  return render_template("index.html", mappers=mappers)

@app.route("/salary", methods=["GET"])
def calculateSalary():
  company_location = float64(request.args.get("company_location"))
  company_size = float64(request.args.get("company_size"))
  experience_level = float64(request.args.get("experience_level"))
  job_popularity = float64(request.args.get("job_popularity"))
  remote_ratio = float64(request.args.get("remote_ratio"))
  ricl = bool_(request.args.get("ricl"))
  return jsonify(float(round(e ** model.predict([[experience_level, remote_ratio, company_location, company_size, job_popularity, ricl]]), 2)))

app.run(debug=False)