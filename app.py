from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')

# Symulowane dane pomiarowe
data = {
    "labels": ["2025-04-01", "2025-04-02", "2025-04-03", "2025-04-04", "2025-04-05"],
    "pm25": [35, 45, 60, 75, 90],
    "pm10": [50, 60, 80, 100, 120]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)