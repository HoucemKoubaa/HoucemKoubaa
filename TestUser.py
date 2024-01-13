import unittest
import requests

class TestApp(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000'  # L'URL de votre application Flask en local

    def test_add_user(self):
        url = self.base_url + '/adduser'
        user_data = {
            'login': 'testuser',
            'pwd': 'testpassword',
            'nom': 'Test',
            'prenom': 'User'
        }
        response = requests.post(url, json=user_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Utilisateur ajouté avec succès")

    def test_check_user(self):
        url = self.base_url + '/checkuser'
        user_data = {
            'login': 'testuser',
            'pwd': 'testpassword'
        }
        response = requests.post(url, json=user_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['nom'], 'Test')
        self.assertEqual(response.json()['prenom'], 'User')

if __name__ == '__main__':
    unittest.main()