from dtos import UserDto, ProductDto


class OrderDto:
    def __init__(self, model: dict):
        self.id = str(model['_id'])
        self.user = UserDto(model['user']).get_dict()
        self.address = model['address']
        self.status = model['status']
        self.date = model['date']
        self.products = [{'product': ProductDto(i['product']).get_dict(), 'count': i['count']} for i in model['products']]

    def get_dict(self):
        return self.__dict__
