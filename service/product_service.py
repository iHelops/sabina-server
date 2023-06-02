from aggregations.product import PRODUCT
from dtos import ProductDto
from exceptions import ApiError
from models import Product, Category


def create_product(name: str, description: str, attachments: list, cost: int, discount: int, category_id: str):
    category = Category.objects(id=category_id).first()
    if not category:
        raise ApiError.BadRequest('Category not found')

    product = Product(
        name=name,
        description=description,
        attachments=attachments,
        cost=cost,
        discount=discount,
        category=category
    )

    product.save()

    product_dict = dict(product.to_mongo())
    return ProductDto(product_dict).get_dict()


def remove_product(product_id: str):
    product = Product.objects(id=product_id).first()
    if not product:
        raise ApiError.BadRequest('Product not found')

    product.update(set__deleted=True)


def edit_product(product_id: str, name: str = None, description: str = None, attachments: list = None, cost: int = None, discount: int = None, category_id: str = None):
    product = Product.objects(id=product_id).first()
    if not product:
        raise ApiError.BadRequest('Product not found')

    args = {
        'set__name': name,
        'set__description': description,
        'set__attachments': attachments,
        'set__cost': cost,
        'set__discount': discount,
    }
    args = {key: value for key, value in args.items() if value is not None}

    if category_id:
        category = Category.objects(id=category_id).first()
        if not category:
            raise ApiError.BadRequest('Category not found')

        args.update({'set__category': category})

    if len(args) != 0:
        product.update(**args)

    product_dict = list(Product.objects(id=product_id).aggregate(PRODUCT))
    return ProductDto(product_dict[0]).get_dict()


def get_product(product_id: str):
    product = list(Product.objects(id=product_id).aggregate(PRODUCT))
    if not product:
        raise ApiError.BadRequest('Product not found')

    return ProductDto(product[0]).get_dict()


def search(query: str, position: int):
    products = list(Product.objects(name__icontains=query).aggregate((*PRODUCT, {'$limit': position + 8}, {'$skip': position})))
    return [ProductDto(product).get_dict() for product in products]


def get_products():
    products = Product.objects().aggregate(PRODUCT)

    products_dict = list(products)
    return [ProductDto(product).get_dict() for product in products_dict]


def get_lasts():
    products = Product.objects().order_by('-id').aggregate((*PRODUCT, {'$limit': 20}))

    products_dict = list(products)
    return [ProductDto(product).get_dict() for product in products_dict]


def get_random():
    products = Product.objects().aggregate((*PRODUCT, {'$sample': {'size': 4}}))

    products_dict = list(products)
    return [ProductDto(product).get_dict() for product in products_dict]
