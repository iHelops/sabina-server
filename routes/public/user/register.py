from flask import Blueprint, jsonify, request, make_response
from webargs import flaskparser, fields
from service import user_service

register_router = Blueprint('register', __name__)

fields_model = {
    'email': fields.Email(required=True),
    'phone': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'password': fields.String(required=True)
}


@register_router.route('/user/register', methods=['POST'])
def register():
    data = flaskparser.parser.parse(fields_model, request)
    user_data = user_service.registration(data['email'], data['phone'], data['first_name'], data['last_name'], data['password'])
    res = make_response(jsonify(user_data))
    res.set_cookie('session', user_data['session'], httponly=True)
    return res
