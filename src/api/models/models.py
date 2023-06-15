from sqlalchemy import Column, Numeric, String, Text, Integer, DateTime, Boolean, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func, text

Base = declarative_base()
metadata = Base.metadata


class AccountMaster(Base):
    __tablename__ = "m_accounts"

    accountId = Column('account_id', Integer,
                       primary_key=True, comment='アカウントID')
    accountCd = Column('account_cd', String(100),
                       comment='アカウントコード:社員番号など利用企業のIDやコードのため')
    extAccountId = Column('ext_account_id', Integer,
                          comment='外部アカウントID:cognitoなどの外部認証サービスと連携する場合は設定')
    accountName = Column('account_name', String(100), comment='アカウント名')
    emailAddress = Column('email_address', String(100), comment='メールアドレス')
    accountStatus = Column('account_status', Integer, nullable=False,
                           server_default=text("0"),
                           comment='ステータス:0：仮登録、1：本登録、2：削除')
    isSystemManager = Column('is_system_manager', Boolean,
                             nullable=False, server_default=text("False"),
                             comment='システム管理フラグ:アプリケーションで設定/更新しないこと')
    version = Column('version', Integer, nullable=False,
                     server_default=text("1"), comment='バージョン:楽観的排他で利用')
    createdAt = Column("created_at", DateTime, nullable=False,
                       server_default=func.now(), comment="作成日時:プログラムでは設定しない")
    createdBy = Column("created_by", String(
        200), comment="作成処理:プログラムで設定、API名、関数名")
    modifiedAt = Column("modified_at", DateTime, nullable=False,
                        server_default=func.now(), comment="更新日時:プログラムでは設定しない")
    modifiedBy = Column("modified_by", String(
        200), comment="更新処理:プログラムで設定、API名、関数名")
    deletedAt = Column("deleted_at", DateTime, comment="削除日時")
    deletedBy = Column("deleted_by", String(200), comment="削除")
    isDeleted = Column("is_deleted", Boolean, nullable=False,
                       server_default=text("False"),
                       comment="登録旗deleted: 0：消去未 ,1：消去済")


class AccountBaseMaster(Base):
    __tablename__ = "m_account_base"

    accountBaseId = Column("account_base_id", Integer, nullable=False,
                           primary_key=True, comment="アカウントベースID")
    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"), comment='アカウントID')
    baseId = Column("base_id", ForeignKey("m_base.base_id"),
                    comment='拠点ID')
    version = Column("version", Integer, nullable=False,
                     server_default=text("1"), comment='バージョン:楽観的排他で利用')
    createdAt = Column("created_at", DateTime, nullable=False,
                       server_default=func.now(), comment="作成日時:プログラムでは設定しない")
    createdBy = Column("created_by", ForeignKey(
        "m_accounts.account_id"), comment="作成処理:プログラムで設定、API名、関数名")
    modifiedAt = Column("modified_at", DateTime, nullable=False,
                        server_default=func.now(), comment="更新日時:プログラムでは設定しない")
    modifiedBy = Column("modified_by", ForeignKey(
        "m_accounts.account_id"), comment="更新処理:プログラムで設定、API名、関数名")
    deletedAt = Column("deleted_at", DateTime, comment="削除日時")
    deletedBy = Column("deleted_by", ForeignKey(
        "m_accounts.account_id"), comment="削除者")
    isDeleted = Column("is_deleted", Boolean, nullable=False,
                       server_default=text("False"))

    baseMaster = relationship("BaseMaster", back_populates="accountBaseMaster")


class BaseMaster(Base):
    __tablename__ = 'm_base'

    baseId = Column("base_id", Integer, primary_key=True, comment='拠点ID')
    baseCd = Column("base_cd", String(200), comment='拠点コード')
    baseName = Column("base_name", String(200), comment='拠点名')
    zipCode = Column("zip_code", String(10), comment='郵便番号')
    prefCode = Column("pref_code", ForeignKey("m_prefecture.pref_id"),
                      nullable=False, comment='都道府県コード')
    address = Column("address", String(400), comment='住所')
    addressee = Column("addressee", String(200), comment='受取名:配送や郵送時の受信名')
    telephoneNumber = Column("telephone_number", String(200), comment='電話番号')
    faxNumber = Column("fax_number", String(200), comment='FAX番号')
    eMailAddress = Column("e_mail_address", String(200), comment='メールアドレス')
    note = Column("note", Text, comment='備考')
    version = Column("version", Integer, nullable=False,
                     server_default=text("1"), comment='バージョン:楽観的排他で利用')
    createdAt = Column("created_at", DateTime, nullable=False,
                       server_default=func.now(), comment="作成日時:プログラムでは設定しない")
    createdBy = Column("created_by", ForeignKey(
        "m_accounts.account_id"), comment="作成処理:プログラムで設定、API名、関数名")
    modifiedAt = Column("modified_at", DateTime, nullable=False,
                        server_default=func.now(), comment="更新日時:プログラムでは設定しない")
    modifiedBy = Column("modified_by", ForeignKey(
        "m_accounts.account_id"), comment="更新処理:プログラムで設定、API名、関数名")
    deletedAt = Column("deleted_at", DateTime, comment="削除日時")
    deletedBy = Column("deleted_by", ForeignKey(
        "m_accounts.account_id"), comment="削除者")
    isDeleted = Column("is_deleted", Boolean, nullable=False,
                       server_default=text("False"),
                       comment="登録旗deleted: 0：消去未 ,1：消去済")

    prefecture = relationship("Prefecture")
    accountBaseMaster = relationship("AccountBaseMaster",
                                     back_populates="baseMaster")


