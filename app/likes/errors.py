from app.errors import BaseCustomError

class ThisSubjectLikedError(BaseCustomError):
    status_code = 409
    message = 'Вы уже лайкали или дизлайкали'


class NoneSubjectForLikeError(BaseCustomError):
    status_code = 409
    message = 'Объекта с таким id не существует'