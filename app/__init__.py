import os
from flask import Flask, jsonify
from flask_jwt import JWT
from app.components import user
from werkzeug.security import safe_str_cmp

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    class User(object):
        def __init__(self, id, username, password):
            self.id = id
            self.username = username
            self.password= password

        def __str__(self):
            return "User(id='%s')" % self.id

    users = [
        User(1, 'user1','abcxyz'),
        User(2, 'user2','abcxyz'),
    ]

    username_table = {u.username: u for u in users}
    userid_table = {u.id: u for u in users}



    @app.route('/')
    def index():
        return jsonify(healthcheck="ok")

    @app.route('/health')
    def health():
        return jsonify(healthcheck="ok")

    def authenticate(username, password):
        # need to get user here or something
        user = username_table.get(username, None)
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

    # for any apps to NOT have auth, just make a method that reutnrs None and I think it'll work
    def authagain(username, password):
        return None

    def identity(payload):
        user_id = payload['identity']
        return userid_table.get(user_id, None)

    app.config['SECRET_KEY'] = 'super-secret'
    jwt = JWT(app, authagain, identity)
    app.register_blueprint(user.bp)
    return app

