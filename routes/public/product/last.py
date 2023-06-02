from flask import Blueprint, jsonify
from service import product_service

products_last_router = Blueprint('products_last', __name__)


@products_last_router.route('/products/last', methods=['GET'])
def last_products():
    product = product_service.get_lasts()
    return jsonify(product)
