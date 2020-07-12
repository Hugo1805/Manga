import json

from tests.BaseCase import BaseCase

class TestCreateManga(BaseCase):

    def test_create_manga_successful(self):
        # Given
        email = "test4@gmail.com"
        password = "mycoolpassword"
        payload = json.dumps({
            "email" : email,
            "password" : password
        })

        self.app.post('/api/v1/auth/signup', headers={"Content-Type":"application/json"}, data=payload)
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type":"application/json"}, data=payload)
        login_token = response.json['token']
        
        manga_payload = {
            "name" : "Manga 01 test",
            "description" :"Test Test Test"
        }

        # When

        response = self.app.post('/api/v1/mangas', 
        headers={"Content-Type": "application/json","Authorization":f"Bearer {login_token}"},
        data=json.dumps(manga_payload))

        # Then

        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
        