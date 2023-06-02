from mongoengine import StringField, Document


class Category(Document):
    name = StringField(required=True)
    icon = StringField(required=True)
