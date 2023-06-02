from flask import Blueprint, jsonify, request
from decorators import login_required
from service import cart_service

cart_get_router = Blueprint('cart_get', __name__)


@cart_get_router.route('/cart/get', methods=['GET'])
@login_required
def get_cart(user):
    products = cart_service.get_cart(user['id'])
    return jsonify(products)
