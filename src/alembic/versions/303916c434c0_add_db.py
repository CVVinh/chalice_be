"""add_db

Revision ID: 303916c434c0
Revises: 
Create Date: 2023-06-15 00:56:40.358627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '303916c434c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('m_accounts',
    sa.Column('account_id', sa.Integer(), nullable=False, comment='アカウントID'),
    sa.Column('account_cd', sa.String(length=100), nullable=True, comment='アカウントコード:社員番号など利用企業のIDやコードのため'),
    sa.Column('ext_account_id', sa.Integer(), nullable=True, comment='外部アカウントID:cognitoなどの外部認証サービスと連携する場合は設定'),
    sa.Column('account_name', sa.String(length=100), nullable=True, comment='アカウント名'),
    sa.Column('email_address', sa.String(length=100), nullable=True, comment='メールアドレス'),
    sa.Column('account_status', sa.Integer(), server_default=sa.text('0'), nullable=False, comment='ステータス:0：仮登録、1：本登録、2：削除'),
    sa.Column('is_system_manager', sa.Boolean(), server_default=sa.text('False'), nullable=False, comment='システム管理フラグ:アプリケーションで設定/更新しないこと'),
    sa.Column('version', sa.Integer(), server_default=sa.text('1'), nullable=False, comment='バージョン:楽観的排他で利用'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='作成日時:プログラムでは設定しない'),
    sa.Column('created_by', sa.String(length=200), nullable=True, comment='作成処理:プログラムで設定、API名、関数名'),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新日時:プログラムでは設定しない'),
    sa.Column('modified_by', sa.String(length=200), nullable=True, comment='更新処理:プログラムで設定、API名、関数名'),
    sa.Column('deleted_at', sa.DateTime(), nullable=True, comment='削除日時'),
    sa.Column('deleted_by', sa.String(length=200), nullable=True, comment='削除'),
    sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('False'), nullable=False, comment='登録旗deleted: 0：消去未 ,1：消去済'),
    sa.PrimaryKeyConstraint('account_id')
    )
    op.create_table('m_insurances',
    sa.Column('insurance_id', sa.Integer(), nullable=False, comment='保険ID'),
    sa.Column('insurance_name', sa.String(length=200), nullable=True, comment='名前保険'),
    sa.Column('insurance_value', sa.Float(), nullable=True, comment='Giá bảo hiểm'),
    sa.PrimaryKeyConstraint('insurance_id')
    )
    op.create_table('m_makers',
    sa.Column('maker_id', sa.Integer(), nullable=False, comment='メーカーID'),
    sa.Column('maker_name', sa.String(length=200), nullable=True, comment='名前メーカー'),
    sa.PrimaryKeyConstraint('maker_id')
    )
    op.create_table('m_models',
    sa.Column('model_id', sa.Integer(), nullable=False, comment='モデルID'),
    sa.Column('model_name', sa.String(length=200), nullable=True, comment='名前モデル'),
    sa.PrimaryKeyConstraint('model_id')
    )
    op.create_table('m_options',
    sa.Column('option_id', sa.Integer(), nullable=False, comment='オプションID'),
    sa.Column('option_name', sa.String(length=200), nullable=True, comment='名前オプション'),
    sa.Column('option_value', sa.Float(), nullable=True, comment='Giá option'),
    sa.PrimaryKeyConstraint('option_id')
    )
    op.create_table('m_payment_methods',
    sa.Column('payment_method_id', sa.Integer(), nullable=False, comment='お支払い方法ID'),
    sa.Column('payment_method_name', sa.String(length=200), nullable=True, comment='名前お支払い方法'),
    sa.PrimaryKeyConstraint('payment_method_id')
    )
    op.create_table('m_prefecture',
    sa.Column('pref_id', sa.Integer(), nullable=False, comment='県ID'),
    sa.Column('pref_name', sa.String(length=200), nullable=True, comment='名前県'),
    sa.PrimaryKeyConstraint('pref_id')
    )
    op.create_table('m_stores',
    sa.Column('store_id', sa.Integer(), nullable=False, comment='売上ID'),
    sa.Column('store_name', sa.String(length=200), nullable=True, comment='名前売上'),
    sa.PrimaryKeyConstraint('store_id')
    )
    op.create_table('m_base',
    sa.Column('base_id', sa.Integer(), nullable=False, comment='拠点ID'),
    sa.Column('base_cd', sa.String(length=200), nullable=True, comment='拠点コード'),
    sa.Column('base_name', sa.String(length=200), nullable=True, comment='拠点名'),
    sa.Column('zip_code', sa.String(length=10), nullable=True, comment='郵便番号'),
    sa.Column('pref_code', sa.Integer(), nullable=False, comment='都道府県コード'),
    sa.Column('address', sa.String(length=400), nullable=True, comment='住所'),
    sa.Column('addressee', sa.String(length=200), nullable=True, comment='受取名:配送や郵送時の受信名'),
    sa.Column('telephone_number', sa.String(length=200), nullable=True, comment='電話番号'),
    sa.Column('fax_number', sa.String(length=200), nullable=True, comment='FAX番号'),
    sa.Column('e_mail_address', sa.String(length=200), nullable=True, comment='メールアドレス'),
    sa.Column('note', sa.Text(), nullable=True, comment='備考'),
    sa.Column('version', sa.Integer(), server_default=sa.text('1'), nullable=False, comment='バージョン:楽観的排他で利用'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='作成日時:プログラムでは設定しない'),
    sa.Column('created_by', sa.Integer(), nullable=True, comment='作成処理:プログラムで設定、API名、関数名'),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新日時:プログラムでは設定しない'),
    sa.Column('modified_by', sa.Integer(), nullable=True, comment='更新処理:プログラムで設定、API名、関数名'),
    sa.Column('deleted_at', sa.DateTime(), nullable=True, comment='削除日時'),
    sa.Column('deleted_by', sa.Integer(), nullable=True, comment='削除者'),
    sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('False'), nullable=False, comment='登録旗deleted: 0：消去未 ,1：消去済'),
    sa.ForeignKeyConstraint(['created_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['deleted_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['pref_code'], ['m_prefecture.pref_id'], ),
    sa.PrimaryKeyConstraint('base_id')
    )
    op.create_table('m_vehicles',
    sa.Column('vehicle_id', sa.Integer(), nullable=False, comment='車両ID'),
    sa.Column('vehicle_name', sa.String(length=200), nullable=True, comment='名前車両'),
    sa.Column('maker_id', sa.Integer(), nullable=True, comment='メーカーID'),
    sa.Column('store_id', sa.Integer(), nullable=True, comment='売上ID'),
    sa.Column('year', sa.Integer(), nullable=True, comment='製造年'),
    sa.Column('mileage', sa.Integer(), nullable=True, comment='車の走行距離(km)'),
    sa.Column('vehicle_status', sa.Integer(), nullable=True, comment='車の状態：1-利用可能、2-レンタル済、3-保守中'),
    sa.Column('vehicle_seat', sa.Integer(), nullable=True, comment='Số lượng ghế'),
    sa.Column('vehicle_type', sa.String(length=200), nullable=True, comment='Kiểu xe'),
    sa.Column('vehicle_value', sa.Float(), nullable=True, comment='Giá xe'),
    sa.Column('vehicleEngine', sa.String(length=200), nullable=True, comment='Động cơ xe'),
    sa.Column('vehicleRating', sa.String(length=5), nullable=True, comment='Xếp hạng'),
    sa.Column('vehicleConsumedEnergy', sa.String(length=100), nullable=True, comment='Năng lượng tiêu hao trên 100km'),
    sa.Column('vehicle_describe', sa.String(length=200), nullable=True, comment='Mô tả'),
    sa.ForeignKeyConstraint(['maker_id'], ['m_makers.maker_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['m_stores.store_id'], ),
    sa.PrimaryKeyConstraint('vehicle_id')
    )
    op.create_table('t_rental_orders',
    sa.Column('rental_orders_id', sa.Integer(), nullable=False, comment='発注明細ID:自動採番'),
    sa.Column('total_amount', sa.Float(), nullable=True, comment='合計'),
    sa.Column('payment_method_id', sa.Integer(), nullable=True, comment='お支払い方法ID'),
    sa.Column('rental_status', sa.Integer(), nullable=True, comment='注文の状態。1:新規、2:確認中、3:確認済、4:支払い済み、5:キャンセル'),
    sa.Column('paymented_at', sa.DateTime(), nullable=False, comment='支払日'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='作成日時:プログラムでは設定しない'),
    sa.Column('created_by', sa.Integer(), nullable=True, comment='作成者'),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新日時:プログラムでは設定しない'),
    sa.Column('modified_by', sa.Integer(), nullable=True, comment='更新者'),
    sa.Column('deleted_at', sa.DateTime(), nullable=True, comment='削除日時'),
    sa.Column('deleted_by', sa.Integer(), nullable=True, comment='削除者'),
    sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('False'), nullable=False, comment='登録旗deleted: 0：消去未 ,1：消去済'),
    sa.ForeignKeyConstraint(['created_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['deleted_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['payment_method_id'], ['m_payment_methods.payment_method_id'], ),
    sa.PrimaryKeyConstraint('rental_orders_id')
    )
    op.create_table('m_account_base',
    sa.Column('account_base_id', sa.Integer(), nullable=False, comment='アカウントベースID'),
    sa.Column('account_id', sa.Integer(), nullable=True, comment='アカウントID'),
    sa.Column('base_id', sa.Integer(), nullable=True, comment='拠点ID'),
    sa.Column('version', sa.Integer(), server_default=sa.text('1'), nullable=False, comment='バージョン:楽観的排他で利用'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='作成日時:プログラムでは設定しない'),
    sa.Column('created_by', sa.Integer(), nullable=True, comment='作成処理:プログラムで設定、API名、関数名'),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新日時:プログラムでは設定しない'),
    sa.Column('modified_by', sa.Integer(), nullable=True, comment='更新処理:プログラムで設定、API名、関数名'),
    sa.Column('deleted_at', sa.DateTime(), nullable=True, comment='削除日時'),
    sa.Column('deleted_by', sa.Integer(), nullable=True, comment='削除者'),
    sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('False'), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['base_id'], ['m_base.base_id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['deleted_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['m_accounts.account_id'], ),
    sa.PrimaryKeyConstraint('account_base_id')
    )
    op.create_table('m_vehicle_img',
    sa.Column('vehicleImageid', sa.Integer(), nullable=False),
    sa.Column('vehicleId', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['vehicleId'], ['m_vehicles.vehicle_id'], ),
    sa.PrimaryKeyConstraint('vehicleImageid')
    )
    op.create_table('t_rental_order_detail',
    sa.Column('rental_orders_detail_id', sa.Integer(), nullable=False, comment='発注明細ID:自動採番'),
    sa.Column('rental_order_id', sa.Integer(), nullable=False, comment='車両ID'),
    sa.Column('vehicle_id', sa.Integer(), nullable=False, comment='車両ID'),
    sa.Column('option_id', sa.Integer(), nullable=False, comment='車両ID'),
    sa.Column('quantity', sa.Integer(), nullable=False, comment='数量'),
    sa.Column('amount', sa.Float(), nullable=False, comment='小計'),
    sa.Column('rental_start_date', sa.DateTime(), nullable=False, comment='レンタル開始日'),
    sa.Column('rental_end_date', sa.DateTime(), nullable=False, comment='レンタル終了日'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='作成日時:プログラムでは設定しない'),
    sa.Column('created_by', sa.Integer(), nullable=True, comment='作成者'),
    sa.Column('modified_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新日時:プログラムでは設定しない'),
    sa.Column('modified_by', sa.Integer(), nullable=True, comment='更新者'),
    sa.Column('deleted_at', sa.DateTime(), nullable=True, comment='削除日時'),
    sa.Column('deleted_by', sa.Integer(), nullable=True, comment='削除者'),
    sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('False'), nullable=False, comment='登録旗deleted: 0：消去未 ,1：消去済'),
    sa.ForeignKeyConstraint(['created_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['deleted_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['m_accounts.account_id'], ),
    sa.ForeignKeyConstraint(['option_id'], ['m_options.option_id'], ),
    sa.ForeignKeyConstraint(['rental_order_id'], ['t_rental_orders.rental_orders_id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['m_vehicles.vehicle_id'], ),
    sa.PrimaryKeyConstraint('rental_orders_detail_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_rental_order_detail')
    op.drop_table('m_vehicle_img')
    op.drop_table('m_account_base')
    op.drop_table('t_rental_orders')
    op.drop_table('m_vehicles')
    op.drop_table('m_base')
    op.drop_table('m_stores')
    op.drop_table('m_prefecture')
    op.drop_table('m_payment_methods')
    op.drop_table('m_options')
    op.drop_table('m_models')
    op.drop_table('m_makers')
    op.drop_table('m_insurances')
    op.drop_table('m_accounts')
    # ### end Alembic commands ###
