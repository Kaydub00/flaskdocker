import os
from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    @app.route('/')
    def index():
        return jsonify(healthcheck="ok")

    @app.route('/health')
    def health():
        return jsonify(healthcheck="ok")

    return app

