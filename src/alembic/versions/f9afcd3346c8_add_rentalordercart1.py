"""add rentalOrderCart1

Revision ID: f9afcd3346c8
Revises: 
Create Date: 2023-06-16 08:24:59.493755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9afcd3346c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_rental_order_cart',
    sa.Column('rental_orders_cart_id', sa.Integer(), nullable=False, comment='発注明細ID:自動採番'),
    sa.Column('account_id', sa.Integer(), nullable=True, comment='アカウントID'),
    sa.Column('vehicle_id', sa.Integer(), nullable=False, comment='車両ID'),
    sa.Column('option_id', sa.Integer(), nullable=True, comment='車両ID'),
    sa.Column('insurance_id', sa.Integer(), nullable=True, comment='保険ID'),
    sa.Column('status_cart', sa.Integer(), server_default=sa.text('0'), nullable=False, comment='0: giỏ hàng; 1: đã đặt'),
    sa.Column('rental_start_date', sa.DateTime(), nullable=False, comment='レンタル開始日'),
    sa.Column('rental_end_date', sa.DateTime(), nullable=False, comment='レンタル終了日'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='作成日時:プログラムでは設定しない'),
    sa.Column('created_by', sa.Integer(), nullable=True, comment='作成者'),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新日時:プログラムでは設定しない'),
    sa.Column('modified_by', sa.Integer(), nullable=True, comment='更新者'),
    sa.Column('deleted_at', sa.DateTime(), nullable=True, comment='削除日時'),
    sa.Column('deleted_by', sa.Integer(), nullable=True, comment='削除者'),
    sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('False'), nullable=False, comment='登録旗deleted: 0：消去未 ,1：消去済'),
    sa.ForeignKeyConstraint(['account_id'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['deleted_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['insurance_id'], ['m_insurances.insurance_id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['option_id'], ['m_options.option_id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['m_vehicles.vehicle_id'], ),
    sa.PrimaryKeyConstraint('rental_orders_cart_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_rental_order_cart')
    # ### end Alembic commands ###