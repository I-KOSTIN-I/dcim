from marshmallow import Schema, fields


class RackSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    size = fields.Int()
    state = fields.Str()
    customer_id = fields.Int()
    room_id = fields.Int()
