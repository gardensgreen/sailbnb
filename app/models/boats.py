from .db import db
from sqlalchemy.orm import relationship
from datetime import datetime


class Boat(db.Model):
    __tablename__ = "boats"
    id = db.Column(db.Integer, primary_key=True)
    boat_type = db.Column(db.String(50), nullable=False)
    total_occupancy = db.Column(db.Integer, nullable=False)
    total_bedrooms = db.Column(db.Integer, nullable=False)
    total_bathrooms = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.String(255), nullable=False)
    has_tv = db.Column(db.Boolean, nullable=False, default=False)
    has_kitchen = db.Column(db.Boolean, nullable=False, default=False)
    has_air_con = db.Column(db.Boolean, nullable=False, default=False)
    has_internet = db.Column(db.Boolean, nullable=False, default=False)
    has_heating = db.Column(db.Boolean, nullable=False, default=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    latitude = db.Column(db.Numeric(60, 50), nullable=False)
    longitude = db.Column(db.Numeric(60, 50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    owner = relationship("User")
