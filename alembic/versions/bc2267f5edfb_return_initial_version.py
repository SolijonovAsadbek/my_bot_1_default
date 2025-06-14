"""return initial version

Revision ID: bc2267f5edfb
Revises: cc938f681f61
Create Date: 2025-05-31 16:48:30.451784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc2267f5edfb'
down_revision: Union[str, None] = 'cc938f681f61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint(op.f('post_user_fkey'), 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'users', ['user_id'], ['id'])
    op.drop_column('post', 'user')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key(op.f('post_user_fkey'), 'post', 'users', ['user'], ['id'])
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###
