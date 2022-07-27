import os

from flask import Flask, jsonify

from app.config import app_config

app = Flask(__name__)


app.config.from_object(app_config[os.getenv('FLASK_ENV')])

@app.route("/")
def hello_world(): return jsonify({"teste": "teste"})
