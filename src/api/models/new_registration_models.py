from sqlalchemy import Column, String, Text, CHAR, Integer, DateTime, BIGINT, Boolean, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func, text

Base = declarative_base()
metadata = Base.metadata


class KittingMaster(Base):
    __tablename__ = 'm_kitting'

    kittingMasterId = Column("kitting_master_id",
                             Integer, primary_key=True, comment="キッティングマスタID")
    kittingMasterName = Column(
        "kitting_master_name", String(200), comment="キッティングマスタ名称")
    note = Column("note", Text, comment="備考")
    version = Column("version", Integer, nullable=False,
                     server_default=text("1"), comment="バージョン:楽観的排他で利用")
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    kitting = relationship(
        "Kitting", back_populates="kittingMaster")


class ItemSet(Base):
    __tablename__ = 'm_item_set'

    itemIdSet = Column("item_id_set", Integer, primary_key=True,
                       comment='セット用品目ID:セット用の品目の品目ID')
    itemSetType = Column("item_set_type", Integer,
                         nullable=False, server_default=text("0"))
    itemSetName = Column("item_set_name", String(200))
    itemSetJanCode = Column("item_set_jan_code", String(13))
    itemSetMakerId = Column(
        "item_set_maker_id", ForeignKey("m_maker.maker_id"), nullable=False)
    itemSetMakerModel = Column("item_set_maker_model", String(200))
    itemSetOs = Column("item_set_os", Integer,
                       nullable=False, server_default=text("0"))
    itemSetExpirationDateFrom = Column(
        "item_set_expiration_date_from", Date)
    itemSetExpirationDateTo = Column("item_set_expiration_date_to", Date)
    taxIncPrice = Column("tax_inc_price", Float, comment="税には価格が含まれます")
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    makerMaster = relationship("MakerMaster", back_populates="itemSet")
    itemSetItem = relationship(
        "ItemSetItem", uselist=False, back_populates="itemSet")
    order = relationship("Order", back_populates="itemSet")


class ItemSetItem(Base):
    __tablename__ = 'm_item_set_item'

    itemSetItemId = Column("item_set_item_id", Integer, primary_key=True)
    itemIdSet = Column("item_id_set", ForeignKey(
        "m_item_set.item_id_set"), nullable=False)
    itemId = Column("item_id", ForeignKey("m_item.item_id"), nullable=False,
                    comment='品目ID:セットされる個別の品目ID')
    isMain = Column("is_main", Boolean, nullable=False, server_default=text(
        "False"), comment='メインフラグ:0：非メイン、1：メイン品目。「メイン可」の品目タイプの品目が対象')
    sortOrder = Column("sort_order", Integer, nullable=False,
                       server_default=text("1"), comment='表示順')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    itemSet = relationship("ItemSet", back_populates="itemSetItem")
    itemMaster = relationship("ItemMaster", back_populates="itemSetItem")


class Procurement(Base):
    __tablename__ = 't_procurement'

    procurementId = Column("procurement_id", Integer,
                           primary_key=True, comment="調達ID")
    procurementName = Column("procurement_name", String(200), comment="調達名称")
    procurementStatus = Column(
        "procurement_status",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="調達ステータス:0：作成中、1：見積依頼、2：見積回答、3：承認依頼、4：承認済、5：発注依頼、6：発注済、7：無効（削除）",
    )
    isBack = Column(
        "is_back",
        Boolean,
        nullable=False,
        server_default=text("False"),
        comment="差戻フラグ:0：対象外、1：対象(差戻状態である)",
    )
    quotationRequester = Column(
        "quotation_requester", String(36), comment="見積依頼者")
    quotationRequestNote = Column(
        "quotation_request_note", String(2000), comment="見積依頼備考"
    )
    quotationRequestDatetime = Column(
        "quotation_request_datetime", DateTime, comment="見積依頼日時"
    )
    quotationAccountId = Column(
        "quotation_account_id", ForeignKey("m_accounts.account_id"), comment="見積担当者"
    )
    quotationNote = Column("quotation_note", String(2000), comment="見積回答備考")
    quotationDatetime = Column(
        "quotation_datetime", DateTime, comment="見積回答日時")
    approvalRequester = Column(
        "approval_requester", String(36), comment="承認依頼者")
    approvalExpirationDate = Column(
        "approval_expiration_date", Date, comment="承認期限")
    approvalRequestNote = Column(
        "approval_request_note", String(2000), comment="承認依頼備考"
    )
    approvalRequestDatetime = Column(
        "approval_request_datetime", DateTime, comment="承認依頼日時"
    )
    approvalAccountId = Column(
        "account_id", ForeignKey("m_accounts.account_id"), comment="承認者"
    )
    approvalNote = Column("approval_note", String(2000), comment="承認備考")
    approvalDatetime = Column("approval_datetime", DateTime, comment="承認日時")
    totalAmount = Column("total_amount", BIGINT)
    extApprovalId = Column("ext_approval_id", String(100), comment="外部承認ID")
    version = Column(
        "version",
        Integer,
        nullable=False,
        server_default=text("1"),
        comment="バージョン:楽観的排他で利用",
    )
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    order = relationship("Order", back_populates="procurement")