class Prefecture(Base):
    __tablename__ = 'm_prefecture'

    prefId = Column("pref_id", Integer, primary_key=True, comment="県ID")
    prefName = Column("pref_name", String(200), comment="名前県")


class ModelsMaster(Base):
    __tablename__ = 'm_models'

    modelId = Column("model_id", Integer, primary_key=True, comment="モデルID")
    modelName = Column("model_name", String(200), comment="名前モデル")


class MakersMaster(Base):
    __tablename__ = 'm_makers'

    makerId = Column("maker_id", Integer, primary_key=True, comment="メーカーID")
    makerName = Column("maker_name", String(200), comment="名前メーカー")


class VehiclesMaster(Base):
    __tablename__ = 'm_vehicles'

    vehicleId = Column("vehicle_id", Integer, primary_key=True, comment="車両ID")
    vehicleName = Column("vehicle_name", String(200), comment="名前車両")
    makerId = Column("maker_id", Integer, ForeignKey("m_makers.maker_id"),
                     comment="メーカーID")
    storeId = Column("store_id", Integer, ForeignKey("m_stores.store_id"),
                     comment="売上ID")
    year = Column("year", Integer, comment="製造年")
    mileage = Column("mileage", Integer, comment="車の走行距離(km)")
    vehicleStatus = Column("vehicle_status", Integer,
                           comment="車の状態：1-利用可能、2-レンタル済、3-保守中")
    vehicleSeat = Column("vehicle_seat", Integer, comment="Số lượng ghế")
    vehicleModel = Column("vehicle_model", Integer,
                          ForeignKey("m_models.model_id"), comment="Kiểu xe")
    vehicleValue = Column("vehicle_value", Float, comment="Giá xe")
    vehicleEngine = Column("vehicleEngine", String(200), comment="Động cơ xe")
    vehicleRating = Column("vehicleRating", String(5), comment="Xếp hạng")
    vehicleConsumedEnergy = Column("vehicleConsumedEnergy", String(100),
                                   comment="Năng lượng tiêu hao trên 100km")
    vehicleDescribe = Column("vehicle_describe", String(200), comment="Mô tả")
    images = relationship('VehicleImage', back_populates='vehicle')


class VehicleImage(Base):
    __tablename__ = 'm_vehicle_img'

    vehicleImageid = Column(Integer, primary_key=True)
    vehicleId = Column(Integer, ForeignKey('m_vehicles.vehicle_id'))
    image = Column(String(255))

    vehicle = relationship('VehiclesMaster', back_populates='images')


class StoresMaster(Base):
    __tablename__ = 'm_stores'

    storeId = Column("store_id", Integer, primary_key=True, comment="売上ID")
    storeName = Column("store_name", String(200), comment="名前売上")


class OptionsMaster(Base):
    __tablename__ = 'm_options'

    optionId = Column("option_id", Integer, primary_key=True,
                      comment="オプションID")
    optionName = Column("option_name", String(200), comment="名前オプション")
    optionValue = Column("option_value", Float, comment="Giá option")


class InsurancesMaster(Base):
    __tablename__ = 'm_insurances'

    insuranceId = Column("insurance_id", Integer, primary_key=True,
                         comment="保険ID")
    insuranceName = Column("insurance_name", String(200), comment="名前保険")
    insuranceValue = Column("insurance_value", Float, comment="Giá bảo hiểm")


class PaymentMethodsMaster(Base):
    __tablename__ = 'm_payment_methods'

    paymentMethodId = Column("payment_method_id", Integer, primary_key=True,
                             comment="お支払い方法ID")
    paymentMethodName = Column("payment_method_name", String(200),
                               comment="名前お支払い方法")


