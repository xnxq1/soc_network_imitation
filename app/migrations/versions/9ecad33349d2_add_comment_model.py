"""Add comment model

Revision ID: 9ecad33349d2
Revises: 72f321b09b42
Create Date: 2024-08-21 18:53:50.174538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ecad33349d2'
down_revision: Union[str, None] = '72f321b09b42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Comment',
    sa.Column('comment_parent_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('dislikes', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['comment_parent_id'], ['Comment.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['Post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint('post_user_uc', 'LikePost', ['post_id', 'user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('post_user_uc', 'LikePost', type_='unique')
    op.drop_table('Comment')
    # ### end Alembic commands ###
