from flask import Flask
from flask_restx import Api
from app.config import Config
from app.database import db
from app.views import customers, racks, rooms, sql, math


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    with app.app_context():

        db.create_all()

        from app import migration

        migration.migrate_customers(app.config['CUSTOMER_FIXTURE_PATH'])
        migration.migrate_racks(app.config['RACK_FIXTURE_PATH'])
        migration.migrate_rooms(app.config['ROOM_FIXTURE_PATH'])

    api = Api(app)
    api.add_namespace(customers.customer_ns)
    api.add_namespace(racks.rack_ns)
    api.add_namespace(rooms.room_ns)
    api.add_namespace(sql.sql_ns)
    api.add_namespace(math.math_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run(debug=True)
