import datetime
import unittest
from argumentum import application, db
from argumentum.models import Argument, Premise, Evidence
from tests.utils import create_argument, create_evidence, create_premise


class ArgumentumTests(unittest.TestCase):
    def setUp(self):
        db.create_all()
        self.argumentid = create_argument()
        premiseid = create_premise(argumentid=self.argumentid)
        create_evidence(premiseid=premiseid)
        application.config['WTF_CSRF_ENABLED'] = False
        self.app = application.test_client()

    def tearDown(self):
        db.drop_all()

    def test_argument_create(self):
        self.app.post(
            '/argument',
            data=dict(
                title='This is an argument',
                description='Argument description',
                left_opponent='Lefty',
                right_opponent='Righty'
            )
        )
        self.assertEqual(Argument.query.count(), 2)

    def test_argument_delete(self):
        self.app.post(
            '/argument/delete',
            data=dict(
                argumentid=self.argumentid
            )
        )
        # When you delete an argument, it should delete all of its children as well.
        self.assertEqual(0, Argument.query.count())
        self.assertEqual(0, Premise.query.count())
        self.assertEqual(0, Evidence.query.count())

    def test_argument_update(self):
        new_title = 'New argument title'
        new_description = 'This is the new description.'
        new_left_opponent = 'New Left'
        new_right_opponent = 'New Right'
        old_updated_datetime = Argument.query.get(self.argumentid).updated
        self.app.post(
            '/argument/update',
            data=dict(
                argumentid=self.argumentid,
                title=new_title,
                description=new_description,
                left_opponent=new_left_opponent,
                right_opponent=new_right_opponent
            )
        )
        argument = Argument.query.get(self.argumentid)
        self.assertEqual(new_title, argument.title)
        self.assertEqual(new_description, argument.description)
        self.assertEqual(new_left_opponent, argument.left_opponent)
        self.assertEqual(new_right_opponent, argument.right_opponent)
        self.assertGreater(argument.updated, old_updated_datetime)
