from flask import Blueprint, jsonify
from service import category_service

category_get_products_router = Blueprint('category_get_products', __name__)


@category_get_products_router.route('/category/<category_id>&position=<int:position>', methods=['GET'])
def get_products(category_id, position):
    products = category_service.get_products(category_id, position)
    return jsonify(products)
