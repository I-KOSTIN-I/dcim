from sql_functions import search_by_status, search_by_customers, search_by_size
from flask_restx import Resource, Namespace
from app.schemas.sql import StatusSchema, CustomersSchema, SizesSchema


sql_ns = Namespace('sql_search')
status_schema = StatusSchema(many=True)
customers_schema = CustomersSchema(many=True)
size_schema = SizesSchema(many=True)


@sql_ns.route('/status/')
class SqlView(Resource):
    def get(self):
        status_data = search_by_status()

        return status_schema.dump(status_data), 200


@sql_ns.route('/customers/')
class SqlView(Resource):
    def get(self):
        customers_data = search_by_customers()

        return customers_schema.dump(customers_data), 200


@sql_ns.route('/size/')
class SqlView(Resource):
    def get(self):
        size_data = search_by_size()

        return size_schema.dump(size_data), 200
