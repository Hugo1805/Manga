from flask import Response,request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Manga, User
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, \
    NotUniqueError,DoesNotExist,ValidationError,InvalidQueryError

from resources.errors import SchemaValidationError, MangaAlreadyExistsError, \
    InternalServerError, UpdatingMangaError, DeletingMangaError, MangaNotExistsError

class MangasApi(Resource):

    def get(self):
        mangas = Manga.objects().to_json()
        return Response(mangas, mimetype="applicatin/json",status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user =  User.objects.get(id=user_id)
            manga = Manga(**body,added_by=user)
            manga.save()
            user.update(push__manga=manga)
            user.save()
            id = manga.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise MangaAlreadyExistsError
        except Exception as e:
            raise InternalServerError
        
class MangaApi(Resource):

    @jwt_required
    def put(self,id):
        try:
            user_id = get_jwt_identity()
            manga = Manga.objects.get(id=id,added_by=user_id)
            body = request.get_json()
            Manga.objects.get(id=id).update(**body)
            return {'msg':'updated'}, 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingMangaError
        except Exception:
            raise InternalServerError
        

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            manga = Manga.objects.get(id=id,added_by=user_id)
            manga.delete()
            return {'msg':'deleted'}, 200
        except DoesNotExist:
            raise DeletingMangaError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            mangas = Manga.objects().get(id=id).to_json()
            return Response(mangas, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MangaAlreadyExistsError
        except Exception:
            raise InternalServerError