class RentalOrders(Base):
    __tablename__ = 't_rental_orders'

    rentalOrdersId = Column("rental_orders_id", Integer, primary_key=True,
                            comment="発注明細ID:自動採番")
    totalAmount = Column("total_amount", Float, comment="合計")
    paymentMethodId = Column("payment_method_id",
                             ForeignKey("m_payment_methods.payment_method_id"),
                             comment="お支払い方法ID")
    rentalStatus = Column("rental_status", Integer,
                          comment="注文の状態。1:新規、2:確認中、3:確認済、4:支払い済み、5:キャンセル")
    paymentedAt = Column("paymented_at", DateTime, nullable=False,
                         comment="支払日")
    createdAt = Column("created_at", DateTime, nullable=False,
                       server_default=func.now(), comment="作成日時:プログラムでは設定しない")
    createdBy = Column("created_by", ForeignKey("m_accounts.account_id"),
                       comment="作成者")
    modifiedAt = Column("modified_at", DateTime, nullable=False,
                        server_default=func.now(), comment="更新日時:プログラムでは設定しない")
    modifiedBy = Column("modified_by", ForeignKey("m_accounts.account_id"),
                        comment="更新者")
    deletedAt = Column("deleted_at", DateTime, comment="削除日時")
    deletedBy = Column("deleted_by", ForeignKey("m_accounts.account_id"),
                       comment="削除者")
    isDeleted = Column("is_deleted", Boolean, nullable=False,
                       server_default=text("False"),
                       comment="登録旗deleted: 0：消去未 ,1：消去済")


class RentalOrderDetail(Base):
    __tablename__ = 't_rental_order_detail'

    rentalOrdersId = Column("rental_orders_detail_id", Integer,
                            primary_key=True,
                            comment="発注明細ID:自動採番")
    rentalOrderId = Column("rental_order_id",
                           ForeignKey("t_rental_orders.rental_orders_id"),
                           nullable=False, comment="車両ID")
    vehicleId = Column("vehicle_id", ForeignKey("m_vehicles.vehicle_id"),
                       nullable=False, comment="車両ID")
    optionId = Column("option_id", ForeignKey("m_options.option_id"),
                      nullable=False, comment="車両ID")
    quantity = Column("quantity", Integer, comment="数量", nullable=False)
    amount = Column("amount", Float, comment="小計", nullable=False)
    rentalStartDate = Column("rental_start_date", DateTime, nullable=False,
                             comment="レンタル開始日")
    rentalEndDate = Column("rental_end_date", DateTime, nullable=False,
                           comment="レンタル終了日")
    createdAt = Column("created_at", DateTime, nullable=False,
                       server_default=func.now(), comment="作成日時:プログラムでは設定しない")
    createdBy = Column("created_by", ForeignKey("m_accounts.account_id"),
                       comment="作成者")
    modifiedAt = Column("modified_at", DateTime, nullable=False,
                        server_default=func.now(), comment="更新日時:プログラムでは設定しない")
    modifiedBy = Column("modified_by", ForeignKey("m_accounts.account_id"),
                        comment="更新者")
    deletedAt = Column("deleted_at", DateTime, comment="削除日時")
    deletedBy = Column("deleted_by", ForeignKey("m_accounts.account_id"),
                       comment="削除者")
    isDeleted = Column("is_deleted", Boolean, nullable=False,
                       server_default=text("False"),
                       comment="登録旗deleted: 0：消去未 ,1：消去済")


class RentalOrderCart(Base):
    __tablename__ = 't_rental_order_cart'

    rentalOrdersCartId = Column("rental_orders_cart_id", Integer,
                                primary_key=True,
                                comment="発注明細ID:自動採番")
    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"), comment='アカウントID')
    vehicleId = Column("vehicle_id", ForeignKey("m_vehicles.vehicle_id"),
                       nullable=False, comment="車両ID")
    optionId = Column("option_id", ForeignKey("m_options.option_id"),
                      comment="車両ID")
    insuranceId = Column("insurance_id", ForeignKey(
        "m_insurances.insurance_id"), comment="保険ID")
    statusCart = Column("status_cart", Integer, nullable=False, server_default=text("0"),
                        comment="0: giỏ hàng; 1: đã đặt")
    rentalStartDate = Column("rental_start_date", DateTime,
                             comment="レンタル開始日")
    rentalEndDate = Column("rental_end_date", DateTime,
                           comment="レンタル終了日")
    createdAt = Column("created_at", DateTime, nullable=False,
                       server_default=func.now(), comment="作成日時:プログラムでは設定しない")
    createdBy = Column("created_by", ForeignKey("m_accounts.account_id"),
                       comment="作成者")
    modifiedAt = Column("modified_at", DateTime, nullable=False,
                        server_default=func.now(), comment="更新日時:プログラムでは設定しない")
    modifiedBy = Column("modified_by", ForeignKey("m_accounts.account_id"),
                        comment="更新者")
    deletedAt = Column("deleted_at", DateTime, comment="削除日時")
    deletedBy = Column("deleted_by", ForeignKey("m_accounts.account_id"),
                       comment="削除者")
    isDeleted = Column("is_deleted", Boolean, nullable=False,
                       server_default=text("False"),
                       comment="登録旗deleted: 0：消去未 ,1：消去済")
