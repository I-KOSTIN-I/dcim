from math_functions import first_function, second_function, third_function, fourth_function
from flask_restx import Resource, Namespace
from app.schemas.math import FirstSchema, SecondSchema, ThirdSchema, FourthSchema


math_ns = Namespace('math_functions')
first_schema = FirstSchema()
second_schema = SecondSchema()
third_schema = ThirdSchema()
fourth_schema = FourthSchema()


@math_ns.route('/first/')
class MathView(Resource):
    def get(self):
        data = first_function(5, 4, 3, 2, 9, 10)
        result = {"answer": data}

        return first_schema.dump(result), 200


@math_ns.route('/second/')
class MathView(Resource):
    def get(self):
        data = second_function(6, 1, 2, 4)
        result = {"answer": data}

        return second_schema.dump(result), 200


@math_ns.route('/third/')
class MathView(Resource):
    def get(self):
        data = third_function(5, 7, 9, 17, 12)
        result = {"answer": data}

        return third_schema.dump(result), 200
    
    
@math_ns.route('/fourth/')
class MathView(Resource):
    def get(self):
        data = fourth_function(4, 8, 15, 16, 23, 42)
        result = {"answer": data}

        return fourth_schema.dump(result), 200

