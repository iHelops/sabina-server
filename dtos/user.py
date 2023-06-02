class UserDto:
    def __init__(self, model: dict):
        self.id = str(model['_id'])
        self.email = model['email']
        self.phone = model['phone']
        self.first_name = model['first_name']
        self.last_name = model['last_name']
        self.avatar = model['avatar']
        self.role = model['role']

    def get_dict(self):
        return self.__dict__
