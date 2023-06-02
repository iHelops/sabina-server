from flask import Blueprint, jsonify, request
from webargs import flaskparser, fields
from decorators import login_required
from service import order_service

order_create_router = Blueprint('order_create', __name__)

fields_model = {
    'address': fields.String(required=True),
    'products': fields.List(fields.Nested(
        {'product': fields.String(required=True), 'count': fields.Integer(required=True)}
    ))
}


@order_create_router.route('/order/create', methods=['POST'])
@login_required
def create_order(user):
    data = flaskparser.parser.parse(fields_model, request)
    order = order_service.create_order(user['id'], data['address'], data['products'])
    return jsonify(order)
