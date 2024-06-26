"""empty message

Revision ID: f7ca906ccba7
Revises: ebdcfe313e8c
Create Date: 2023-07-03 22:34:57.278426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7ca906ccba7'
down_revision = 'ebdcfe313e8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chercheur', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prj_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(None, ['passwd_che'])
        batch_op.create_foreign_key(None, 'projet', ['prj_id'], ['id_prj'])

    with op.batch_alter_table('expert', schema=None) as batch_op:
        batch_op.alter_column('dispo',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.create_unique_constraint(None, ['passwd_exp'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expert', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('dispo',
               existing_type=sa.String(length=20),
               type_=sa.BOOLEAN(),
               existing_nullable=True)

    with op.batch_alter_table('chercheur', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('prj_id')

    # ### end Alembic commands ###