class Order(Base):
    __tablename__ = 't_order'

    orderId = Column("order_id", Integer, primary_key=True,
                     comment="発注明細ID:自動採番")
    procurementId = Column(
        "procurement_id",
        ForeignKey("t_procurement.procurement_id"),
        nullable=False,
        comment="調達ID",
    )
    itemId = Column(
        "item_id", ForeignKey("m_item.item_id"), nullable=False, comment="品目ID"
    )
    itemIdSet = Column(
        "item_id_set",
        ForeignKey("m_item_set.item_id_set"),
        comment="セット用品目ID:セット用の品目の品目ID",
    )
    quantity = Column("quantity", Integer, comment="数量")
    amount = Column("amount", Float, comment="小計")
    hasUsersFile = Column(
        "has_users_file",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment='利用者ファイル有無:0：なし、1：あり実ファイルはS3の以下に格納。バケット名/{調達ID}/{発注明細ID}+"_users_"+[アップロードした時のファイル名]',
    )
    hasQuotationFile = Column(
        "has_quotation_file",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment='見積有無:0：なし、1：あり実ファイルはS3の以下に格納。バケット名/{調達ID}/{発注明細ID}+"_quotation_"+[アップロードした時のファイル名]：',
    )
    estimatedArrivalDate = Column(
        "estimated_arrival_date", Date, comment="入荷予定日")
    estimatedShippingDate = Column(
        "estimated_shipping_date", Date, comment="出荷予定日")
    kittingMasterId = Column(
        "kitting_master_id",
        ForeignKey("m_kitting.kitting_master_id"),
        comment="キッティングマスタID",
    )
    recordType = Column(
        "record_type", Integer, nullable=False, server_default=text("0"), comment="計上方式"
    )
    supplierId = Column(
        "supplier_id", ForeignKey("m_supplier.supplier_id"), comment="発注先ID"
    )
    orderOn = Column("order_on", Date, comment="発注日")
    hasOrderFile = Column(
        "has_order_file",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment='エビデンスファイル有無:0：なし、1：あり実ファイルはS3の以下に格納。バケット名/{調達ID}/{発注明細ID}+"_order_"+[アップロードした時のファイル名]',
    )
    version = Column(
        "version",
        Integer,
        nullable=False,
        server_default=text("1"),
        comment="バージョン:楽観的排他で利用",
    )
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    procurement = relationship("Procurement", back_populates="order")
    itemMaster = relationship("ItemMaster", back_populates="order")
    supplier = relationship("SupplierMaster", back_populates="order")
    arrival = relationship("Arrival", back_populates="order")
    itemSet = relationship("ItemSet", back_populates="order")


class ItemMaster(Base):
    __tablename__ = 'm_item'

    itemId = Column('item_id', Integer, primary_key=True, comment='品目ID')
    itemName = Column('item_name', String(200), comment='品目名称')
    janCode = Column('jan_code', String(13), comment='JANコード')
    makerId = Column("maker_id", ForeignKey(
        "m_maker.maker_id"), nullable=False, comment='メーカーID')
    makerModel = Column('maker_model', String(200), comment='メーカー型番')
    assetType = Column('asset_type', Integer, nullable=False, server_default=text(
        "0"), comment='資産区分:1：償却資産(PCセット)、2：償却資産(PC,機器)、3：償却資産(ソフトウェア)、4：消耗品、5：リース、6：レンタル')
    expirationDateFrom = Column('expiration_date_from', Date, comment='有効開始日')
    expirationDateTo = Column('expiration_date_to', Date, comment='有効終了日')
    serialNumber = Column('serial_number', String(100), comment='物理資産ID')
    version = Column('version', Integer, nullable=False,
                     server_default=text("1"), comment='バージョン:楽観的排他で利用')
    osId = Column('os_id', Integer, comment='OS')
    orderUnit = Column('order_unit', Integer, comment='発注単位数量')
    orderUnitMax = Column('order_unit_max', Integer, comment='最大発注単位量')
    price = Column('price', Integer, comment='単価')
    tax = Column('tax', Integer, comment="税")
    taxIncPrice = Column('tax_inc_price', Float, comment="税には価格が含まれます")
    itemTitle = Column('item_title', String(
        200), comment='商品タイトル:未指定の場合は「品目名称」を設定')
    itemDescription = Column('item_description', Text, comment='商品説明')
    # itemImage = Column('item_image',String(200))
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    itemSetItem = relationship("ItemSetItem", back_populates="itemMaster")
    order = relationship("Order", back_populates="itemMaster")
    makerMaster = relationship("MakerMaster", back_populates="itemMaster")
    arrival = relationship("Arrival", back_populates="itemMaster")


