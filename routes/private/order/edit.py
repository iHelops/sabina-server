from flask import Blueprint, jsonify, request
from webargs import flaskparser, fields
from decorators import login_required, admin_required
from service import order_service

order_edit_router = Blueprint('order_edit', __name__)

fields_model = {
    'id': fields.String(required=True),
    'address': fields.String(missing=None),
    'status': fields.String(missing=None),
}


@order_edit_router.route('/admin/order/edit', methods=['POST'])
@login_required
@admin_required
def create_category(user):
    data = flaskparser.parser.parse(fields_model, request)
    order = order_service.edit_order(data['id'], data['address'], data['status'])
    return jsonify(order)
