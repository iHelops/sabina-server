from mongoengine import Document, ReferenceField, StringField, DateField, EmbeddedDocumentListField, EmbeddedDocument, IntField
from models import User, Product


class ProductWithCount(EmbeddedDocument):
    count = IntField(default=1)
    product = ReferenceField(Product, required=True)


class Order(Document):
    user = ReferenceField(User, required=True)
    status = StringField(required=True)
    address = StringField(required=True)
    date = DateField(required=True)
    products = EmbeddedDocumentListField(ProductWithCount, required=True)
