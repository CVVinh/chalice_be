from sqlalchemy.orm import joinedload
from api.models.models import MakersMaster, VehiclesMaster
from sqlalchemy.sql import func
from api.models import session
from api.messages import MessageResponse
from api.utils.utils import add_update_object, object_as_dict, paginate, export, format_day_and_bool_dict

message_makers_constant = MessageResponse()
message_makers_constant.setName("Makers")


def get_makers_list(query_params):
    """
    Get all record for makers by params.

    Argument:
        query_params: param search
    Returns:
        Response: Returning a message, lists.
    """
    try:
        result_list = session.query(MakersMaster).all()
        makers_list = [object_as_dict(order)
                       for order in result_list]

        # Paginate by pageNum & pageSize
        paginated_lst = paginate(makers_list, query_params)
        return {
            "makers_list": paginated_lst,
            "totalRecords": len(makers_list),
            "message": message_makers_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": 500
        }


def create_makers(query_params):
    """
    Create request and add record for base.

    Argument:
        base_obj: request body
    Returns:
        The message.
    """
    makers_id = query_params.get("makerId")

    # Check if the makers exists in the database
    existing_makers = session.query(MakersMaster).filter(
        MakersMaster.makerId == makers_id
    ).first()

    if existing_makers:
        return (False, "makers already exists")

    shipping = MakersMaster()
    session.add(add_update_object(query_params, shipping))
    session.commit()

    return (True, message_makers_constant.MESSAGE_SUCCESS_CREATED)


def update_makers(query_params):
    """
    update 1 record for makers by id.

    Arguments:
        prefecture_obj: json body
    Returns:
        Response: Returning a message.
    """
    makers_id = query_params.get("makerId")

    # Check if the makers exists in the database
    existing_makers = session.query(MakersMaster).filter(
        MakersMaster.makerId == makers_id
    ).first()
    if existing_makers:
        # Update the existing makers object
        add_update_object(query_params, existing_makers)

        session.commit()

        return True, message_makers_constant.MESSAGE_SUCCESS_UPDATED
    else:
        return False, message_makers_constant.MESSAGE_ERROR_NOT_EXIST


def delete_makers(query_params):
    """
    Delete 1 record for makers by id.

    Argument:
        query_params: parameter
    Returns:
        The message.
    """
    makers_id = query_params.get("makerId")

    # Cập nhật các vehicle liên quan
    vehicle_has_maker_id = session.query(VehiclesMaster).filter(
        VehiclesMaster.makerId == makers_id
    ).all()

    for vehicle in vehicle_has_maker_id:
        if vehicle.makerId == makers_id:
            vehicle.makerId = None

    makers = session.query(MakersMaster).filter(
        MakersMaster.makerId == makers_id
    ).first()

    if makers is None:
        return (False, message_makers_constant.MESSAGE_ERROR_NOT_EXIST)

    session.delete(makers)
    session.commit()

    return True, {
        "message": message_makers_constant.MESSAGE_SUCCESS_DELETED,
        "status": 200
    }
