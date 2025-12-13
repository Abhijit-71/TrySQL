from flask import render_template , redirect
from flask_jwt_extended import verify_jwt_in_request
from app import app



@app.route("/")
def home():
    try:
        verify_jwt_in_request()
        # token exists AND is valid
        return redirect("/runner/dashboard")
    except:
        # no token / invalid / expired
        return render_template("index.html")