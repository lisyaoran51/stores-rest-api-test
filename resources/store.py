from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()

        return {'message': 'store not found'}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': "store '{}' already exist".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': "error occur creating '{}' store".format(name)}, 500


        return store.json(), 201




    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if not store:
            return {'message': 'store not exist'.format(name)}, 200

        try:
            store.delete_from_db()
        except:
            return {'message': " the '{}' store deleting error".format(name)}, 500

        return {'message': 'store deleted.'}



class StoreList(Resource):
    def get(self):
        # return {'stores': list(map(lambda x: x.json(), StoreModel.find_all()))}
        return {'stores': [store.json() for store in StoreModel.find_all()]}
