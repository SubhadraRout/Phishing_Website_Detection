from flask import Flask, render_template, request, jsonify
import joblib
from feature_extractor import extract_features

app = Flask(__name__)

# Load your trained model
model = joblib.load("phishing_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data["url"]

    # Extract features for the input URL
    features = extract_features(url)
    url_lower = url.lower()

    # ✅ HARD PHISHING RULES (HIGH-RISK PATTERNS)

    # Rule 1: IP address based URL
    if features["ip"].iloc[0] == 1:
        label = "Phishing"

    # Rule 2: @ symbol attack
    elif "@" in url_lower:
        label = "Phishing"

    else:
        # ✅ ML prediction fallback
        result = model.predict(features)[0]
        label = "Phishing" if result == 1 else "Legitimate"

    return jsonify({"label": label})


if __name__ == "__main__":
    app.run(debug=True)
