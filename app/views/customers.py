from flask_restx import Resource, Namespace
from app import models
from app.database import db
from app.schemas.customers import CustomerSchema
from flask import request

customer_ns = Namespace('customers')
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


@customer_ns.route('/<int:customer_id>')
class CustomerView(Resource):
    def get(self, customer_id):
        customer = db.session.query(models.Customer).filter(models.Customer.id == customer_id).first()

        if customer is None:
            return {}, 404

        return customer_schema.dump(customer), 200

    def put(self, customer_id):
        db.session.query(models.Customer).filter(models.Customer.id == customer_id).update(request.json)
        db.session.commit()

        return None, 204

    def delete(self, customer_id):
        db.session.query(models.Customer).filter(models.Customer.id == customer_id).delete()
        db.session.commit()

        return None, 200


@customer_ns.route('/')
class CustomerView(Resource):
    def get(self):
        customers = db.session.query(models.Customer).all()
        db.session.commit()

        return customers_schema.dump(customers), 200

    def post(self):
        customer = customer_schema.load(request.json)
        db.session.add(models.Customer(**customer))
        db.session.commit()

        return None, 201
