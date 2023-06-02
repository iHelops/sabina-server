from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from decorators import login_required, admin_required
from service import category_service

category_remove_router = Blueprint('category_remove', __name__)

fields_model = {
    'id': fields.String(required=True)
}


@category_remove_router.route('/admin/category/remove', methods=['DELETE'])
@login_required
@admin_required
def remove_category(user):
    data = flaskparser.parser.parse(fields_model, request)
    category_service.remove_category(data['id'])
    return Response(status=204)
