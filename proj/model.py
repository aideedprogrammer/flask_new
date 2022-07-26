import uuid
from flask import json
from proj import db


class User(db.Model):
    uuid = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(32))
    date_birth = db.Column(db.DateTime)

    def __init__(self, name):
        self.uuid = uuid.uuid4().hex
        self.name = name
