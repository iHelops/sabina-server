from flask import Blueprint, jsonify
from service import category_service

category_get_router = Blueprint('category_get', __name__)


@category_get_router.route('/categories', methods=['GET'])
def category_get():
    categories = category_service.get_categories()
    return jsonify(categories)
