from app.errors import BaseCustomError

class ThisPostLikedError(BaseCustomError):
    status_code = 409
    message = 'Вы уже лайкали этот пост'