from flask import Blueprint, jsonify, request
from webargs import flaskparser, fields
from decorators import login_required, admin_required
from service import category_service

category_create_router = Blueprint('category_create', __name__)

fields_model = {
    'name': fields.String(required=True),
    'icon': fields.String(required=True),
}


@category_create_router.route('/admin/category/create', methods=['POST'])
@login_required
@admin_required
def create_category(user):
    data = flaskparser.parser.parse(fields_model, request)
    category = category_service.create_category(data['name'], data['icon'])
    return jsonify(category)
