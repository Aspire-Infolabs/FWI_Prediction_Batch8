from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pickle
import os
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "fwi_secret_key_2026"

# -------------------------------
# Load model and scaler
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, "ridge.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "scaler.pkl"), "rb"))

# -------------------------------
# Temporary user storage (demo)
# -------------------------------
users = {}  # { email : hashed_password }

# -------------------------------
# Login required decorator
# -------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# -------------------------------
# HOME PAGE (Project Info)
# -------------------------------
@app.route("/home")
@login_required
def landing_home():
    return render_template("home.html")

# -------------------------------
# LOGIN
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in users and check_password_hash(users[email], password):
            session["user"] = email
            return redirect(url_for("predict_page"))  # ✅ FIXED
        else:
            return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")

# -------------------------------
# SIGNUP
# -------------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in users:
            return render_template("signup.html", error="User already exists")

        users[email] = generate_password_hash(password)
        return redirect(url_for("login"))

    return render_template("signup.html")

# -------------------------------
# PREDICTOR INPUT PAGE
# -------------------------------
@app.route("/predict-page")
@login_required
def predict_page():
    return render_template("index.html")

# -------------------------------
# PREDICTION
# -------------------------------
@app.route("/predict", methods=["POST"])
@login_required
def predict():
    try:
        features = [
            float(request.form["Temperature"]),
            float(request.form["RH"]),
            float(request.form["Ws"]),
            float(request.form["Rain"]),
            float(request.form["FFMC"]),
            float(request.form["DMC"]),
            float(request.form["DC"]),
            float(request.form["ISI"]),
            float(request.form["BUI"]),
            int(request.form["Region"])
        ]

        scaled_input = scaler.transform(np.array([features]))
        fwi = round(model.predict(scaled_input)[0], 2)

        if fwi < 5:
            risk, color, desc = "Low Fire Risk", "green", "Safe conditions. Fire unlikely."
        elif fwi < 15:
            risk, color, desc = "Moderate Fire Risk", "orange", "Dry conditions. Stay cautious."
        elif fwi < 30:
            risk, color, desc = "High Fire Risk", "red", "Dangerous conditions. Fire may spread."
        else:
            risk, color, desc = "Extreme Fire Risk", "darkred", "Critical conditions. Immediate action required."

        return render_template(
            "result.html",
            fwi=fwi,
            risk=risk,
            color=color,
            desc=desc
        )

    except:
        return render_template("result.html", error="Invalid input values")

# -------------------------------
# LOGOUT
# -------------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
