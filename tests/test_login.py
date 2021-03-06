import  json

from tests.BaseCase import BaseCase

class TestUserLogin(BaseCase):
    def test_successsful_login(self):
        # Given
        email = "test2@gmail.com"
        password = "mycoolpassword"
        payload = json.dumps({
            "email":email,
            "password" : password
        })
        response = self.app.post('/api/v1/auth/signup', headers={"Content-Type":"application/json"}, data=payload)

        # When
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type":"application/json"}, data=payload)

        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)
