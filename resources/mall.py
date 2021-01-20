from flask_restful import Resource
from models.mall import MallModel

class Mall(Resource):
    def get(self, name):
        mall = MallModel.find_by_name(name)
        if mall:
            return mall.json()
        else:
            return {'message': 'this mall {} does not exist'.format(name)}, 404

    def post(self, name):
        mall = MallModel.find_by_name(name)
        if mall is None:
            mall = MallModel(name)
            mall.save_to_db()
        else:
            return {'message': 'mall already exists.'}, 400

    def delete(self, name):
        mall = MallModel.find_by_name(name)
        if mall:
            mall.delete_from_db()
            return {'message': 'mall deleted successfully'}
        else:
            return {'message': 'mall with name {} does not exist'.format(name)}, 404


class MallList(Resource):
    def get(self):
        return {'malls': [mall.json() for mall in MallModel.query.all()]}

