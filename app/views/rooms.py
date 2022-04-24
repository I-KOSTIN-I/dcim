from flask_restx import Resource, Namespace
from app import models
from app.database import db
from app.schemas.rooms import RoomSchema
from flask import request

room_ns = Namespace('rooms')
room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True)


@room_ns.route('/<int:room_id>')
class RackView(Resource):
    def get(self, room_id):
        room = db.session.query(models.Room).filter(models.Room.id == room_id).first()

        if room is None:
            return {}, 404

        return room_schema.dump(room), 200

    def put(self, room_id):
        db.session.query(models.Room).filter(models.Room.id == room_id).update(request.json)
        db.session.commit()

        return None, 204

    def delete(self, room_id):
        db.session.query(models.Room).filter(models.Room.id == room_id).delete()
        db.session.commit()

        return None, 200


@room_ns.route('/')
class RoomView(Resource):
    def get(self):
        rooms = db.session.query(models.Room).all()
        db.session.commit()

        return rooms_schema.dump(rooms), 200

    def post(self):
        room = room_schema.load(request.json)
        db.session.add(models.Room(**room))
        db.session.commit()

        return None, 201
