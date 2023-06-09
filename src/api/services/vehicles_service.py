from sqlalchemy.orm import joinedload
from api.models.models import VehiclesMaster, StoresMaster, MakersMaster
from sqlalchemy.sql import func
from api.models import session
from api.messages import MessageResponse
from api.utils.utils import add_update_object, object_as_dict, paginate, export, format_day_and_bool_dict

message_vehicles_constant = MessageResponse()
message_vehicles_constant.setName("Vehicles")


def get_vehicles_list(query_params):
    """
    Get all record for vehicles by params.

    Argument:
        query_params: param search
    Returns:
        Response: Returning a message, lists.
    """
    try:
        vehicles_list = session.query(VehiclesMaster).all()
        stores_list = session.query(StoresMaster).all()
        makers_list = session.query(MakersMaster).all()

        combined_result = combine_vehicles_and_detail(
            vehicles_list, stores_list, makers_list)
        # Paginate by pageNum & pageSize
        paginated_lst = paginate(combined_result, query_params)
        return True, {
            "vehicles_list": paginated_lst,
            "totalRecords": len(combined_result),
            "message": message_vehicles_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200
        }
    except Exception as e:
        return False, {
            "message": str(e),
            "status": 500
        }

# Merge VehiclesMaster & StoresMaster & MakersMaster


def combine_vehicles_and_detail(vehicles_list, stores_list, makers_list):
    """
    Get all record of VehiclesMaster & StoresMaster & MakersMaster .

    Arguments:
        vehicles_list: A list of VehicleMaster objects.
        stores_list: A list of StoresMaster objects.
        makers_list: A list of MakersMaster objects.

    Returns:
        combined_list: A list of dictionaries containing the combined information of vehicles, stores, and makers.
    """
    combined_list = []

    for vehicles in vehicles_list:
        vehicles_dict = object_as_dict(vehicles)
        vehicles_dict['stores_list'] = []
        vehicles_dict['makers_list'] = []

        for stores in stores_list:
            if stores.storeId == vehicles.storeId:
                stores_dict = object_as_dict(
                    stores)
                vehicles_dict['stores_list'].append(
                    stores_dict)

        for makers in makers_list:
            if makers.makerId == vehicles.makerId:
                makers_dict = object_as_dict(
                    makers)
                vehicles_dict['makers_list'].append(
                    makers_dict)

        combined_list.append(vehicles_dict)

    return combined_list


def create_vehicles(query_params):
    """
    Create request and add record for base.

    Argument:
        base_obj: request body
    Returns:
        The message.
    """
    vehicles_id = query_params.get("vehicleId")

    # Check if the vehicles exists in the database
    existing_vehicles = session.query(VehiclesMaster).filter(
        VehiclesMaster.vehicleId == vehicles_id
    ).first()

    if existing_vehicles:
        return (False, "Vehicles already exists")

    shipping = VehiclesMaster()
    session.add(add_update_object(query_params, shipping))
    session.commit()

    return (True, message_vehicles_constant.MESSAGE_SUCCESS_CREATED)


def update_vehicles(query_params):
    """
    update 1 record for vehicle by id.

    Arguments:
        prefecture_obj: json body
    Returns:
        Response: Returning a message.
    """
    vehicles_id = query_params.get("vehicleId")

    # Check if the vehicles exists in the database
    existing_vehicles = session.query(VehiclesMaster).filter(
        VehiclesMaster.vehicleId == vehicles_id
    ).first()
    if existing_vehicles:
        # Update the existing vehicles object
        add_update_object(query_params, existing_vehicles)

        session.commit()

        return True, message_vehicles_constant.MESSAGE_SUCCESS_UPDATED
    else:
        return False, message_vehicles_constant.MESSAGE_ERROR_NOT_EXIST


def delete_vehicles(query_params):
    """
    Delete 1 record for vehicle by id.

    Argument:
        query_params: parameter
    Returns:
        The message.
    """
    vehicles_id = query_params.get("vehicleId")

    vehicles = session.query(VehiclesMaster).filter(
        VehiclesMaster.vehicleId == vehicles_id
    ).first()

    if vehicles is None:
        return (False, message_vehicles_constant.MESSAGE_ERROR_NOT_EXIST)

    session.delete(vehicles)
    session.commit()

    return True, {
        "message": message_vehicles_constant.MESSAGE_SUCCESS_DELETED,
        "status": 200
    }
