import datetime
from argumentum import db
from argumentum.models import Argument, Premise, Evidence


def create_demo_data():
    # Define an argument.
    argument = Argument(
        title='My first argument',
        left_opponent='Patrick Walentiny',
        right_opponent='Matt Byrne',
        description='This is a default argument to demonstrate the applications features.',
        created=datetime.datetime.now(),
        updated=datetime.datetime.now()
    )
    db.session.add(argument)
    db.session.commit()

    # Define premises.
    left_premise = Premise(
        argumentid=argument.id,
        opponent='left',
        side='left',
        text='This is a demonstration argument.',
        created=datetime.datetime.now(),
        updated=datetime.datetime.now()
    )
    right_premise = Premise(
        argumentid=argument.id,
        opponent='right',
        side='right',
        text='This is a demonstration argument.',
        created=datetime.datetime.now(),
        updated=datetime.datetime.now()
    )
    db.session.add(left_premise)
    db.session.add(right_premise)
    db.session.commit()

    # Define a sub-premise under the left-top premise.
    sub_premise = Premise(
        argumentid=argument.id,
        parent=left_premise.id,
        side='left',
        text='This is a demonstration argument.',
        created=datetime.datetime.now(),
        updated=datetime.datetime.now()
    )
    db.session.add(sub_premise)
    db.session.commit()

    # Add evidence to each premise.
    left_evidence = Evidence(
        premiseid=left_premise.id,
        text='This is some evidence',
        created=datetime.datetime.now(),
        updated=datetime.datetime.now()
    )
    right_evidence = Evidence(
        premiseid=right_premise.id,
        text='This is some evidence',
        created=datetime.datetime.now(),
        updated=datetime.datetime.now()
    )
    sub_evidence = Evidence(
        premiseid=sub_premise.id,
        text='This is some evidence',
        created=datetime.datetime.now(),
        updated=datetime.datetime.now()
    )
    db.session.add(left_evidence)
    db.session.add(right_evidence)
    db.session.add(sub_evidence)
    db.session.commit()
