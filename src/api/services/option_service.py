from api.models.models import OptionsMaster
from api.models import session
from api.utils.utils import add_update_object, object_as_dict, export, paginate
from api.messages import MessageResponse

message_option_constant = MessageResponse()
message_option_constant.setName("Options Master")


def add_option(option_obj):
    """
    Create request and add record for option

    Args:
        option_obj: request body
    Returns:
        The message
    """
    create_option = OptionsMaster()
    session.add(add_update_object(option_obj, create_option))
    session.commit()
    return (True, message_option_constant.MESSAGE_SUCCESS_CREATED)


def add_multi_option(option_obj):
    """
    Create request and add many record for option

    Args:
        option_obj: request body
    Returns:
        The message
    """
    for item in option_obj:
        create_option = OptionsMaster()
        session.add(add_update_object(item, create_option))
    session.commit()
    return (True, message_option_constant.MESSAGE_SUCCESS_CREATED)


def update_option_info(option_obj):
    """
    update 1 record for option by id

    Args:
        option_obj: request body
    Returns:
        Response: Returning a message
    """
    option_id = option_obj.get("optionId")
    if (
        update_to_option := session.query(OptionsMaster)
        .filter(OptionsMaster.optionId == option_id)
        .first()
    ):
        add_update_object(option_obj, update_to_option)
        session.commit()
        return (True, message_option_constant.MESSAGE_SUCCESS_UPDATED)
    return (False, message_option_constant.MESSAGE_ERROR_NOT_EXIST)


def delete_option(query_params):
    """
    Delete 1 record for option by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    option_id = query_params.get("option_id")
    if (
        update_to_option := session.query(OptionsMaster)
        .filter(OptionsMaster.optionId == option_id)
        .first()
    ):
        session.delete(update_to_option)
        session.commit()
        return (True, message_option_constant.MESSAGE_SUCCESS_DELETED)
    return (False, message_option_constant.MESSAGE_ERROR_NOT_EXIST)


def delete_multi_option(query_params):
    """
    Delete many record for option by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    for item in query_params:
        if (
            update_to_option := session.query(OptionsMaster)
            .filter(OptionsMaster.optionId == item)
            .first()
        ):
            session.delete(update_to_option)
    session.commit()
    return (True, message_option_constant.MESSAGE_SUCCESS_DELETED)


def get_option_info(query_params):
    """
    get 1 record for option by id

    Args:
        query_params: parameter search
    Returns:
        Response: Returning a message and a object inclue obj the option
    """
    option_id = query_params.get("option_id")
    if (
        option_info := session.query(OptionsMaster)
        .filter(OptionsMaster.optionId == option_id)
        .first()
    ):
        tmp_option_info = {
            **object_as_dict(option_info, True),
            "message": message_option_constant.MESSAGE_SUCCESS_GET_INFO,
            "status": 200,
        }
        return (True, tmp_option_info)
    return (False, message_option_constant.MESSAGE_ERROR_NOT_EXIST)


def get_option_list(query_params):
    """
    Get 1 or many record for option by params

    Args:
        query_params: param search
    Returns:
        Response: Returning a message, total record, lists
    """
    filter_param_get_list = filter_param_get_list_option(query_params)
    paginated_lst = paginate(filter_param_get_list, query_params)
    return (
        True,
        {
            "mstOptions": paginated_lst,
            "total": len(paginated_lst),
            "message": message_option_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200,
        },
    )


def export_option_list(query_params):
    return export(filter_param_get_list_option(query_params))


def filter_param_get_list_option(query_params):
    """
    Query and search base with parameters

    Args:
        query_params: param search
    Returns:
        Response: Returning a object list
    """
    query_list_option = session.query(OptionsMaster)
    if query_params:
        if "option_id" in query_params:
            query_list_option = query_list_option.filter(
                OptionsMaster.optionId == query_params["option_id"]
            )

        if "option_name" in query_params:
            query_list_option = query_list_option.filter(
                OptionsMaster.optionName.like(
                    f"%{query_params['option_name']}%")
            )

    return [object_as_dict(option) for option in query_list_option.all()]
