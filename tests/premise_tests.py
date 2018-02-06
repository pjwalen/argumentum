import unittest
from argumentum import application, db
from argumentum.models import Premise, Evidence
from tests.utils import create_argument, create_evidence, create_premise


class PremiseTests(unittest.TestCase):
    def setUp(self):
        db.create_all()
        self.argumentid = create_argument()
        premiseid = create_premise(argumentid=self.argumentid)
        create_evidence(premiseid=premiseid)
        application.config['WTF_CSRF_ENABLED'] = False
        self.app = application.test_client()

    def tearDown(self):
        db.drop_all()

    def test_premise_create(self):
        self.app.post(
            '/premise',
            data=dict(
                argumentid=self.argumentid,
                opponent='left',
                text='Premise text'
            )
        )
        self.assertEqual(Premise.query.count(), 2)

    def test_premise_delete(self):
        self.app.post(
            '/premise/delete',
            data=dict(
                premiseid=1
            )
        )
        # When you delete a premise, it should delete all of its children as well.
        self.assertEqual(Evidence.query.count(), 0)
        self.assertEqual(Premise.query.count(), 0)

    def test_premise_update(self):
        new_text = 'New premise text'
        self.app.post(
            '/premise/update',
            data=dict(
                argumentid=self.premiseid,
                text=new_text
            )
        )
        premise = Premise.query.filter(id=self.premiseid).one()
        self.assertEqual(new_text, premise.text)
