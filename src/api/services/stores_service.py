from sqlalchemy.orm import joinedload
from api.models.models import StoresMaster, VehiclesMaster
from sqlalchemy.sql import func
from api.models import session
from api.messages import MessageResponse
from api.utils.utils import add_update_object, object_as_dict, paginate, export, format_day_and_bool_dict

message_stores_constant = MessageResponse()
message_stores_constant.setName("Stores")


def get_stores_list(query_params):
    """
    Get all record for stores by params.

    Argument:
        query_params: param search
    Returns:
        Response: Returning a message, lists.
    """
    try:
        result_list = session.query(StoresMaster).all()
        stores_list = [object_as_dict(order)
                       for order in result_list]

        # Paginate by pageNum & pageSize
        paginated_lst = paginate(stores_list, query_params)
        return True, {
            "stores_list": paginated_lst,
            "totalRecords": len(stores_list),
            "message": message_stores_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200
        }
    except Exception as e:
        return False, {
            "message": str(e),
            "status": 500
        }


def create_stores(query_params):
    """
    Create request and add record for base.

    Argument:
        base_obj: request body
    Returns:
        The message.
    """
    stores_id = query_params.get("storeId")

    # Check if the stores exists in the database
    existing_stores = session.query(StoresMaster).filter(
        StoresMaster.storeId == stores_id
    ).first()

    if existing_stores:
        return (False, "stores already exists")

    shipping = StoresMaster()
    session.add(add_update_object(query_params, shipping))
    session.commit()

    return (True, message_stores_constant.MESSAGE_SUCCESS_CREATED)


def update_stores(query_params):
    """
    update 1 record for stores by id.

    Arguments:
        prefecture_obj: json body
    Returns:
        Response: Returning a message.
    """
    stores_id = query_params.get("storeId")

    # Check if the stores exists in the database
    existing_stores = session.query(StoresMaster).filter(
        StoresMaster.storeId == stores_id
    ).first()
    if existing_stores:
        # Update the existing stores object
        add_update_object(query_params, existing_stores)

        session.commit()

        return True, message_stores_constant.MESSAGE_SUCCESS_UPDATED
    else:
        return False, message_stores_constant.MESSAGE_ERROR_NOT_EXIST


def delete_stores(query_params):
    """
    Delete 1 record for stores by id.

    Argument:
        query_params: parameter
    Returns:
        The message.
    """
    stores_id = query_params.get("storeId")

    # Cập nhật các vehicle liên quan
    vehicle_has_stores_id = session.query(VehiclesMaster).filter(
        VehiclesMaster.storeId == stores_id
    ).all()

    for vehicle in vehicle_has_stores_id:
        if vehicle.storeId == stores_id:
            vehicle.storeId = None

    stores = session.query(StoresMaster).filter(
        StoresMaster.storeId == stores_id
    ).first()

    if stores is None:
        return (False, message_stores_constant.MESSAGE_ERROR_NOT_EXIST)

    session.delete(stores)
    session.commit()

    return True, {
        "message": message_stores_constant.MESSAGE_SUCCESS_DELETED,
        "status": 200
    }
