from fastapi import HTTPException


class ThereIsAUserError(Exception):
    message = "Такой пользователь уже есть"
    @classmethod
    def fast_api_exception(cls):
        raise HTTPException(status_code=409, detail=cls.message)


class ValidationError(Exception):
    message = "Не правильно введены данные"

    @classmethod
    def fast_api_exception(cls):
        raise HTTPException(status_code=409, detail=cls.message)

