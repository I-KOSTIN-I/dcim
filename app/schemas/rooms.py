from marshmallow import Schema, fields


class RoomSchema(Schema):
    id = fields.Int()
    name = fields.Str()