from flask import Flask, render_template, request
import os
import re
import smtplib
from email.message import EmailMessage
from topsis_logic import run_topsis
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load credentials from environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        if not valid_email(email):
            return render_template("index.html", message="Invalid email format")

        weights_list = list(map(float, weights.split(",")))
        impacts_list = impacts.split(",")

        if len(weights_list) != len(impacts_list):
            return render_template("index.html", message="Weights and impacts count mismatch")

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "result.csv")

        file.save(input_path)

        run_topsis(input_path, weights_list, impacts_list, output_path)

        # Send email
        msg = EmailMessage()
        msg["Subject"] = "TOPSIS Result"
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg.set_content("Please find the TOPSIS result attached.")

        with open(output_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="csv",
                filename="result.csv"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)

        return render_template("index.html", message="Result sent successfully via email")

    except Exception as e:
        return render_template("index.html", message=str(e))

if __name__ == "__main__":
    app.run(debug=True) 