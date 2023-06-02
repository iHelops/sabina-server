from flask import Blueprint, jsonify
from service import product_service

product_get_router = Blueprint('product_get', __name__)


@product_get_router.route('/product/<product_id>', methods=['GET'])
def category(product_id):
    product = product_service.get_product(product_id)
    return jsonify(product)
