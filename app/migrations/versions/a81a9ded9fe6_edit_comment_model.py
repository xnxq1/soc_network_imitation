"""Edit comment model

Revision ID: a81a9ded9fe6
Revises: 9ecad33349d2
Create Date: 2024-08-21 19:01:15.663405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a81a9ded9fe6'
down_revision: Union[str, None] = '9ecad33349d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CommentToPost',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('dislikes', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Post.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('CommentToComment',
    sa.Column('comment_parent_id', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('dislikes', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['comment_parent_id'], ['CommentToPost.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Comment')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Comment',
    sa.Column('comment_parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('dislikes', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['comment_parent_id'], ['Comment.id'], name='Comment_comment_parent_id_fkey'),
    sa.ForeignKeyConstraint(['post_id'], ['Post.id'], name='Comment_post_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Comment_pkey')
    )
    op.drop_table('CommentToComment')
    op.drop_table('CommentToPost')
    # ### end Alembic commands ###
