from .manga import MangaApi, MangasApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):

    #MANGA

    api.add_resource(MangasApi, '/api/v1/mangas')
    api.add_resource(MangaApi, '/api/v1/manga/<id>')

    #AUTH

    api.add_resource(SignupApi, '/api/v1/signup')
    api.add_resource(LoginApi, '/api/v1/login')


