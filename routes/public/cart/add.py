from flask import Blueprint, jsonify, request
from webargs import flaskparser, fields
from decorators import login_required
from service import cart_service

cart_add_router = Blueprint('cart_add', __name__)

fields_model = {
    'product_id': fields.String(required=True),
}


@cart_add_router.route('/cart/add', methods=['POST'])
@login_required
def add_cart(user):
    data = flaskparser.parser.parse(fields_model, request)
    product = cart_service.add_cart(user['id'], data['product_id'])
    return jsonify(product)
