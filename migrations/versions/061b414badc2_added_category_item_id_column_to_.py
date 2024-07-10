"""added category item id column to Expense model

Revision ID: 061b414badc2
Revises: 28ab8d2c9ad1
Create Date: 2024-07-08 13:27:32.061801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '061b414badc2'
down_revision = '28ab8d2c9ad1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expenses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_item_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_expenses_category_item_id', 'expense_category_items', ['category_item_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expenses', schema=None) as batch_op:
        batch_op.drop_constraint('fk_expenses_category_item_id', type_='foreignkey')
        batch_op.drop_column('category_item_id')

    # ### end Alembic commands ###