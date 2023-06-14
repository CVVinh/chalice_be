from api.models import session
from api.models.models import Prefecture
from api.utils.utils import add_update_object, paginate
from api.messages import MessageResponse

message_prefecture_constant = MessageResponse()
message_prefecture_constant.setName("Prefecture")


def get_prefecture_list(query_params):
    """
    Get all record for prefecture by params.

    Argument:
        query_params: param search
    Returns:
        Response: Returning a message, lists.
    """
    # Get list perfecture
    list_prefecture_master = session.query(Prefecture).all()

    prefecture_list = []
    for prefecture in list_prefecture_master:
        tmp_prefecture = {
            'prefId': prefecture.prefId,
            'prefName': prefecture.prefName
        }
        prefecture_list.append(tmp_prefecture)

    # Paginate by pageNum & pageSize
    paginated_list = paginate(prefecture_list, query_params)

    return (True, {
        "mstPrefecture": paginated_list,
        "total": len(prefecture_list),
        "msg": message_prefecture_constant.MESSAGE_SUCCESS_GET_LIST,
        "status": 200
    })


def add_prefecture(prefecture_obj):
    """
    Create request and add record for base.

    Argument:
        base_obj: request body
    Returns:
        The message.
    """
    prefecture_name = prefecture_obj.get("prefName")

    # Find the prefecture name with prefecture_name in the database
    check_prefecture_name = session.query(Prefecture) \
        .filter(Prefecture.prefName == prefecture_name) \
        .first()

    # If the prefecture name already exists, return a message
    if check_prefecture_name is not None:
        return (False, "This prefecture name already exists!")

    create_prefecture = Prefecture()
    session.add(add_update_object(prefecture_obj, create_prefecture))
    session.commit()
    return (True, message_prefecture_constant.MESSAGE_SUCCESS_CREATED)


def update_prefecture(prefecture_obj):
    """
    update 1 record for prefecture by id.

    Arguments:
        prefecture_obj: json body
    Returns:
        Response: Returning a message.
    """
    prefecture_id = prefecture_obj.get("prefId")
    prefecture_name = prefecture_obj.get("prefName")

    # Find the prefecture with prefecture_id in the database
    update_to_prefecture = session.query(Prefecture) \
                                  .filter(Prefecture.prefId == prefecture_id) \
                                  .first()

    # If prefecture is none exist, return a message
    if update_to_prefecture is None:
        return (False, message_prefecture_constant.MESSAGE_ERROR_NOT_EXIST)

    # Fine the prefecture name with prefecture_name in the database
    check_prefecture_name = session.query(Prefecture) \
        .filter(Prefecture.prefName == prefecture_name,
                Prefecture.prefId != prefecture_id) \
        .first()

    # If the prefecture name already exists, return a message
    if check_prefecture_name is not None:
        return (False, "This prefecture name already exists!")

    add_update_object(prefecture_obj, update_to_prefecture)
    session.commit()
    return (True, message_prefecture_constant.MESSAGE_SUCCESS_UPDATED)


def delete_prefecture(query_params):
    """
    Delete 1 record for prefecture by id.

    Argument:
        query_params: parameter
    Returns:
        The message.
    """
    prefecture_id = query_params.get("prefId")

    # Find the prefecture with prefecture_id in the database
    delete_to_prefecture = session.query(Prefecture) \
                                  .filter(Prefecture.prefId == prefecture_id) \
                                  .first()

    # If prefecture is none exist, return a message
    if delete_to_prefecture is None:
        return (False, message_prefecture_constant.MESSAGE_ERROR_NOT_EXIST)

    session.delete(delete_to_prefecture)
    session.commit()
    return (True, message_prefecture_constant.MESSAGE_SUCCESS_DELETED)
