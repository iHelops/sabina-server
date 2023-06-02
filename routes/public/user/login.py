from flask import Blueprint, jsonify, request, make_response
from webargs import flaskparser, fields
from service import user_service

login_router = Blueprint('login', __name__)

fields_model = {
    'email': fields.Email(required=True),
    'password': fields.String(required=True)
}


@login_router.route('/user/login', methods=['POST'])
def login():
    data = flaskparser.parser.parse(fields_model, request)
    user_data = user_service.login(data['email'], data['password'])
    res = make_response(jsonify(user_data))
    res.set_cookie('session', user_data['session'], httponly=True)
    return res
