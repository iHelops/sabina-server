# user
from .public.user.register import register_router
from .public.user.login import login_router
from .public.user.check import check_router
from .public.user.logout import logout_router

# file
from .public.file.upload_image import upload_image_router
from .public.file.upload_icon import upload_icon_router
from .public.file.file import file_router

# category
from .private.category.create import category_create_router
from .public.category.get import category_get_router
from .private.category.remove import category_remove_router
from .private.category.edit import category_edit_router
from .public.category.get_products import category_get_products_router

# product
from .private.product.create import product_create_router
from .public.product.get import product_get_router
from .private.product.remove import product_remove_router
from .private.product.edit import product_edit_router
from .private.product.get_all import product_get_all_router
from .public.product.last import products_last_router
from .public.product.random import products_random_router
from .public.product.search import product_search_router

# cart
from .public.cart.add import cart_add_router
from .public.cart.get import cart_get_router
from .public.cart.remove import cart_remove_router

# order
from .public.order.create import order_create_router
from .public.order.get import orders_get_router
from .private.order.get_all import orders_get_all_router
from .private.order.edit import order_edit_router

routes = [
    register_router,
    login_router,
    check_router,
    logout_router,

    upload_image_router,
    upload_icon_router,
    file_router,

    category_get_products_router,
    category_get_router,
    category_create_router,
    category_remove_router,
    category_edit_router,

    product_create_router,
    product_get_all_router,
    product_get_router,
    product_remove_router,
    product_edit_router,
    products_last_router,
    products_random_router,
    product_search_router,

    cart_add_router,
    cart_get_router,
    cart_remove_router,

    order_create_router,
    orders_get_router,
    orders_get_all_router,
    order_edit_router
]
