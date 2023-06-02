class ProductDto:
    def __init__(self, model: dict):
        self.id = str(model['_id'])
        self.name = model['name']
        self.description = model['description']
        self.attachments = model['attachments']
        self.cost = model['cost']
        self.discount = model['discount']
        self.category = str(model['category']) if model.get('category') else None

    def get_dict(self):
        return self.__dict__
