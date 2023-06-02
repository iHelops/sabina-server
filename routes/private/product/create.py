from flask import Blueprint, jsonify, request
from webargs import flaskparser, fields
from decorators import login_required, admin_required
from service import product_service

product_create_router = Blueprint('product_create', __name__)

fields_model = {
    'name': fields.String(required=True),
    'description': fields.String(required=True),
    'attachments': fields.List(fields.String(), missing=[], ),
    'cost': fields.Integer(required=True),
    'discount': fields.Integer(required=True),
    'category_id': fields.String(required=True)
}


@product_create_router.route('/admin/product/create', methods=['POST'])
@login_required
@admin_required
def create_product(user):
    data = flaskparser.parser.parse(fields_model, request)
    product = product_service.create_product(data['name'], data['description'], data['attachments'], data['cost'], data['discount'], data['category_id'])
    return jsonify(product)
