from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from model import Data, DataSchema, db

datas_schema = DataSchema(many=True)
data_schema = DataSchema()

# http://127.0.0.1:5000/api/Data


class DataResource(Resource):
    def get(self):
        id = request.args.getlist('id')
        if id:
            data = Data.query.filter_by(
                id=id).first()
            if not data:
                return {"errors": "Data could not be find"}, 404
            return {'status': 'success', 'data': data_schema.dump(data)}, 200
        datas = Data.query.all()
        datas = datas_schema.dump(datas)
        return {'status': 'success', 'data': datas}, 200

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        # Validate and deserialize input
        try:
            data = data_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
            # Create a new data
        data = Data(notes=data['notes'])
        db.session.add(data)
        db.session.commit()
        result = data_schema.dump(
            Data.query.get(data.id))
        return {"status": "success", "message": "Created new Data.", "data": result}, 201

    def delete(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            # data = data_schema.load(json_data)
            data = data_schema.load(json_data)

        except ValidationError as err:
            return err.messages, 422

        data = Data.query.filter_by(
            id=data['id']).delete()
        db.session.commit()

        result = data_schema.dump(Data)

        return {"status": 'success', 'data': result}, 200
