from flask import Blueprint, jsonify
from decorators import login_required, admin_required
from service import order_service

orders_get_all_router = Blueprint('orders_get_all', __name__)


@orders_get_all_router.route('/admin/orders', methods=['GET'])
@login_required
@admin_required
def get_all_orders(user):
    orders = order_service.get_orders()
    return jsonify(orders)
