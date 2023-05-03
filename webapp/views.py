from flask import Flask
from flask import render_template
from datetime import datetime
from flask import send_file, current_app as app
from . import app

@app.route("/")
def home():
    return render_template("index.html")

""" @app.route("/resume")
def resume():
    with open('/assets/DilenGovin_Resume.pdf', 'rb') as static_file:
        return send_file(static_file, attachment_filename='DilenGovin_Resume.pdf') """
