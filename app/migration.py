import json
import os
from app.database import db
from app import models


def load_fixture(file_path):
    """
    Загружает данные из фикстуры
    :param file_path:
    :return:
    """
    data = []
    if os.path.isfile(file_path):
        with open(file_path) as file:
            data = json.load(file)

    return data


def migrate_racks(fixture_path):
    fixture_data = load_fixture(fixture_path)

    for rack in fixture_data:

        if db.session.query(models.Rack).filter(models.Rack.id == rack['id']).first() is None:
            new_rack = models.Rack(**rack)
            db.session.add(new_rack)

    db.session.commit()


def migrate_rooms(fixture_path):
    fixture_data = load_fixture(fixture_path)

    for room in fixture_data:

        if db.session.query(models.Room).filter(models.Room.id == room['id']).first() is None:
            new_room = models.Room(**room)
            db.session.add(new_room)

    db.session.commit()


def migrate_customers(fixture_path):
    fixture_data = load_fixture(fixture_path)

    for customer in fixture_data:

        if db.session.query(models.Customer).filter(models.Customer.id == customer['id']).first() is None:
            new_customer = models.Customer(**customer)
            db.session.add(new_customer)

    db.session.commit()




#print(load_fixture(Config.RACK_FIXTURE_PATH))
#print(migrate_racks(load_fixture(n))
#print(load_fixture(Config.ROOM_FIXTURE_PATH))