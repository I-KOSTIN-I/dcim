import os

DATA_BASE_PATH = os.path.join('dcim.db')
FIXTURE_DIR = os.path.join('app', 'fixtures')


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATA_BASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CUSTOMER_FIXTURE_PATH = os.path.join(FIXTURE_DIR, 'customer.json')
    RACK_FIXTURE_PATH = os.path.join(FIXTURE_DIR, 'rack.json')
    ROOM_FIXTURE_PATH = os.path.join(FIXTURE_DIR, 'room.json')