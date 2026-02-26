from flask import Flask, render_template, request
import os
from log_parser import parse_log
from detection import detect_bruteforce, detect_scanning
from anomaly import detect_anomalies

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    results = {
        "total_logs": 0,
        "bruteforce": [],
        "scanning": [],
        "anomalies": []
    }

    if request.method == "POST":
        file = request.files["logfile"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            df = parse_log(filepath)

            results["bruteforce"] = detect_bruteforce(df)
            results["scanning"] = detect_scanning(df)
            results["anomalies"] = detect_anomalies(df)
            results["total_logs"] = len(df)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)