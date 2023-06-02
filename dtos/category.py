class CategoryDto:
    def __init__(self, model: dict):
        self.id = str(model['_id'])
        self.name = model['name']
        self.icon = model['icon']

    def get_dict(self):
        return self.__dict__