class MakerMaster(Base):
    __tablename__ = 'm_maker'

    makerId = Column('maker_id', Integer, primary_key=True, comment='メーカーID')
    makerName = Column('maker_name', String(200), comment='メーカー名称')
    sortOrder = Column('sort_order', Integer, nullable=False,
                       server_default=text("1"), comment='表示順')
    note = Column('note', Text, comment='備考')
    version = Column('version', Integer, nullable=False,
                     server_default=text("1"), comment='バージョン:楽観的排他で利用')
    area = Column('area', String(
        200), comment='エリア:hokkaido：北海道, tohoku：東北, kanto_koushinetsu：関東甲信, hokuriku：北陸, tokai：東海,kinki：近畿,chugoku：中国,shikoku：四国,kyushu：九州,okinawa：沖縄')
    zipCode = Column('zip_code', String(10), comment='郵便番号')
    prefCode = Column("pref_code", ForeignKey(
        "m_prefecture.pref_id"), nullable=False, comment='都道府県コード')
    city = Column('city', String(200), comment='市区町村')
    street = Column('street', String(200), comment='番地')
    building = Column('building', String(200), comment='建物')
    pilotNumber = Column('pilot_number', String(200), comment='代表電話番号')
    department = Column('department', String(200), comment='担当部署')
    pic = Column('pic', String(200), comment='担当者')
    directNumber = Column('direct_number', String(200), comment='担当電話番号')
    directEmailAddress = Column(
        'direct_email_address', String(200), comment='担当メールアドレス')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    itemSet = relationship("ItemSet", back_populates="makerMaster")
    itemMaster = relationship(
        "ItemMaster", uselist=False, back_populates="makerMaster")
    prefecture = relationship("Prefecture")


