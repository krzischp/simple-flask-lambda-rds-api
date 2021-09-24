import json

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from model import Data, DataSchema, db

Datas_schema = DataSchema(many=True)
Data_schema = DataSchema()


# http://127.0.0.1:5000/api/Data
class DataResource(Resource):
    def get(self):
        id = request.args.getlist('id')
        if id is not None:
            Data = Data.query.filter_by(
                id=id).first()
            if not Data:
                return {"errors": "Data could not be find"}, 404
            return {'status': 'success', 'data': Data_schema.dump(Data)}, 200
        Datas = Data.query.all()
        Datas = Datas_schema.dump(Datas)
        return {'status': 'success', 'data': Datas}, 200

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        # Validate and deserialize input
        try:
            data = Data_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
            # Create a new Data
        Data = Data(notes=data['notes'])
        db.session.add(Data)
        db.session.commit()
        result = Data_schema.dump(
            Data.query.get(Data.id))
        return {"status": "success", "message": "Created new Data.", "data": result}, 201

    def delete(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            # data = Data_schema.load(json_data)
            data = Data_schema.load(json_data)

        except ValidationError as err:
            return err.messages, 422

        Data = Data.query.filter_by(
            id=data['id']).delete()
        db.session.commit()

        result = Data_schema.dump(Data)

        return {"status": 'success', 'data': result}, 200
