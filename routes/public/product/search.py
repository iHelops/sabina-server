from flask import Blueprint, jsonify
from service import product_service

product_search_router = Blueprint('product_search', __name__)


@product_search_router.route('/products/search&query=<query>&position=<int:position>', methods=['GET'])
def product_search(query, position):
    products = product_service.search(query, position)
    return jsonify(products)
