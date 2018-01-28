from argumentum import db


class Argument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    left_opponent = db.Column(db.Text)
    right_opponent = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


class Premise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    argumentid = db.Column(db.Integer, db.ForeignKey('argument.id'))
    contents = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


class Rebuttal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    premiseid = db.Column(db.Integer, db.ForeignKey('premise.id'))
    contents = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
