PRODUCT = (
    # {"$lookup": {
    #     "from": "category",
    #     "foreignField": "_id",
    #     "localField": "category",
    #     "as": "category",
    # }},
    # {"$set": {
    #     "category": {
    #         "$arrayElemAt": ["$category.name", 0]
    #     }
    # }}
    {'$match': {'deleted': False}},
)