class OutsourcingCompanyMaster(Base):
    __tablename__ = 'm_outsourcing_company'

    outsourcingCompanyId = Column("outsourcing_company_id",
                                  Integer, primary_key=True, comment='委託先ID')
    outsourcingCompanyName = Column(
        "outsourcing_company_name", String(200), comment='委託先名称')
    area = Column('area', String(
        200), comment='エリア:hokkaido：北海道, tohoku：東北, kanto_koushinetsu：関東甲信, hokuriku：北陸, tokai：東海,kinki：近畿,chugoku：中国,shikoku：四国,kyushu：九州,okinawa：沖縄')
    zipCode = Column('zip_code', String(10), comment='郵便番号')
    prefCode = Column("pref_code", ForeignKey(
        "m_prefecture.pref_id"), nullable=False, comment='都道府県コード')
    city = Column('city', String(200), comment='市区町村')
    street = Column('street', String(200), comment='番地')
    building = Column('building', String(200), comment='建物')
    pilotNumber = Column('pilot_number', String(200), comment='代表電話番号')
    department = Column('department', String(200), comment='担当部署')
    pic = Column('pic', String(200), comment='担当者')
    directNumber = Column('direct_number', String(200), comment='担当電話番号')
    directEmailAddress = Column(
        'direct_email_address', String(200), comment='担当メールアドレス')
    note = Column('note', Text, comment='備考')
    sortOrder = Column("sort_order", Integer, nullable=False,
                       server_default=text("1"), comment='表示順')
    version = Column('version', Integer, nullable=False,
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    prefecture = relationship("Prefecture")
    shipping = relationship("Shipping", uselist=False,
                            back_populates="outsourcingCompany")
    pickUp = relationship("PickUp", uselist=False,
                          back_populates="outsourcingCompany")
    repairing = relationship("Repairing", back_populates="outsourcingCompany")
    disposal = relationship("Disposal", back_populates="outsourcingCompany")


class Prefecture(Base):
    __tablename__ = 'm_prefecture'

    prefId = Column("pref_id", Integer, primary_key=True, comment="県ID")
    prefName = Column("pref_name", String(200), comment="名前県")


class BaseMaster(Base):
    __tablename__ = 'm_base'

    baseId = Column("base_id", Integer, primary_key=True, comment='拠点ID')
    baseCd = Column("base_cd", String(200), comment='拠点コード')
    baseName = Column("base_name", String(200), comment='拠点名')
    zipCode = Column("zip_code", String(10), comment='郵便番号')
    prefCode = Column("pref_code", ForeignKey(
        "m_prefecture.pref_id"), nullable=False, comment='都道府県コード')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    prefecture = relationship("Prefecture")
    arrival = relationship("Arrival", back_populates="baseMaster")
    use = relationship("Use", back_populates="baseMaster")
    accountBaseMaster = relationship(
        "AccountBaseMaster", back_populates="baseMaster")
    notificationTo = relationship(
        "NotificationTo", back_populates="baseMaster")


class Arrival(Base):
    __tablename__ = 't_arrival'

    arrivalId = Column(
        "arrival_id", Integer, primary_key=True, comment="資産ID:資産登録前だが資産IDとする"
    )
    arrivalCode = Column("arrival_code", String(200), comment="資産コード")
    isAsset = Column(
        "is_asset",
        Boolean,
        nullable=False,
        server_default=text("False"),
        comment="資産登録フラグ:0：未、1：済",
    )
    inspectionStatus = Column(
        "inspection_status",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="検品ステータス:0：未,1：合格,2：不合格",
    )
    inspectionStatusNote = Column(
        "inspection_status_note", String(400), comment="検査ステータスノート"
    )
    inspectionDate = Column("inspection_date", Date, comment="検査日")
    inspectionAccountId = Column(
        "inspection_account_id", ForeignKey("m_accounts.account_id"), comment="検品担当者"
    )
    accountId = Column(
        "account_id", ForeignKey("m_accounts.account_id"), comment="アカウントID"
    )
    usingFrom = Column("using_from", DateTime)
    usingTo = Column("using_to", DateTime)
    assetApproveAccountId = Column(
        "asset_approve_account_id", ForeignKey("m_accounts.account_id")
    )
    failureAction = Column(
        "failure_action",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="不合格処理:0：未,1：返品(再入荷待ち),2：返品(再入荷済),3：返品(再入荷なし)",
    )
    failureActionNote = Column(
        "failure_action_note", String(400), comment="障害アクションノート")
    orderId = Column("order_id", ForeignKey(
        "t_order.order_id"), comment="発注明細ID")
    itemId = Column(
        "item_id", ForeignKey("m_item.item_id"), comment="品目ID"
    )
    itemNameKana = Column("item_name_kana", String(400), comment="品目名称カナ")
    itemTypeId = Column(
        "item_type_id", ForeignKey("m_item_type.item_type_id"), comment="タイプID"
    )
    price = Column("price", Integer, comment="単価")
    baseId = Column("base_id", ForeignKey("m_base.base_id"), comment="入荷拠点ID")
    arrivalType = Column(
        "arrival_type",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="入荷方法:0：発注,1：持ち込み",
    )
    arrivalOn = Column(
        "arrival_on", DateTime, nullable=False, server_default=func.now(), comment="入荷日"
    )
    recordType = Column(
        "record_type", Integer, nullable=False, server_default=text("0"), comment="計上方式"
    )
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    order = relationship("Order", back_populates="arrival")
    itemMaster = relationship("ItemMaster", back_populates="arrival")
    itemTypeMaster = relationship("ItemTypeMaster", back_populates="arrival")
    baseMaster = relationship("BaseMaster", back_populates="arrival")
    asset = relationship("Asset", back_populates="arrival")
    inspectionAccount = relationship(
        "AccountMaster", foreign_keys="Arrival.inspectionAccountId", back_populates="arrival")
    accountMaster = relationship(
        "AccountMaster", foreign_keys="Arrival.accountId", back_populates="arrivalAccountMaster")


class ItemTypeMaster(Base):
    __tablename__ = "m_item_type"

    itemTypeId = Column("item_type_id", Integer,
                        primary_key=True, comment='タイプID')
    itemTypeName = Column("item_type_name", String(400), comment='タイプ名称')
    canBeMain = Column("can_be_main", Boolean, nullable=False, server_default=text(
        "False"), comment='メイン可フラグ:0：不可、1：可（主にPCを想定）')
    sortOrder = Column("sort_order", Integer, nullable=False,
                       server_default=text("1"), comment='表示順')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    arrival = relationship("Arrival", back_populates="itemTypeMaster")


class Asset(Base):
    __tablename__ = "t_asset"

    assetId = Column("asset_id", Integer, primary_key=True, comment="資産ID")
    assetNameKana = Column("asset_name_kana", String(500), comment="資産名称カナ")
    assetCd = Column("asset_cd", String(100), comment="資産コード")
    assetStatus = Column(
        "asset_status",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="資産ステータス:0：在庫(stock), 1：キッティング中(kitting), 2：出荷中(shipping), 3：集荷中(pickingup), 4：修理中(repairing), 5：廃棄中(disposing), 6：利用中(using), 7：廃棄済み(disposed)",
    )
    arrivalId = Column(
        "arrival_id", ForeignKey("t_arrival.arrival_id"), nullable=False, comment="資産ID"
    )
    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"), comment='資産ID')
    assetKind = Column(
        "asset_kind",
        String(50),
        comment="資産種別:set_desktop：デスクトップセット,set_laptop：ノートセット,desktop：デスクトップ,laptop：ノート,tablet：タブレット,device：機器,software_without_license：ソフトウェア(ライセンスなし),software_with_license：ソフトウェア(ライセンスあり),cloud_license：クラウドライセンス",
    )
    assetType = Column(
        "asset_type",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="資産区分:0：償却資産(PCセット),1：償却資産(P,機器),2：償却資産(ソフトウェア),3：消耗品,4：リース,5：レンタル",
    )
    assetFrom = Column("asset_from", Date, comment="資産開始日")
    assetTo = Column("asset_to", Date, comment="資産終了日")
    parentAssetId = Column("parent_asset_id", Integer, comment="親資産ID")
    recordType = Column(
        "record_type", Integer, nullable=False, server_default=text("0"), comment="計上方式"
    )
    version = Column(
        "version",
        Integer,
        nullable=False,
        server_default=text("1"),
        comment="バージョン:楽観的排他で利用",
    )
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    arrival = relationship("Arrival", back_populates="asset")
    use = relationship("Use", back_populates="asset")
    shipping = relationship("Shipping", back_populates="asset")
    pickUp = relationship("PickUp", back_populates="asset")
    repairing = relationship(
        "Repairing", back_populates="asset")
    disposal = relationship("Disposal", back_populates="asset")
    kitting = relationship("Kitting", back_populates="asset")
    accountMaster = relationship(
        "AccountMaster", foreign_keys="Asset.accountId", back_populates="asset")


class Use(Base):
    __tablename__ = "t_use"

    useId = Column("use_id", Integer, primary_key=True, comment='利用ID')
    useStatus = Column("use_status", Integer, nullable=False,
                       server_default=text("0"), comment='利用ステータス: 0：未, 1：中, 2：完了')
    assetId = Column("asset_id", ForeignKey(
        "t_asset.asset_id"), comment='資産ID')
    useOnFrom = Column("use_on_from", Date, comment='利用開始日')
    useOnTo = Column("use_on_to", Date, comment='利用終了日')
    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"), comment='アカウントID')
    groupId = Column("group_id", ForeignKey(
        "m_group.group_id"), comment='グループID')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    asset = relationship("Asset", back_populates="use")
    baseMaster = relationship("BaseMaster", back_populates="use")
    accountMaster = relationship(
        "AccountMaster", foreign_keys="Use.accountId", back_populates="use")
    groupMaster = relationship("GroupMaster", back_populates="use")


class AssetDepreciation(Base):
    __tablename__ = "m_asset_depreciation"

    assetId = Column("asset_id", ForeignKey(
        "t_asset.asset_id"), primary_key=True, nullable=False, comment='資産ID')
    fiscalYear = Column("fiscal_year", CHAR(4), comment='年度:YYYY')
    amount = Column("amount", Integer, comment='費用')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")


class Shipping(Base):
    __tablename__ = "t_shipping"

    shippingId = Column("shipping_id", Integer,
                        primary_key=True, comment='出荷ID')
    shippingReceptionStatus = Column("shipping_reception_status",
                                     Integer, nullable=False, server_default=text("0"), comment='出荷受付ステータス')
    shippingReceptionType = Column("shipping_reception_type",
                                   Integer, nullable=False, server_default=text("0"))
    useStartDay = Column("use_start_day", Date)
    estimatedShippingDate = Column("estimated_shipping_date", Date)
    shippingLate = Column("shipping_late", Boolean, nullable=False,
                          server_default=text("False"))
    shippingStatus = Column("shipping_status", Integer, nullable=False,
                            server_default=text("0"), comment='出荷ステータス: 0：未, 1：中, 2：完了')
    assetId = Column("asset_id", ForeignKey(
        "t_asset.asset_id"), comment='資産ID')
    receptionOn = Column("reception_on", DateTime, nullable=False,
                         server_default=func.now(), comment='受付日')
    workingOn = Column("working_on", Date, comment='作業開始日時')
    completedOn = Column("completed_on", Date, comment='完了日時')
    outsourcingCompanyId = Column("outsourcing_company_id", ForeignKey(
        "m_outsourcing_company.outsourcing_company_id"), comment='委託先ID')
    note = Column("note", Text, comment='備考')
    version = Column("version", Integer, nullable=False,
                     server_default=text("1"), comment='バージョン:楽観的排他で利用')
    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"))
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    asset = relationship("Asset", back_populates="shipping")
    outsourcingCompany = relationship(
        "OutsourcingCompanyMaster", back_populates="shipping")
    accountMaster = relationship(
        "AccountMaster", foreign_keys="Shipping.accountId", back_populates="shipping")


class PickUp(Base):
    __tablename__ = "t_pick_up"

    pickUpId = Column("pick_up_id", Integer, primary_key=True, comment='集荷ID')
    pickUpStatus = Column("pick_up_status", Integer, nullable=False,
                          server_default=text("0"), comment='集荷ステータス: 0：未, 1：中, 2：完了')
    assetId = Column("asset_id", ForeignKey(
        "t_asset.asset_id"), comment='資産ID')
    pickUpType = Column("pick_up_type", Integer,
                        comment='集荷区分: 0:集荷待ち（返却）1:集荷待ち（修理）')
    pickUpArrangementOn = Column(
        "pick_up_arrangement_on", DateTime, nullable=False, server_default=func.now(), comment='集荷手配日')
    pickUpScheduledDate = Column(
        "pick_up_scheduled_date", Date, comment='集荷予定日')
    completedOn = Column("completed_on", Date, comment='集荷完了日')
    outsourcingCompanyId = Column("outsourcing_company_id", ForeignKey(
        "m_outsourcing_company.outsourcing_company_id"), comment='委託先ID')
    note = Column("note", Text, comment='備考')
    version = Column("version", Integer, nullable=False,
                     server_default=text("1"), comment='バージョン:楽観的排他で利用')
    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"))
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    asset = relationship("Asset", back_populates="pickUp")
    outsourcingCompany = relationship(
        "OutsourcingCompanyMaster", back_populates="pickUp")
    accountMaster = relationship(
        "AccountMaster", foreign_keys="PickUp.accountId", back_populates="pickUp")


class Repairing(Base):
    __tablename__ = "t_repairing"

    repairingId = Column("repairing_id", Integer,
                         primary_key=True, comment="修理ID")
    repairingStatus = Column(
        "repairing_status",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="修理ステータス: 0：未, 1：中, 2：完了",
    )
    outsourcingCompanyId = Column(
        "outsourcing_company_id",
        ForeignKey("m_outsourcing_company.outsourcing_company_id"),
        comment="委託先ID",
    )
    assetId = Column("asset_id", ForeignKey(
        "t_asset.asset_id"), comment="資産ID")
    version = Column(
        "version",
        Integer,
        nullable=False,
        server_default=text("1"),
        comment="バージョン:楽観的排他で利用",
    )
    accountId = Column("account_id", ForeignKey("m_accounts.account_id"))
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    outsourcingCompany = relationship(
        "OutsourcingCompanyMaster", back_populates="repairing")
    asset = relationship("Asset", back_populates="repairing")


class Disposal(Base):
    __tablename__ = "t_disposal"

    disposalId = Column("disposal_id", Integer,
                        primary_key=True, comment="廃棄ID")
    disposalStatus = Column(
        "disposal_status",
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="廃棄ステータス: 0：未, 1：中, 2：完了",
    )
    outsourcingCompanyId = Column(
        "outsourcing_company_id",
        ForeignKey("m_outsourcing_company.outsourcing_company_id"),
        comment="委託先ID",
    )
    assetId = Column("asset_id", ForeignKey(
        "t_asset.asset_id"), comment="資産ID")
    note = Column("note", Text, comment="備考")
    version = Column(
        "version",
        Integer,
        nullable=False,
        server_default=text("1"),
        comment="バージョン:楽観的排他で利用",
    )
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    outsourcingCompany = relationship(
        "OutsourcingCompanyMaster", back_populates="disposal")
    asset = relationship("Asset", back_populates="disposal")


class GroupMaster(Base):
    __tablename__ = "m_group"

    groupId = Column("group_id", Integer, primary_key=True,
                     comment='グループID:1以上であること')
    groupName = Column("group_name", String(200), comment='グループ名称')
    groupCd = Column("group_cd", String(200), comment='グループコード')
    parentGroupId = Column("parent_group_id", Integer, nullable=False, server_default=text(
        "0"), comment='親グループID:0 は親グループが無し')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    use = relationship("Use", back_populates="groupMaster")


class AccountGroupMaster(Base):
    __tablename__ = "m_account_group"

    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"), primary_key=True, nullable=False, comment='アカウントID')
    groupId = Column("group_id", ForeignKey(
        "m_group.group_id"), comment='グループID')
    isManager = Column("is_manager", Boolean, nullable=False,
                       server_default=text("False"), comment='管理者フラグ')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")


class AccountMaster(Base):
    __tablename__ = "m_account"

    accountId = Column('account_id', Integer,
                       primary_key=True, comment='アカウントID')
    accountCd = Column('account_cd', String(
        100), comment='アカウントコード:社員番号など利用企業のIDやコードのため')
    extAccountId = Column('ext_account_id',
                          Integer, comment='外部アカウントID:cognitoなどの外部認証サービスと連携する場合は設定')
    accountName = Column('account_name', String(100), comment='アカウント名')
    emailAddress = Column('email_address', String(100), comment='メールアドレス')
    accountStatus = Column('account_status', Integer, nullable=False, server_default=text(
        "0"), comment='ステータス:0：仮登録、1：本登録、2：削除')
    isSystemManager = Column('is_system_manager',
                             Boolean, nullable=False, server_default=text("False"), comment='システム管理フラグ:アプリケーションで設定/更新しないこと')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    arrival = relationship(
        "Arrival", foreign_keys="Arrival.inspectionAccountId", back_populates="inspectionAccount")
    kitting = relationship(
        "Kitting", foreign_keys="Kitting.accountId", back_populates="accountMaster")
    kittingUserAccount = relationship(
        "Kitting", foreign_keys="Kitting.kittingUserId", back_populates="kittingUser")
    use = relationship(
        "Use", foreign_keys="Use.accountId", back_populates="accountMaster")
    shipping = relationship(
        "Shipping", foreign_keys="Shipping.accountId", back_populates="accountMaster")
    pickUp = relationship(
        "PickUp", foreign_keys="PickUp.accountId", back_populates="accountMaster")
    arrivalAccountMaster = relationship(
        "Arrival", foreign_keys="Arrival.accountId", back_populates="accountMaster")
    asset = relationship(
        "Asset", foreign_keys="Asset.accountId", back_populates="accountMaster")


class AccountRoleMaster(Base):
    __tablename__ = "m_account_role"

    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"), primary_key=True, nullable=False, comment='アカウントID')
    roleId = Column("role_id", ForeignKey("m_role.role_id"), comment='ロールID')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    roleMaster = relationship("RoleMaster", back_populates="accountRoleMaster")


class RoleMaster(Base):
    __tablename__ = "m_role"

    roleId = Column("role_id", Integer, primary_key=True, comment='ロールID')
    roleName = Column("role_name", String(200), comment='ロール名')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    accountRoleMaster = relationship(
        "AccountRoleMaster", back_populates="roleMaster")


class RoleOperationMaster(Base):
    __tablename__ = "m_role_operation"

    roleId = Column("role_id", Integer, primary_key=True, comment='ロールID')
    operationId = Column(
        "operation_id", ForeignKey("m_operation.operation_id"), comment='オペレーションID')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    operationMaster = relationship(
        "OperationMaster", back_populates="roleOperationMaster")


class OperationMaster(Base):
    __tablename__ = "m_operation"

    operationId = Column("operation_id", Integer,
                         primary_key=True, comment='オペレーションID')
    operationName = Column("operation_name", String(200), comment='オペレーション名')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    roleOperationMaster = relationship(
        "RoleOperationMaster", back_populates="operationMaster")


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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    baseMaster = relationship("BaseMaster", back_populates="accountBaseMaster")


class Notification(Base):
    __tablename__ = "t_notification"

    notificationId = Column("notification_id", Integer,
                            primary_key=True, comment='通知ID')
    notificationCd = Column("notification_cd", String(
        36), comment='通知コード:yyyymmdd0000 通知日時＋連番')
    title = Column("title", String(200), comment='件名')
    body = Column("body", Text, comment='内容')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")


class NotificationTo(Base):
    __tablename__ = "t_notification_to"

    notificationId = Column("notification_id", Integer,
                            primary_key=True, comment='通知先ID:自動採番')
    notificationToType = Column("notification_to_type",
                                String(100), comment='通知先区分:0：アカウント、1：グループ、2：ベース')
    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"), comment='アカウントID')
    groupId = Column("group_id", ForeignKey(
        "m_group.group_id"), comment='グループID')
    baseId = Column("base_id", ForeignKey("m_base.base_id"),
                    comment='拠点ID')
    notificationStatus = Column("notification_status",
                                Integer, nullable=False, server_default=text("0"), comment='通知ステータス:temporarily')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    baseMaster = relationship("BaseMaster", back_populates="notificationTo")


class SupplierMaster(Base):
    __tablename__ = "m_supplier"

    supplierId = Column("supplier_id", Integer,
                        primary_key=True, comment='発注先ID')
    supplierName = Column("supplier_name", String(200), comment='発注先名称')
    zipCode = Column("zip_code", String(10), comment='郵便番号')
    prefCode = Column("pref_code", ForeignKey(
        "m_prefecture.pref_id"), nullable=False, comment='都道府県コード')
    city = Column("city", String(200), comment='市区町村')
    street = Column("street", String(200), comment='番地')
    building = Column("building", String(200), comment='建物')
    pilotNumber = Column("pilot_number", String(200), comment='代表電話番号')
    department = Column("department", String(200), comment='担当部署')
    pic = Column("pic", String(200), comment='担当者')
    directNumber = Column("direct_number", String(200), comment='担当電話番号')
    directEmailAddress = Column(
        "direct_email_address", String(200), comment='担当メールアドレス')
    note = Column("note", Text, comment='備考')
    sortOrder = Column("sort_order", Integer, nullable=False,
                       server_default=text("1"), comment='表示順')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    order = relationship("Order", back_populates="supplier")
    prefecture = relationship("Prefecture")


class Kitting(Base):
    __tablename__ = "t_kitting"

    kittingId = Column("kitting_id", Integer,
                       primary_key=True, comment='キットID')
    kittingStatus = Column("kitting_status",
                           Integer, nullable=False, server_default=text("0"), comment='キッティングステータス: 0：未, 1：中, 2：完了')
    kittingMasterId = Column("kitting_master_id", ForeignKey(
        "m_kitting.kitting_master_id"), comment="キッティングマスタID")
    assetId = Column("asset_id", ForeignKey(
        "t_asset.asset_id"), comment='資産ID')
    kittingUserId = Column("kitting_user_id", ForeignKey(
        "m_accounts.account_id"), comment='アカウントID')
    accountId = Column("account_id", ForeignKey(
        "m_accounts.account_id"), comment='アカウントID')
    hardwareConfirmAccountId = Column("hardware_confirm_account_id", ForeignKey(
        "m_accounts.account_id"))
    softwareConfirmAccountId = Column("software_confirm_account_id", ForeignKey(
        "m_accounts.account_id"))
    kittingConfirmAccountId = Column("kitting_confirm_account_id", ForeignKey(
        "m_accounts.account_id"))
    functionalConfirmAccountId = Column("functional_confirm_account_id", ForeignKey(
        "m_accounts.account_id"))
    kittingComment = Column("kitting_comment", String(50))
    kittingAt = Column("kitting_at", DateTime)
    completedAt = Column("completed_at", DateTime)
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")

    kittingMaster = relationship("KittingMaster", back_populates="kitting")
    asset = relationship("Asset", back_populates="kitting")
    accountMaster = relationship(
        "AccountMaster", foreign_keys="Kitting.accountId", back_populates="kitting")
    kittingUser = relationship(
        "AccountMaster", foreign_keys="Kitting.kittingUserId", back_populates="kittingUserAccount")


class GenCode(Base):
    __tablename__ = "m_gen_code"

    genCodeId = Column("gen_code_id", Integer, primary_key=True)
    tableName = Column("table_name", String(50))
    fieldName = Column("field_name", String(50))
    fieldValue = Column("field_value", Integer)
    fieldDisplayLabel = Column("field_display_label", String(50))


class AssetSetAsset(Base):
    __tablename__ = 't_asset_set_asset'

    assetSetAssetId = Column("asset_set_asset_id", Integer, primary_key=True)
    assetIdSet = Column("asset_id_set", ForeignKey(
        "t_asset_set.asset_id_set"), nullable=False)
    assetId = Column("asset_id", ForeignKey("t_asset.asset_id"),
                     comment='資産ID')
    isMain = Column("is_main", Boolean, nullable=False, server_default=text(
        "False"), comment='メインフラグ:0：非メイン、1：メイン品目。「メイン可」の品目タイプの品目が対象')
    sortOrder = Column("sort_order", Integer, nullable=False,
                       server_default=text("1"), comment='表示順')
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")


class AssetSet(Base):
    __tablename__ = 't_asset_set'

    assetIdSet = Column("asset_id_set", Integer, primary_key=True)
    orderId = Column("order_id", Integer)
    assetSeType = Column("asset_set_type", Integer,
                         nullable=False, server_default=text("0"))
    assetSetName = Column("asset_set_name", String(200))
    assetSetJanCode = Column("asset_set_jan_code", String(13))
    assetSetMakerId = Column("asset_set_maker_id", ForeignKey(
        "m_maker.maker_id"), nullable=False)
    assetSetMakerModel = Column("asset_set_maker_model", String(200))
    assetSetOs = Column("asset_set_os", Integer,
                        nullable=False, server_default=text("0"))
    assetSetExpirationDateFrom = Column("asset_set_expiration_date_from", Date)
    assetSetExpirationDateTo = Column("asset_set_expiration_date_to", Date)
    taxincPrice = Column("tax_inc_price", Float, comment="税には価格が含まれます")
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
                       server_default=text("False"), comment="登録旗deleted: 0：消去未 ,1：消去済")
