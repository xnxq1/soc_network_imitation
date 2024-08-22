from app.errors import BaseCustomError


class NoneCommentError(BaseCustomError):
    message = 'Такого комментария не существует'
    status_code = 409