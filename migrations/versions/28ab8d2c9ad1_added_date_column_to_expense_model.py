"""added date column to Expense model

Revision ID: 28ab8d2c9ad1
Revises: e5707ea96268
Create Date: 2024-07-08 13:24:20.442463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28ab8d2c9ad1'
down_revision = 'e5707ea96268'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expenses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.Date(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expenses', schema=None) as batch_op:
        batch_op.drop_column('date')

    # ### end Alembic commands ###
