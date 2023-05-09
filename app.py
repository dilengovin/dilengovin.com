'''

File: app.py
Author: Dilen Govin
Purpose: Backend for routing and serving the html files

'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")