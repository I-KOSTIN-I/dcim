from marshmallow import Schema, fields


class StatusSchema(Schema):
    rack_id = fields.Int()
    rack_name = fields.Str()
    customer_name = fields.Str()
    room_name = fields.Str()


class SizesSchema(Schema):
    room_id = fields.Int()
    rack_id = fields.Int()
    rack_max_size = fields.Int()


class CustomersSchema(Schema):
    room_id = fields.Int()
    room_name = fields.Str()
    customer_id = fields.Str()
