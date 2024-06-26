"""Initial migration

Revision ID: b59b07233d85
Revises: 47c3604dfcb8
Create Date: 2023-07-05 02:04:24.114498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b59b07233d85'
down_revision = '47c3604dfcb8'
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
        batch_op.add_column(sa.Column('fk_projet_cher_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'chercheur', ['fk_projet_cher_id'], ['id_che'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projet', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fk_projet_cher_id')
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
