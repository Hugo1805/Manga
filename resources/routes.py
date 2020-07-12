from manga import MangaApi, MangasApi
from auth import SignupApi, LoginApi
from reset_password import ForgotPassword, RestPassword

def initialize_routes(api):

    #MANGA

    api.add_resource(MangasApi, '/api/v1/mangas')
    api.add_resource(MangaApi, '/api/v1/manga/<id>')

    #AUTH

    api.add_resource(SignupApi, '/api/v1/auth/signup')
    api.add_resource(LoginApi, '/api/v1/auth/login')

    #MAIL
    
    api.add_resource(ForgotPassword, '/api/v1/forgot')
    api.add_resource(RestPassword, '/api/v1/reset')



