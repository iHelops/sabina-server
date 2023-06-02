CART = (
    {"$lookup": {
        "from": "product",
        "foreignField": "_id",
        "localField": "product",
        "as": "product",
    }},
    {"$unwind": "$product"},
    {"$lookup": {
        "from": "category",
        "foreignField": "_id",
        "localField": "product.category",
        "as": "product.category",
    }},
    {"$set": {
        "product.category": {
            "$arrayElemAt": ["$product.category.name", 0]
        }
    }}
)
