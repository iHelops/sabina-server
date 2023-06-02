from mongoengine import StringField, Document, ListField, IntField, ReferenceField, BooleanField
from models import Category


class Product(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    attachments = ListField(StringField())
    cost = IntField(required=True)
    discount = IntField(required=True)
    category = ReferenceField(Category, required=True)
    deleted = BooleanField(default=False)
