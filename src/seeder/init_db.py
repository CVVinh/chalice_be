from api.models.models import *
from api.models import session
from email.mime import base
import sys
import os

sys.path.insert(0, os.getcwd())


account = (
    AccountsMaster(
        account_id=1,
        account_cd="abc",
        account_name="acbd",
        account_status=0,
        is_deleted=0,
    ),
    AccountsMaster(
        account_id=2,
        account_cd="add",
        account_name="acbd",
        account_status=0,
        is_deleted=0,
    ),
    AccountsMaster(
        account_id=3,
        account_cd="aasd",
        account_name="acbd",
        account_status=0,
        is_deleted=0,
    ),
)
base_master = (
    BaseMaster(base_id=1, base_name="abc", pref_code=22, is_deleted=0),
    BaseMaster(base_id=2, base_name="asd", pref_code=43, is_deleted=0),
    BaseMaster(base_id=3, base_name="asf", pref_code=11, is_deleted=0),
)
maker = (
    MakersMaster(maker_id=1, maker_name="ec ec eec",
                 pref_code=4, is_deleted=0),
    MakersMaster(maker_id=2, maker_name="ec-er", pref_code=9, is_deleted=0),
    MakersMaster(maker_id=3, maker_name="ecccc", pref_code=32, is_deleted=0),
)
item_master = (
    ItemMaster(
        item_id=1,
        item_name="abc",
        maker_id=2,
        asset_type=0,
        expiration_date_from="2023-01-08",
        expiration_date_to="2023-02-23",
        order_unit=4,
        order_unit_max=6,
        item_title="abcd",
        is_deleted=0,
    ),
    ItemMaster(
        item_id=2,
        item_name="ec ec ec!",
        maker_id=1,
        asset_type=0,
        expiration_date_from="2023-01-08",
        expiration_date_to="2023-02-23",
        order_unit=4,
        order_unit_max=6,
        item_title="abcd",
        is_deleted=0,
    ),
    ItemMaster(
        item_id=3,
        item_name="ec ec?",
        maker_id=1,
        asset_type=0,
        expiration_date_from="2023-01-08",
        expiration_date_to="2023-02-23",
        order_unit=4,
        order_unit_max=6,
        item_title="abcd",
        is_deleted=0,
    ),
)
procurement = (
    Procurement(
        procurement_id=1,
        procurement_name="ec ec ec!",
        procurement_status=0,
        is_back=0,
        is_deleted=0,
    ),
    Procurement(
        procurement_id=2,
        procurement_name="abc",
        procurement_status=1,
        is_back=0,
        is_deleted=0,
    ),
    Procurement(
        procurement_id=3,
        procurement_name="ecccc",
        procurement_status=1,
        is_back=0,
        is_deleted=0,
    ),
)
arrival = (
    Arrival(
        arrival_id=1,
        is_asset=1,
        inspection_status=0,
        inspection_account_id=1,
        asset_approve_account_id=1,
        failure_action=2,
        item_id=2,
        base_id=1,
        arrival_type=0,
        is_deleted=0,
    ),
    Arrival(
        arrival_id=2,
        is_asset=1,
        inspection_status=0,
        inspection_account_id=1,
        asset_approve_account_id=1,
        failure_action=2,
        item_id=2,
        base_id=1,
        arrival_type=0,
        is_deleted=0,
    ),
    Arrival(
        arrival_id=3,
        is_asset=1,
        inspection_status=0,
        inspection_account_id=1,
        asset_approve_account_id=1,
        failure_action=2,
        item_id=2,
        base_id=1,
        arrival_type=0,
        is_deleted=0,
    ),
)
asset = (
    Asset(
        asset_id=1,
        asset_name_kana="abc",
        asset_status=0,
        asset_type=0,
        asset_from="2023-01-17",
        asset_to="2023-01-28",
        arrival_id=1,
        is_deleted=0,
    ),
    Asset(
        asset_id=2,
        asset_name_kana="ecccc",
        asset_status=0,
        asset_type=0,
        asset_from="2023-01-12",
        asset_to="2023-01-20",
        arrival_id=2,
        is_deleted=0,
    ),
    Asset(
        asset_id=3,
        asset_name_kana="abc",
        asset_status=0,
        asset_type=0,
        asset_from="2023-01-19",
        asset_to="2023-01-28",
        arrival_id=3,
        is_deleted=0,
    ),
)
order = (
    Order(
        order_id=1, procurement_id=1, item_id=2, quantity=2, amount=200, is_deleted=0
    ),
    Order(
        order_id=2, procurement_id=2, item_id=1, quantity=2, amount=100, is_deleted=0
    ),
    Order(
        order_id=3, procurement_id=3, item_id=3, quantity=7, amount=150, is_deleted=0
    ),
)

session.add_all(account)
session.add_all(base_master)
session.add_all(maker)
session.add_all(item_master)
session.add_all(procurement)
session.add_all(arrival)
session.add_all(asset)
session.add_all(order)
session.commit()
