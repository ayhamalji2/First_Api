from flask_restful import reqparse, Resource
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("mall_id",
                        type=int,
                        required=True,
                        help='This field cannot be left blank.'
                        )

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message': 'store with name {} does not exist'.format(name)}, 404

    def post(self, name):
        data = Store.parser.parse_args()
        store = StoreModel.find_by_name(name)
        if store is None:
            store = StoreModel(name, data['mall_id'])
            store.save_to_db()
        else:
            return {'message': 'store already exists.'}, 400

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'store deleted successfully'}
        else:
            return {'message': 'store with name {} does not exist'.format(name)}, 404


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
