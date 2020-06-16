class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class MangaAlreadyExistsError(Exception):
    pass

class UpdatingMangaError(Exception):
    pass

class DeletingMangaError(Exception):
    pass

class MangaNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError":{
        "message":  "Something went worng",
        "status": 500
    },
    "SchemaValidationError":{
        "message": "Request is missing required fields",
        "status": 400
    },
    "MangaAlreadyExistsError":{
        "message":"Manga with given name already exists",
        "status": 400
    },
    "UpdatingMangaError":{
        "message" : "Updating manga added by other is forbidden",
        "status": 403
    },
    "DeletingMangaError":{
        "message": "Deleting manga added by other is forbidden",
        "status": 403
    },
    "MangaNotExistsError":{
        "message":"Movie with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError":{
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError":{
        "message": "Invalid username or password",
        "status": 401
    }
}