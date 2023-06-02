from aggregations.product import PRODUCT
from dtos import CategoryDto, ProductDto
from exceptions import ApiError
from models import Category, Product


def create_category(name: str, icon: str):
    category = Category(
        name=name,
        icon=icon
    )

    category.save()

    category_dict = dict(category.to_mongo())
    return CategoryDto(category_dict).get_dict()


def remove_category(category_id: str):
    category = Category.objects(id=category_id).first()
    if not category:
        raise ApiError.BadRequest('Category not found')

    category.delete()


def edit_category(category_id: str, name: str = None, icon: str = None):
    category = Category.objects(id=category_id).first()
    if not category:
        raise ApiError.BadRequest('Category not found')

    args = {
        'set__name': name,
        'set__icon': icon
    }
    args = {key: value for key, value in args.items() if value is not None}

    if len(args) != 0:
        category.update(**args)
        category.reload()

    category_dict = dict(category.to_mongo())
    return CategoryDto(category_dict).get_dict()


def get_categories():
    categories = list(Category.objects().as_pymongo())
    return [CategoryDto(category).get_dict() for category in categories]


def get_products(category_id: str, position: int):
    category = Category.objects(id=category_id).first()
    if not category:
        raise ApiError.BadRequest('Category not found')

    products = Product.objects(category=category).aggregate((*PRODUCT, {'$limit': position + 8}, {'$skip': position}))
    if not products:
        raise ApiError.BadRequest('Products not found')

    product_dict = list(products)
    return [ProductDto(product).get_dict() for product in product_dict]
