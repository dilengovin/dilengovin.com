from flask import Flask
from flask import render_template
from datetime import datetime
from flask import send_file, current_app as app
from . import app

@app.route("/")
def home():
    return render_template("index.html")

