from app.database import db


class Rack(db.Model):
    __tablename__ = 'rack'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    size = db.Column(db.Integer)
    state = db.Column(db.String(255))
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    customer = db.relationship("Customer")
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))
    room = db.relationship("Room")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'size': self.size,
            'state': self.state,
            'customer_id': self.customer_id,
            'room_id': self.room_id
        }


class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
