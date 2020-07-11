import json

from tests.BaseCase import BaseCase

class SingupTest(BaseCase):

    def test_successful_singup(self):
        # Given
        email = "test1@gmail.com"
        password = "mycoolpassword"
        payload = json.dumps({
            "email": email,
            "password": password
        })

        # When
        response = self.app.post('/api/v1/auth/signup', headers={"Content-Type":"application/json"}, data=payload)
        
        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200,response.status_code)
        
