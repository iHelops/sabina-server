from bson import ObjectId
from aggregations.cart import CART
from aggregations.product import PRODUCT
from dtos import ProductDto
from exceptions import ApiError
from models import Product, Cart


def add_cart(user_id: str, product_id: str):
    cart = Cart.objects(user=user_id, product=product_id)
    if cart:
        raise ApiError.BadRequest('This product already exist in cart')

    product = list(Product.objects(id=product_id).aggregate(PRODUCT))
    if not product:
        raise ApiError.BadRequest('Product not found')

    cart = Cart(
        user=ObjectId(user_id),
        product=ObjectId(product_id)
    )
    cart.save()

    return ProductDto(product[0]).get_dict()


def remove_cart(user_id: str, product_id: str):
    cart = Cart.objects(user=user_id, product=product_id)
    if not cart:
        raise ApiError.BadRequest('There is no such product in the cart')

    cart.delete()


def get_cart(user_id: str):
    cart_items = list(Cart.objects(user=user_id).aggregate(CART))
    return [ProductDto(cart['product']).get_dict() for cart in cart_items]
