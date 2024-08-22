from app.likes.dao import DaoLikePost, DaoLikeComment, DaoBaseLike
from app.likes.errors import ThisSubjectLikedError, NoneSubjectForLikeError
from app.likes.models import LikeStatus
class LikeHandler:

    def __init__(self, dao: DaoBaseLike):
        self.dao = dao


    async def like_dislike(self, status, **data):
        data = dict(**data)
        liked_this = await self.dao.check_like(**data)
        if liked_this is None:
            try:
                await self.dao.like_dislike(status=status, **data)
            except:
                raise NoneSubjectForLikeError()
        elif liked_this.status == status:
            raise ThisSubjectLikedError()
        else:
            await self.dao.change_status(status, **data)


