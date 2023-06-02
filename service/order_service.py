from bson import ObjectId
from aggregations.order import ORDER
from aggregations.product import PRODUCT
from dtos import OrderDto
from exceptions import ApiError
from models import Order, Product, User, ProductWithCount
from datetime import datetime


def create_order(user_id: str, address: str, products: list):
    if len(products) == 0:
        raise ApiError.BadRequest('Products not found')

    user = User.objects(id=user_id).first()
    if not user:
        raise ApiError.BadRequest('User not found')

    products_list = list(Product.objects(id__in=[i['product'] for i in products]).aggregate(PRODUCT))

    order = Order(
        user=ObjectId(user_id),
        status='in_processing',
        address=address,
        date=datetime.now(),
        products=[
            ProductWithCount(
                count=next((x for x in products if x['product'] == str(i['_id'])), None).get('count'),
                product=ObjectId(i['_id'])
            ) for i in products_list
        ]
    )

    order.save()

    order_dict = list(Order.objects(id=order.id).aggregate(ORDER))
    data = [OrderDto(i).get_dict() for i in order_dict]
    return data


def edit_order(order_id: str, address: str = None, status: str = None):
    order = Order.objects(id=order_id).first()
    if not order:
        raise ApiError.BadRequest('Order not found')

    args = {
        'set__address': address,
        'set__status': status
    }
    args = {key: value for key, value in args.items() if value is not None}

    if len(args) != 0:
        order.update(**args)

    order_dict = list(Order.objects(id=order_id).aggregate(ORDER))
    return OrderDto(order_dict[0]).get_dict()


def get_orders():
    orders = list(Order.objects().aggregate(ORDER))
    return [OrderDto(order).get_dict() for order in orders]


def get_user_orders(user_id: str):
    orders = list(Order.objects(user=user_id).aggregate(ORDER))
    return [OrderDto(order).get_dict() for order in orders]
