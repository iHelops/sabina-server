from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from decorators import login_required, admin_required
from service import product_service

product_remove_router = Blueprint('product_remove', __name__)

fields_model = {
    'id': fields.String(required=True)
}


@product_remove_router.route('/admin/product/remove', methods=['DELETE'])
@login_required
@admin_required
def remove_product(user):
    data = flaskparser.parser.parse(fields_model, request)
    product_service.remove_product(data['id'])
    return Response(status=204)
