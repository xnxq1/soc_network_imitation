from select import select
from sqlalchemy import select, func, update
from app.db import async_session_factory
from app.likes.models import LikePost
from app.posts.models import Post
from sqlalchemy import bindparam, column


async def count_like(main_model, like_model, target_column: str, status: str):
    async with async_session_factory() as session:
        query_like = (select(column(target_column), func.count())
                      .select_from(like_model)
                      .where(like_model.status == status)
                      .group_by(column(target_column)))
        update_tuples = await session.execute(query_like)
        case_statements = [{'id': sub_id, f'{status}s': count} for sub_id, count in update_tuples]
        if len(case_statements) > 0:
            await session.execute(update(main_model), case_statements, execution_options={'synchronize_session':None})

            await session.commit()