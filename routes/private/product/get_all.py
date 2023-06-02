from flask import Blueprint, jsonify
from decorators import login_required, admin_required
from service import product_service

product_get_all_router = Blueprint('product_get_all', __name__)


@product_get_all_router.route('/admin/products', methods=['GET'])
@login_required
@admin_required
def product_all(user):
    products = product_service.get_products()
    return jsonify(products)
