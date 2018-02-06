import unittest
from argumentum import application, db
from argumentum.models import Evidence
from tests.utils import create_argument, create_evidence, create_premise


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        db.create_all()
        argumentid = create_argument()
        self.premiseid = create_premise(argumentid=argumentid)
        self.evidenceid = create_evidence(premiseid=self.premiseid)
        application.config['WTF_CSRF_ENABLED'] = False
        self.app = application.test_client()

    def tearDown(self):
        db.drop_all()

    def test_evidence_create(self):
        self.app.post(
            '/evidence',
            data=dict(
                premiseid=self.premiseid,
                text='This is evidence'
            )
        )
        self.assertEqual(Evidence.query.count(), 2)

    def test_evidence_delete(self):
        self.app.post(
            '/evidence/delete',
            data=dict(
                evidenceid=self.evidenceid
            )
        )
        self.assertEqual(Evidence.query.count(), 0)

    def test_evidence_update(self):
        new_text = 'New evidence text'
        self.app.post(
            '/evidence/update',
            data=dict(
                argumentid=self.evidenceid,
                text=new_text
            )
        )
        evidence = Evidence.query.filter(id=self.evidenceid).one()
        self.assertEqual(new_text, evidence.text)
