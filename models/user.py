from mongoengine import StringField, EmailField, Document, ListField


class User(Document):
    email = EmailField(required=True, unique=True)
    phone = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    avatar = StringField(null=True)
    role = StringField(required=True, default='user')
    password = StringField(required=True)
    sessions = ListField(StringField(), default=None, null=True)
