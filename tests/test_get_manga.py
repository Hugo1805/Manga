    # import unittest
    # import json

    # from tests.BaseCase import BaseCase

    # class TestGetManga(BaseCase):
    
    # def test_empty_response(self):
    #     response = self.app.get('/api/v1/mangas')
    #     self.assertListEqual(response,[])
    #     self.assertEqual(response.status_code, 200)
    
    # def test_manga_response(self):
    #     # Given
    #     email = "test5@gmail.com"
    #     password = "mycoolpassword"
    #     user_payload = json.dumps({
    #         "email": email,
    #         "password": password
    #     })

    #     response = self.app.post('/api/v1/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
    #     user_id = response.json['id']
    #     print('user_id:',user_id)

    #     response = self.app.post('/api/v1/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
    #     login_token = response.json['token']
    #     print('login_token:',login_token)

    #     manga_payload = {
    #         "name" : "Manga",
    #         "description" :"Test"
    #     }

    #     response = self.app.post('/api/v1/mangas', 
    #     headers={"Content-Type": "application/json","Authorization": f"Bearer {login_token}"},
    #     data=json.dumps(manga_payload))
    #     id_manga = response.json['id']
    #     print('id_manga:', id_manga)

    #     # When
    #     response = self.app.get('/api/v1/mangas')
    #     added_manga = response.json[0]
    #     print("added_manga: ",added_manga)

    #     Then
    #     self.assertEqual(manga_payload['name'], added_manga['name'])
    #     self.assertEqual(manga_payload['description'], added_manga['description'])
    #     self.assertEqual(user_id, added_manga['added_by']['$oid'])
    #     self.assertEqual(200, response.status_code)

