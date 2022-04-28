from marshmallow import Schema, fields


class FirstSchema(Schema):
    answer = fields.Int()


class SecondSchema(Schema):
    answer = fields.Int()


class ThirdSchema(Schema):
    answer = fields.Int()


class FourthSchema(Schema):
    answer = fields.Int()
