from flask import Blueprint, jsonify, request
from webargs import flaskparser, fields
from decorators import login_required, admin_required
from service import product_service

product_edit_router = Blueprint('product_edit', __name__)

fields_model = {
    'id': fields.String(required=True),
    'name': fields.String(missing=None),
    'description': fields.String(missing=None),
    'attachments': fields.List(fields.String(), missing=None, ),
    'cost': fields.Integer(missing=None),
    'discount': fields.Integer(missing=None),
    'category_id': fields.String(missing=None)
}


@product_edit_router.route('/admin/product/edit', methods=['POST'])
@login_required
@admin_required
def edit_product(user):
    data = flaskparser.parser.parse(fields_model, request)
    product = product_service.edit_product(data['id'], data['name'], data['description'], data['attachments'], data['cost'], data['discount'], data['category_id'])
    return jsonify(product)
