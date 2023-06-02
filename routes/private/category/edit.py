from flask import Blueprint, jsonify, request
from webargs import flaskparser, fields
from decorators import login_required, admin_required
from service import category_service

category_edit_router = Blueprint('category_edit', __name__)

fields_model = {
    'id': fields.String(required=True),
    'name': fields.String(missing=None),
    'icon': fields.String(missing=None),
}


@category_edit_router.route('/admin/category/edit', methods=['POST'])
@login_required
@admin_required
def create_category(user):
    data = flaskparser.parser.parse(fields_model, request)
    category = category_service.edit_category(data['id'], data['name'], data['icon'])
    return jsonify(category)
