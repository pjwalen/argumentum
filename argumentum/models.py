from argumentum import db


class Argument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    left_opponent = db.Column(db.Text)
    right_opponent = db.Column(db.Text)
    left_premises = db.relationship(
        'Premise',
        primaryjoin="and_(Premise.argumentid == Argument.id, Premise.side == 'left', Premise.parent == None)",
        lazy=True,
        cascade='all, delete-orphan'
    )
    right_premises = db.relationship(
        'Premise',
        primaryjoin="and_(Premise.argumentid == Argument.id, Premise.side == 'right', Premise.parent == None)",
        lazy=True,
        cascade='all, delete-orphan'
    )
    premises = db.relationship('Premise', lazy=True, cascade='all, delete-orphan')
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


class Premise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    argumentid = db.Column(db.Integer, db.ForeignKey('argument.id', ondelete='cascade'))
    argument = db.relationship('Argument', lazy=True)
    text = db.Column(db.Text)
    evidence = db.relationship('Evidence', lazy=True, cascade='all, delete-orphan')
    children = db.relationship('Premise', lazy=True, cascade='all, delete-orphan')
    parent = db.Column(db.Integer, db.ForeignKey('premise.id', ondelete='cascade'), default=None)
    opponent = db.Column(db.Text)
    side = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


class Evidence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    premiseid = db.Column(db.Integer, db.ForeignKey('premise.id'))
    text = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
