ORDER = (
    {"$unwind": "$products"},
    {"$lookup": {
        "from": "product",
        "foreignField": "_id",
        "localField": "products.product",
        "as": "products.product",
    }},
    {"$unwind": "$products.product"},
    {"$lookup": {
        "from": "category",
        "foreignField": "_id",
        "localField": "products.product.category",
        "as": "products.product.category",
    }},
    {"$set": {
        "products.product.category": {
            "$arrayElemAt": ["$products.product.category.name", 0]
        }
    }},
    {"$group": {
        "_id": '$_id',
        "products": {
            "$push": '$products'
        }
    }},
    {"$lookup": {
        "from": "order",
        "foreignField": "_id",
        "localField": "_id",
        "as": "orderDetail",
    }},
    {"$unwind": "$orderDetail"},
    {"$addFields": {
        "orderDetail.products": "$products"
    }},
    {"$replaceRoot": {
        "newRoot": '$orderDetail'
    }},
    {"$lookup": {
        "from": "user",
        "foreignField": "_id",
        "localField": "user",
        "as": "user",
    }},
    {"$unwind": "$user"},
)
