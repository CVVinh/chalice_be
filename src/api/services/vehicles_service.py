from api.models.models import VehiclesMaster, StoresMaster, MakersMaster
from api.models.models import ModelsMaster
from api.models import session
from api.messages import MessageResponse
from api.utils.utils import add_update_object, object_as_dict, paginate

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
    # Get data of list in DB and combine
    try:
        vehicles_list = session.query(VehiclesMaster).all()
        stores_list = session.query(StoresMaster).all()
        makers_list = session.query(MakersMaster).all()
        model_list = session.query(ModelsMaster).all()

        combined_result = combine_vehicles_and_detail(
            vehicles_list, stores_list, makers_list, model_list)
        # Paginate by pageNum & pageSize
        paginated_lst = paginate(combined_result, query_params)
        return {
            "vehicles_list": paginated_lst,
            "totalRecords": len(combined_result),
            "message": message_vehicles_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": 500
        }

# Merge VehiclesMaster & StoresMaster & MakersMaster


def combine_vehicles_and_detail(vehicles_list, stores_list,
                                makers_list, model_list):
    """
    Get all record of VehiclesMaster & StoresMaster & MakersMaster .

    Arguments:
        vehicles_list: A list of VehicleMaster objects.
        stores_list: A list of StoresMaster objects.
        makers_list: A list of MakersMaster objects.

    Returns:
        combined_list:  combined info of vehicles, stores, and makers.
    """
    combined_list = []
    # Combine value if it match with vehicles.storeId, makerId
    for vehicles in vehicles_list:
        vehicles_dict = object_as_dict(vehicles)
        vehicles_dict['stores_list'] = []
        vehicles_dict['makers_list'] = []
        vehicles_dict['model_list'] = []

        for stores in stores_list:
            if stores.storeId == vehicles.storeId:
                stores_dict = object_as_dict(stores)
                vehicles_dict['stores_list'].append(stores_dict)

        for makers in makers_list:
            if makers.makerId == vehicles.makerId:
                makers_dict = object_as_dict(makers)
                vehicles_dict['makers_list'].append(makers_dict)

        for models in model_list:
            if models.modelId == vehicles.vehicleModel:
                model_dict = object_as_dict(models)
                vehicles_dict['model_list'].append(model_dict)

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

    vehicle = VehiclesMaster()
    # vehicle_image = VehicleImage()
    # vehicle_image.vehicleId = vehicle.vehicleId
    # vehicle_image.image = "img/" + query_params.get("image")
    session.add(add_update_object(query_params, vehicle))
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
    # Check if the vehicles exists in the database
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


def get_vehicle_by_id(query_params):
    """
    get 1 record for vehicle by id.

    Arguments:
        query_params: parameter
    Returns:
        Response: Returning a message.
    """
    # Get vehicleId from query_params
    vehicles_id = query_params.get("vehicleId")

    # Check if the vehicles exists in the database
    existing_vehicles = session.query(VehiclesMaster) \
        .filter(VehiclesMaster.vehicleId == vehicles_id).first()
    if existing_vehicles:
        # Create an empty combined_list
        combined_list = []

        # Save object list to vehicles_dict
        vehicles_dict = object_as_dict(existing_vehicles)

        # Create an empty Stores_list and makers_list object list
        vehicles_dict['stores_list'] = []
        vehicles_dict['makers_list'] = []

        # Find store in StoresMaster table with storeId
        store = session.query(StoresMaster).filter(
            StoresMaster.storeId == existing_vehicles.storeId).first()

        # Find maker in MakersMaster table with makerId
        maker = session.query(MakersMaster).filter(
            MakersMaster.makerId == existing_vehicles.makerId).first()

        # Save store and maker to vehicles_dict
        stores_dict = object_as_dict(store)
        vehicles_dict['stores_list'].append(stores_dict)
        makers_dict = object_as_dict(maker)
        vehicles_dict['makers_list'].append(makers_dict)

        # Save vehicles_dict to combined_list
        combined_list.append(vehicles_dict)

        return {
            "vehicles_list": combined_list,
            "message": message_vehicles_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200
        }
    else:
        return False, message_vehicles_constant.MESSAGE_ERROR_NOT_EXIST


def get_vehicle_by_params(query_params):
    """
    get vehicles records by makerId and storeId.

    Arguments:
        query_params: parameters
    Returns:
        Response: Returning a message.
    """
    storeId = query_params.get("storeId")
    vehicleModel = query_params.get("vehicleModel")
    vehicleSeat = query_params.get("vehicleSeat")
    makerId = query_params.get("makerId")
 
    # Join the tables to fetch the required data
    query = session.query(VehiclesMaster, StoresMaster,
                          MakersMaster, ModelsMaster) \
        .join(StoresMaster, VehiclesMaster.storeId == StoresMaster.storeId) \
        .join(MakersMaster, VehiclesMaster.makerId == MakersMaster.makerId) \
        .join(ModelsMaster, VehiclesMaster.vehicleModel
              == ModelsMaster.modelId) \

    # If storeId, vehicleSeat,makerId is !null
    if storeId:
        query = query.filter(VehiclesMaster.storeId == storeId)

    if vehicleModel:
        query = query.filter(VehiclesMaster.vehicleModel == vehicleModel)

    if vehicleSeat:
        query = query.filter(VehiclesMaster.vehicleSeat == vehicleSeat)

    if makerId:
        query = query.filter(VehiclesMaster.makerId == makerId)

    # Execute the query to fetch the results
    result = query.all()

    if result:
        combined_list = []

        for vehicle, store, model, maker in result:
            vehicles_dict = object_as_dict(vehicle)
            vehicles_dict['stores_list'] = [object_as_dict(store)]
            vehicles_dict['models_list'] = [object_as_dict(model)]
            vehicles_dict['makers_list'] = [object_as_dict(maker)]
            combined_list.append(vehicles_dict)

        return {
            "vehicles_list": combined_list,
            "totalRecords": len(combined_list),
            "message": message_vehicles_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200
        }
    else:
        return {
            "vehicles_list": [],
            "message": message_vehicles_constant.MESSAGE_ERROR_NOT_EXIST,
            "status": 404
        }
