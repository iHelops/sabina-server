from flask import Blueprint, jsonify
from decorators import login_required
from service import order_service

orders_get_router = Blueprint('orders_get', __name__)


@orders_get_router.route('/orders', methods=['GET'])
@login_required
def get_orders(user):
    order = order_service.get_user_orders(user['id'])
    return jsonify(order)
