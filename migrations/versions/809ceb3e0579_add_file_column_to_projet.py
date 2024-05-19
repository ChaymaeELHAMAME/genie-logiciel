"""Add file column to Projet

Revision ID: 809ceb3e0579
Revises: 1f43deb5feff
Create Date: 2023-07-04 19:20:26.651762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '809ceb3e0579'
down_revision = '1f43deb5feff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chercheur', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['passwd_che'])

    with op.batch_alter_table('expert', schema=None) as batch_op:
        batch_op.alter_column('dispo',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.create_unique_constraint(None, ['passwd_exp'])

    with op.batch_alter_table('projet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file', sa.LargeBinary(), nullable=True))
        batch_op.add_column(sa.Column('grade', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('cher_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'chercheur', ['cher_id'], ['id_che'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projet', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('cher_id')
        batch_op.drop_column('grade')
        batch_op.drop_column('file')

    with op.batch_alter_table('expert', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('dispo',
               existing_type=sa.String(length=20),
               type_=sa.BOOLEAN(),
               existing_nullable=True)

    with op.batch_alter_table('chercheur', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
