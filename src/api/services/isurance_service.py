# from sqlalchemy.sql import func
from api.models.models import InsurancesMaster
from api.models import session
from api.utils.utils import add_update_object, object_as_dict, export, paginate
from api.messages import MessageResponse

message_isurances_constant = MessageResponse()
message_isurances_constant.setName("Insurances Master")


def add_isurances(isurances_obj):
    """
    Create request and add record for isurances

    Args:
        isurances_obj: request body
    Returns:
        The message
    """
    create_isurances = InsurancesMaster()
    session.add(add_update_object(isurances_obj, create_isurances))
    session.commit()
    return (True, message_isurances_constant.MESSAGE_SUCCESS_CREATED)


def add_multi_isurances(isurances_obj):
    """
    Create request and add many record for isurances

    Args:
        isurances_obj: request body
    Returns:
        The message
    """
    for item in isurances_obj:
        create_isurances = InsurancesMaster()
        session.add(add_update_object(item, create_isurances))
    session.commit()
    return (True, message_isurances_constant.MESSAGE_SUCCESS_CREATED)


def update_isurances_info(isurances_obj):
    """
    update 1 record for isurances by id

    Args:
        isurances_obj: request body
    Returns:
        Response: Returning a message
    """
    isurances_id = isurances_obj.get("insuranceId")
    if (
        update_to_isurances := session.query(InsurancesMaster)
        .filter(InsurancesMaster.insuranceId == isurances_id)
        .first()
    ):
        add_update_object(isurances_obj, update_to_isurances)
        session.commit()
        return (True, message_isurances_constant.MESSAGE_SUCCESS_UPDATED)
    return (False, message_isurances_constant.MESSAGE_ERROR_NOT_EXIST)


def delete_isurances(query_params):
    """
    Delete 1 record for isurances by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    isurances_id = query_params.get("insurance_id")
    if (
        update_to_isurances := session.query(InsurancesMaster)
        .filter(InsurancesMaster.insuranceId == isurances_id)
        .first()
    ):
        session.delete(update_to_isurances)
        session.commit()
        return (True, message_isurances_constant.MESSAGE_SUCCESS_DELETED)
    return (False, message_isurances_constant.MESSAGE_ERROR_NOT_EXIST)


def delete_multi_isurances(query_params):
    """
    Delete many record for isurances by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    for item in query_params:
        if (
            update_to_isurances := session.query(InsurancesMaster)
            .filter(InsurancesMaster.insuranceId == item)
            .first()
        ):
            session.delete(update_to_isurances)
    session.commit()
    return (True, message_isurances_constant.MESSAGE_SUCCESS_DELETED)


def get_isurances_info(query_params):
    """
    get 1 record for isurances by id

    Args:
        query_params: parameter search
    Returns:
        Response: Returning a message and a object inclue obj the isurances
    """
    isurances_id = query_params.get("insurance_id")
    if (
        isurances_info := session.query(InsurancesMaster)
        .filter(InsurancesMaster.insuranceId == isurances_id)
        .first()
    ):
        tmp_isurances_info = {
            "mstIsurances": [{**object_as_dict(isurances_info, True)}],
            "total": 1,
            "message": message_isurances_constant.MESSAGE_SUCCESS_GET_INFO,
            "status": 200,
        }
        return (True, tmp_isurances_info)
    return (False, message_isurances_constant.MESSAGE_ERROR_NOT_EXIST)


def get_isurances_list(query_params):
    """
    Get 1 or many record for isurances by params

    Args:
        query_params: param search
    Returns:
        Response: Returning a message, total record, lists
    """
    filter_param_get_list = filter_param_get_list_isurances(query_params)
    paginated_lst = paginate(filter_param_get_list, query_params)
    return (
        True,
        {
            "mstIsurances": paginated_lst,
            "total": len(paginated_lst),
            "message": message_isurances_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200,
        },
    )


def export_isurances_list(query_params):
    return export(filter_param_get_list_isurances(query_params))


def filter_param_get_list_isurances(query_params):
    """
    Query and search base with parameters

    Args:
        query_params: param search
    Returns:
        Response: Returning a object list
    """
    query_list_isurances = session.query(InsurancesMaster)
    if query_params:
        if "insurance_id" in query_params:
            query_list_isurances = query_list_isurances.filter(
                InsurancesMaster.insuranceId == query_params["insurance_id"]
            )

        if "insurance_name" in query_params:
            query_list_isurances = query_list_isurances.filter(
                InsurancesMaster.insuranceName.like(
                    f"%{query_params['insurance_name']}%"
                )
            )

    return [object_as_dict(item) for item in query_list_isurances.all()]
