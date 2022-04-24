from flask_restx import Resource, Namespace
from app import models
from app.database import db
from app.schemas.racks import RackSchema
from flask import request

rack_ns = Namespace('racks')
rack_schema = RackSchema()
racks_schema = RackSchema(many=True)


@rack_ns.route('/<int:rack_id>')
class RackView(Resource):
    def get(self, rack_id):
        rack = db.session.query(models.Rack).filter(models.Rack.id == rack_id).first()

        if rack is None:
            return {}, 404

        return rack_schema.dump(rack), 200

    def put(self, rack_id):
        db.session.query(models.Rack).filter(models.Rack.id == rack_id).update(request.json)
        db.session.commit()

        return None, 204

    def delete(self, rack_id):
        db.session.query(models.Rack).filter(models.Rack.id == rack_id).delete()
        db.session.commit()

        return None, 200


@rack_ns.route('/')
class RackView(Resource):
    def get(self):
        racks = db.session.query(models.Rack).all()
        db.session.commit()

        return racks_schema.dump(racks), 200

    def post(self):
        rack = rack_schema.load(request.json)
        db.session.add(models.Rack(**rack))
        db.session.commit()

        return None, 201
