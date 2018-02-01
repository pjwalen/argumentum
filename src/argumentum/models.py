from argumentum import db


class Argument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    left_opponent = db.Column(db.Text)
    right_opponent = db.Column(db.Text)
    left_premises = db.relationship(
        'Premise',
        primaryjoin="and_(Premise.argumentid == Argument.id, Premise.opponent == 'left', Premise.parent == None)",
        lazy=True
    )
    right_premises = db.relationship(
        'Premise',
        primaryjoin="and_(Premise.argumentid == Argument.id, Premise.opponent == 'right')",
        lazy=True
    )
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


class Premise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    argumentid = db.Column(db.Integer, db.ForeignKey('argument.id'))
    text = db.Column(db.Text)
    evidence = db.relationship('Evidence', lazy=True)
    children = db.relationship('Premise', lazy=True)
    parent = db.Column(db.Integer, db.ForeignKey('premise.id'), default=None)
    opponent = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


class Evidence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    premiseid = db.Column(db.Integer, db.ForeignKey('premise.id'))
    text = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
