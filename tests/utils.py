import datetime
from argumentum import db
from argumentum.models import Argument, Evidence, Premise


def create_argument(title='This is an argument',
                    description='This is the argument\'s description.',
                    left_opponent='Lefty',
                    right_opponent='Righty'):
    argument = Argument()
    argument.title = title
    argument.description = description
    argument.left_opponent = left_opponent
    argument.right_opponent = right_opponent
    argument.created = datetime.datetime.now()
    argument.updated = datetime.datetime.now()
    db.session.add(argument)
    db.session.commit()
    return argument.id


def create_evidence(premiseid=1,
                    text='This is evidence'):
    evidence = Evidence()
    evidence.premiseid = premiseid
    evidence.text = text
    evidence.created = datetime.datetime.now()
    evidence.updated = datetime.datetime.now()
    db.session.add(evidence)
    db.session.commit()
    return evidence.id


def create_premise(argumentid=1,
                   text='This is evidence'):
    premise = Premise()
    premise.argumentid = argumentid
    premise.text = text
    premise.created = datetime.datetime.now()
    premise.updated = datetime.datetime.now()
    db.session.add(premise)
    db.session.commit()
    return premise.id
