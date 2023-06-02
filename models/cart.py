from mongoengine import Document, ReferenceField
from models import User, Product


class Cart(Document):
    user = ReferenceField(User, required=True)
    product = ReferenceField(Product, required=True)
