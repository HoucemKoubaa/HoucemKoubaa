import unittest
import sqlite3
from app import app

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = sqlite3.connect('tp_cicd.db')
        self.cursor = self.db.cursor()

    def tearDown(self):
        self.db.close()

    def test_add_user(self):
        data = {'login': 'user1', 'pwd': 'password1', 'nom': 'nom1', 'prenom': 'prenom1'}
        response = self.app.post('/adduser', json=data)
        self.assertEqual(response.status_code, 201)

    def test_check_user(self):
        data = {'login': 'user1', 'pwd': 'password1'}
        response = self.app.post('/checkuser', json=data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['nom'], 'nom1')
        self.assertEqual(data['prenom'], 'prenom1')

if __name__ == '__main__':
    unittest.main()