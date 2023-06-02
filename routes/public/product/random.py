from flask import Blueprint, jsonify
from service import product_service

products_random_router = Blueprint('products_random', __name__)


@products_random_router.route('/products/random', methods=['GET'])
def last_products():
    product = product_service.get_random()
    return jsonify(product)
