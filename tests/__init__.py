import unittest
from argumentum import application, db


class ArgumentumTests(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_argumentum(self):
        self.assertEqual(1, 1)
