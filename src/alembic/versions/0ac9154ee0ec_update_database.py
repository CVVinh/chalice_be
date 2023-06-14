"""update database

Revision ID: 0ac9154ee0ec
Revises: 
Create Date: 2023-06-14 14:33:29.591907

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0ac9154ee0ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('m_insurances', sa.Column('insurance_value', sa.Float(), nullable=True, comment='Giá bảo hiểm'))
    op.drop_column('m_insurances', 'vehicle_value')
    op.add_column('m_options', sa.Column('option_value', sa.Float(), nullable=True, comment='Giá option'))
    op.drop_column('m_options', 'vehicle_value')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('m_options', sa.Column('vehicle_value', mysql.FLOAT(), nullable=True, comment='Giá option'))
    op.drop_column('m_options', 'option_value')
    op.add_column('m_insurances', sa.Column('vehicle_value', mysql.FLOAT(), nullable=True, comment='Giá bảo hiểm'))
    op.drop_column('m_insurances', 'insurance_value')
    # ### end Alembic commands ###