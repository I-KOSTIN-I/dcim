from marshmallow import Schema, fields


class CustomerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
