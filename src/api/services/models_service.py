from api.models.models import ModelsMaster, VehiclesMaster
from api.models import session
from api.messages import MessageResponse
from api.utils.utils import add_update_object, object_as_dict, paginate

message_models_constant = MessageResponse()
message_models_constant.setName("Models")


def get_models_list(query_params):
    """
    Get all record for Models by params.

    Argument:
        query_params: param search
    Returns:
        Response: Returning a message, lists.
    """
    # Get data of list in DB
    try:
        result_list = session.query(ModelsMaster).all()
        models_list = [object_as_dict(model)
                       for model in result_list]

        # Paginate by pageNum & pageSize
        paginated_lst = paginate(models_list, query_params)
        return {
            "models_list": paginated_lst,
            "totalRecords": len(models_list),
            "message": message_models_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": 500
        }


def create_models(query_params):
    """
    Create request and add record for base.

    Argument:
        base_obj: request body
    Returns:
        The message.
    """
    Models_id = query_params.get("modelId")

    # Check if the Models exists in the database
    existing_models = session.query(ModelsMaster).filter(
        ModelsMaster.modelId == Models_id
    ).first()

    if existing_models:
        return (False, "Models already exists")

    shipping = ModelsMaster()
    session.add(add_update_object(query_params, shipping))
    session.commit()

    return (True, message_models_constant.MESSAGE_SUCCESS_CREATED)


def update_models(query_params):
    """
    update 1 record for Models by id.

    Arguments:
        prefecture_obj: json body
    Returns:
        Response: Returning a message.
    """
    Models_id = query_params.get("modelId")

    # Check if the Models exists in the database
    existing_models = session.query(ModelsMaster).filter(
        ModelsMaster.modelId == Models_id
    ).first()
    if existing_models:
        # Update the existing Models object
        add_update_object(query_params, existing_models)

        session.commit()

        return True, message_models_constant.MESSAGE_SUCCESS_UPDATED
    else:
        return False, message_models_constant.MESSAGE_ERROR_NOT_EXIST


def delete_models(query_params):
    """
    Delete 1 record for Models by id.

    Argument:
        query_params: parameter
    Returns:
        The message.
    """
    Models_id = query_params.get("modelId")

    # Set vehicle.modelId = None if it match with Models_id
    vehicle_has_model_id = session.query(VehiclesMaster).filter(
        VehiclesMaster.vehicleModel == Models_id
    ).all()

    for vehicle in vehicle_has_model_id:
        if vehicle.vehicleModel == Models_id:
            vehicle.vehicleModel = None

    Models = session.query(ModelsMaster).filter(
        ModelsMaster.modelId == Models_id
    ).first()

    if Models is None:
        return (False, message_models_constant.MESSAGE_ERROR_NOT_EXIST)

    session.delete(Models)
    session.commit()

    return True, {
        "message": message_models_constant.MESSAGE_SUCCESS_DELETED,
        "status": 200
    }
