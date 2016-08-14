"""empty message

Revision ID: 9be9077d8fce
Revises: c5fe28ec7139
Create Date: 2016-08-13 12:46:13.985575

"""

# revision identifiers, used by Alembic.
revision = '9be9077d8fce'
down_revision = 'c5fe28ec7139'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('call_for_papers', 'privacy',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('call_for_papers', 'timezone',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('events', sa.Column('thumbnail', sa.String(), nullable=True))
    op.add_column('events_version', sa.Column('thumbnail', sa.String(), autoincrement=False, nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'thumbnail')
    op.drop_column('events', 'thumbnail')
    op.alter_column('call_for_papers', 'timezone',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('call_for_papers', 'privacy',
               existing_type=sa.VARCHAR(),
               nullable=True)
    ### end Alembic commands ###
