from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from decorators import login_required
from service import cart_service

cart_remove_router = Blueprint('cart_remove', __name__)

fields_model = {
    'id': fields.String(required=True)
}


@cart_remove_router.route('/cart/remove', methods=['DELETE'])
@login_required
def remove_cart(user):
    data = flaskparser.parser.parse(fields_model, request)
    cart_service.remove_cart(user['id'], data['id'])
    return Response(status=204)
