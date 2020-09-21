import functools
from flask import(
    Blueprint, request, jsonify
)
from flask_jwt import jwt_required, current_identity

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/register', methods=['POST'])
def register():
    return jsonify(message="success")

@bp.route('/update', methods=['GET','POST'])
@jwt_required()
def protected():
    return '%s' % current_identity