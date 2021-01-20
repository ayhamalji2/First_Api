from db import db


class MallModel(db.Model):
    __tablename__ = 'malls'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    stores = db.relationship('StoreModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def json(self):
        return {'name': self.name, 'stores': [store.json() for store in self.stores.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()