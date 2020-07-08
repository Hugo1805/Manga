from flask import request,render_template
from flask_jwt_extended import create_access_token, decode_token
from database.models import User
from flask_restful import Resource
import datetime

from resources.errors import SchemaValidationError, InternalServerError, EmailDoesnotExistsError, BadtokenError
from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError
from services.mail_service import send_mail

class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body =  request.get_json()
            email = body.get('email')
            if not email: 
                raise SchemaValidationError
            
            user = User.objects.get(email=email)
            if not user:
                raise EmailDoesnotExistsError

            expires = datetime.timedelta(hours=24)
            reset_token = create_access_token(str(user.id),expires_delta=expires)

            return send_mail('[Manga] Reset You Password',
                            sender = 'support@manga.com',
                            recipients = [user.email],
                            text_body = render_template('email/reset_password.txt',url=url + reset_token),
                            html_body= render_template('email/reset_password.html',url=url + reset_token))
        except SchemaValidationError:
            raise SchemaValidationError
        except EmailDoesnotExistsError:
            raise EmailDoesnotExistsError
        except Exception as e:
            raise InternalServerError

class RestPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            reset_token = body.get('reset_token')
            password = body.get('password')
            if not reset_token or not password:
                raise SchemaValidationError

            user_id = decode_token(reset_token)['identity']

            user = User.objects.get(id=user_id)

            user.modify(password=password)
            user.hash_password()
            user.save()

            return send_mail('[Manga] Password reset successful',
                            sender = 'support@manga.com',
                            recipients=[user.email],
                            text_body='Password reset was successful',
                            html_body='<p>Password rest was successful</p>')
            
        except SchemaValidationError:
            raise SchemaValidationError
        except ExpiredSignatureError:
            raise ExpiredTokenError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        except Exception as e:
            raise InternalServerError