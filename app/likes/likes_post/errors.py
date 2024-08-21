from app.errors import BaseCustomError

class ThisPostLikedError(BaseCustomError):
    status_code = 409
    message = 'Вы уже лайкали или дизлайкали этот пост'


class NonePostForLikeError(BaseCustomError):
    status_code = 409
    message = 'Поста с таким id не существует'