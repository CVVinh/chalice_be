from sqlalchemy.sql import func
from api.models.models import BaseMaster, AccountBaseMaster, AccountMaster
from api.models import session
from api.utils.utils import add_update_object, object_as_dict, export, paginate
from api.messages import MessageResponse

message_base_constant = MessageResponse()
message_base_constant.setName("Base Master")


def add_base(base_obj):
    """
    Create request and add record for base and account base.

    Argument:
        base_obj: request body
    Returns:
        The message.
    """
    create_base = BaseMaster()

    # Save data to base_data
    base_data = {
        "baseCd": base_obj.get("baseCd"),
        "baseName": base_obj.get("baseName"),
        "zipCode": base_obj.get("zipCode"),
        "prefCode": base_obj.get("prefCode"),
        "address": base_obj.get("address"),
        "addressee": base_obj.get("addressee"),
        "telephoneNumber": base_obj.get("telephoneNumber"),
        "faxNumber": base_obj.get("faxNumber"),
        "eMailAddress": base_obj.get("eMailAddress"),
        "note": base_obj.get("note"),
    }
    # Get the creation time
    create_at = func.now()

    # Create new base
    session.add(add_update_object(base_data, create_base))

    # Find the newly created base
    new_base_id = (
        session.query(BaseMaster).filter(
            BaseMaster.createdAt == create_at).first()
    )

    # Save the accountId and baseId of the base just created
    account_base_data = {
        "accountId": base_obj.get("accountId"),
        "baseId": new_base_id.baseId,
    }

    # Create new account base
    create_account_base = AccountBaseMaster()
    session.add(add_update_object(account_base_data, create_account_base))
    session.commit()
    return (True, message_base_constant.MESSAGE_SUCCESS_CREATED)


def update_base_info(base_obj):
    """
    update 1 record for base by id.

    Arguments:
        base_obj: json body
    Returns:
        Response: Returning a message.
    """
    # Get baseId from base_obj
    base_id = base_obj.get("baseId")

    # Search base with baseId
    update_to_base = (
        session.query(BaseMaster)
        .filter(BaseMaster.baseId == base_id, BaseMaster.isDeleted == 0)
        .first()
    )
    # If base exists then update that base and return message
    if update_to_base:
        # Update base
        add_update_object(base_obj, update_to_base)
        update_to_base.modifiedAt = func.now()
        session.commit()
        return (True, message_base_constant.MESSAGE_SUCCESS_UPDATED)
    return (False, message_base_constant.MESSAGE_ERROR_NOT_EXIST)


def delete_base(query_params):
    """
    Delete 1 record for base by id.

    Argument:
        query_params: parameter
    Returns:
        The message.
    """
    # Get baseId
    base_id = query_params.get("baseId")

    # Search base with baseId
    delete_to_base = (
        session.query(BaseMaster)
        .filter(BaseMaster.baseId == base_id, BaseMaster.isDeleted == 0)
        .first()
    )

    # If base id exists then delete that base id and return message
    if delete_to_base:
        # Delete base
        delete_to_base.isDeleted = True
        delete_to_base.deletedAt = func.now()

        # Search all account base whose baseId matches the baseId just deleted
        delete_to_account_base = (
            session.query(AccountBaseMaster)
            .filter(AccountBaseMaster.baseId == delete_to_base.baseId)
            .all()
        )

        # Delete all found account base
        for base in delete_to_account_base:
            base.isDeleted = 1
            base.deletedAt = func.now()

        return (True, message_base_constant.MESSAGE_SUCCESS_DELETED)
    return (False, message_base_constant.MESSAGE_ERROR_NOT_EXIST)


def get_base_info(query_params):
    """
    get 1 record for base by id.

    Arguments:
        query_params: param search
    Returns:
        Response: Returning a message and a object include.
    """
    # Get baseId
    base_id = query_params.get("baseId")

    # Search base with base_id
    base_info = session.query(BaseMaster).filter(
        BaseMaster.baseId == base_id).first()

    # if base id exists then get that base id info and return message
    if base_info:
        tmp_base_info = {
            **object_as_dict(base_info, True),
            "message": message_base_constant.MESSAGE_SUCCESS_GET_INFO,
            "status": 200,
        }
        return (True, tmp_base_info)
    return (False, message_base_constant.MESSAGE_ERROR_NOT_EXIST)


def get_base_list(query_params):
    """
    Get 1 or many record for base by params.

    Argument:
        query_params: param search
    Returns:
        Response: Returning a message, total record, lists.
    """
    # Paginate by pageNum & pageSize
    filter_param_get_list = filter_param_get_list_base(query_params)
    paginated_lst = paginate(filter_param_get_list, query_params)
    return (
        True,
        {
            "mstBase": paginated_lst,
            "total": len(filter_param_get_list),
            "message": message_base_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200,
        },
    )


def export_base_list(query_params):
    return export(filter_param_get_list_base(query_params))


def filter_param_get_list_base(query_params):
    """
    Query and search base with parameters

    Arguments:
        query_params: param search
    Returns:
        List: Returning a list object.
    """

    # Query Column needs to get, join tables containing information to get
    query_list_base = session.query(BaseMaster)
    if query_params:
        params_search_base = ["baseId", "prefCode"]

        # Search for params that exist in BaseMaster
        for param in params_search_base:
            if param in query_params:
                query_list_base = query_list_base.filter(
                    getattr(BaseMaster, param) == query_params[param]
                )

        # Search Base with baseName
        if "baseName" in query_params:
            query_list_base = query_list_base.filter(
                BaseMaster.baseName.like(f"%{query_params['baseName']}%")
            )

        # If the deleted record display mode is 0, search for undeleted record
        if query_params.get("deletedRecordDisplayMode") == "0":
            query_list_base = query_list_base.filter(BaseMaster.isDeleted == 0)
    else:
        query_list_base = query_list_base.filter(BaseMaster.isDeleted == 0)

    return [object_as_dict(base) for base in query_list_base.all()]


def get_base_user_info(query_params):
    """_summary_

    get 1 record for account and base by id account
    Arguments:
        query_params: param search
    Returns:
        Response: Returning a message and a object include obj
    """

    # Query Column needs to get, join tables containing information to get
    account_id = query_params.get("accountId")
    query_list_account = (
        session.query(
            AccountMaster.accountId,
            BaseMaster.baseId,
            BaseMaster.baseName,
            BaseMaster.prefCode,
            BaseMaster.address,
            BaseMaster.addressee,
            BaseMaster.eMailAddress,
            BaseMaster.telephoneNumber,
            BaseMaster.faxNumber,
        )
        .join(
            AccountBaseMaster,
            AccountMaster.accountId == AccountBaseMaster.accountId,
            isouter=True,
        )
        .join(BaseMaster, AccountBaseMaster.baseId == BaseMaster.baseId,
              isouter=True)
        .filter(AccountMaster.accountId == account_id)
        .distinct()
    )

    result_list = [{**account}  # type: ignore
                   for account in query_list_account.all()]
    return (
        True,
        {
            "mstBaseUser": result_list,
            "message": message_base_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200,
        },
    )
