"""Added last seen and about me

Revision ID: 2f7d217c5016
Revises: 3c7dc460f7fe
Create Date: 2024-01-15 21:49:24.753100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f7d217c5016'
down_revision = '3c7dc460f7fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('about_me', sa.String(length=240), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('about_me')
        batch_op.drop_column('last_seen')

    # ### end Alembic commands ###
