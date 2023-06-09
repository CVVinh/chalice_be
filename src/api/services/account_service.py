from sqlalchemy.sql import func
from api.models.models import AccountMaster, BaseMaster, AccountBaseMaster
from api.models import session
from api.utils.utils import add_update_object, paginate
from api.messages import MessageResponse

message_account_constant = MessageResponse()
message_account_constant.setName("Account Master")

message_base_constant = MessageResponse()
message_base_constant.setName("Base Master")

message_account_base_constant = MessageResponse()
message_account_base_constant.setName("Account Base Master")


def get_all_account(query_params):
    """
    Get all account list.

    Argument:
        query_params: parameter
    Returns:
        The message and a list of accounts.
    """

    if query_params is None:
        # Query Column needs to get, join tables containing information to get
        query_list_account = session.query(AccountMaster.accountId, AccountMaster.accountName, BaseMaster.baseId, BaseMaster.baseName) \
                                    .join(AccountBaseMaster, AccountBaseMaster.accountId == AccountMaster.accountId) \
                                    .join(BaseMaster, BaseMaster.baseId == AccountBaseMaster.baseId) \
                                    .filter(AccountMaster.isDeleted == 0)
    else:
        account_id = query_params.get("id")

        # Get account by id
        query_list_account = session.query(AccountMaster.accountId, AccountMaster.accountName
                                           ).filter(AccountMaster.accountId == account_id
                                                    and AccountMaster.isDeleted == 0)

    # Create loop of lists account, assign it to an object and then assign to a new list.
    result_list = [{**account} for account in query_list_account.all()]

    paginated_lst = paginate(result_list, query_params)

    if len(result_list) == 0:
        res_data = {"mstAccount": None,
                    "total": 0,
                    "message": message_account_constant.MESSAGE_ERROR_NOT_EXIST,
                    "status": 404
                    }

        return True, res_data

    # Check exists data or not
    if query_params is None:
        res_data = {"mstAccount": paginated_lst,
                    "total": len(result_list),
                    "message": message_account_constant.MESSAGE_SUCCESS_GET_LIST,
                    "status": 200
                    }
    else:
        res_data = {"accountInfo": result_list[0],
                    "total": 1,
                    "message": message_account_constant.MESSAGE_SUCCESS_GET_INFO,
                    "status": 200
                    }

    return True, res_data


def add_account(account_obj):
    """
    Create request and add record for account.

    Argument:
        account_obj: request body
    Returns:
        The message.
    """
    # get accountName and emailAddress
    account_name = account_obj.get("accountName")
    email_address = account_obj.get("emailAddress")

    # Find the account named account_name in the database
    check_account_name = session.query(AccountMaster) \
                                .filter(AccountMaster.accountName == account_name) \
                                .first()
    # Find the account with email_address in the database
    check_account_email = session.query(AccountMaster) \
                                 .filter(AccountMaster.emailAddress == email_address) \
                                 .first()

    # If the account name already exists, return a message
    if check_account_name is not None:
        return (False, "This account name already exists!")

    # If the email address already exists, return a message
    if check_account_email is not None:
        return (False, "This email address already exists!")

    # Create new account
    create_account = AccountMaster()
    session.add(add_update_object(account_obj, create_account))
    session.commit()
    return (True, message_account_constant.MESSAGE_SUCCESS_CREATED)


def update_account_info(account_obj):
    """
    update 1 record for base by id.

    Arguments:
        account_obj: json body
    Returns:
        Response: Returning a message.
    """
    # Get accountId, accountName and emailAddress information in account_obj
    account_id = account_obj.get("accountId")
    account_name = account_obj.get("accountName")
    email_address = account_obj.get("emailAddress")

    # Find the account with account_id in the database
    update_to_account = session.query(AccountMaster) \
                               .filter(AccountMaster.accountId == account_id, AccountMaster.isDeleted == 0) \
                               .first()

    # If account is none exist, return a message
    if update_to_account is None:
        return (False, message_account_constant.MESSAGE_ERROR_NOT_EXIST)

    # Find the account with account_name in the database
    check_account_name = session.query(AccountMaster) \
                                .filter(AccountMaster.accountName == account_name,
                                        AccountMaster.accountId != update_to_account.accountId) \
                                .first()
    # Find the account with email_address in the database
    check_account_email = session.query(AccountMaster) \
                                 .filter(AccountMaster.emailAddress == email_address,
                                         AccountMaster.accountId != update_to_account.accountId) \
                                 .first()

    # If the account name already exists, return a message
    if check_account_name is not None:
        return (False, "This account name already exists!")

    # If the email address already exists, return a message
    if check_account_email is not None:
        return (False, "This email address already exists!")

    add_update_object(account_obj, update_to_account)
    update_to_account.modifiedAt = func.now()
    session.commit()
    return (True, message_account_constant.MESSAGE_SUCCESS_UPDATED)


def delete_account(query_params):
    """
    Delete 1 record for account by id.

    Argument:
        query_params: parameter
    Returns:
        The message.
    """
    # Get accountId
    account_id = query_params.get("accountId")

    # Find the account with account_id in the database
    delete_to_account = session.query(AccountMaster) \
                               .filter(AccountMaster.accountId == account_id, AccountMaster.isDeleted == 0) \
                               .first()

    # If account is none exist, return a message
    if delete_to_account is None:
        return (False, message_account_constant.MESSAGE_ERROR_NOT_EXIST)

    # Delete the account by updating isDelete to 1 and add time deleteAt
    delete_to_account.isDeleted = 1
    delete_to_account.deletedAt = func.now()

    # Find the account base with account_id in the database
    delete_to_account_base = session.query(AccountBaseMaster) \
                                    .filter(AccountBaseMaster.accountId == delete_to_account.accountId
                                            and AccountBaseMaster.isDeleted == 0)

    # If the account base list is not empty, delete all found account bases
    if delete_to_account_base.first() is not None:
        for account_base in delete_to_account_base.all():
            account_base.isDeleted = 1
            account_base.deletedAt = func.now()

            # Find the base with base id
            delete_to_base = session.query(BaseMaster) \
                                    .filter(BaseMaster.baseId == account_base.baseId) \
                                    .first()

            # Delete all found base
            delete_to_base.isDeleted = 1
            delete_to_base.deletedAt = func.now()

    session.commit()
    return (True, message_account_constant.MESSAGE_SUCCESS_DELETED)


def add_account_base(account_obj):
    """
    Create request and add record for account.

    Argument:
        account_obj: request body
    Returns:
        The message.
    """
    # get accountName and emailAddress
    account_name = account_obj.get("accountName")
    email_address = account_obj.get("emailAddress")

    # Find the account named account_name in the database
    check_account_name = session.query(AccountMaster) \
                                .filter(AccountMaster.accountName == account_name) \
                                .first()
    # Find the account with email_address in the database
    check_account_email = session.query(AccountMaster) \
                                 .filter(AccountMaster.emailAddress == email_address) \
                                 .first()

    # If the account name already exists, return a message
    if check_account_name is not None:
        return (False, "This account name already exists!")

    # If the email address already exists, return a message
    if check_account_email is not None:
        return (False, "This email address already exists!")

    # Save data account to account_data
    account_data = {
        "accountCd": account_obj.get("accountCd"),
        "extAccountId": account_obj.get("extAccountId"),
        "accountName": account_name,
        "emailAddress": email_address,
    }
    create_at_account = func.now()

    # Create new account
    create_account = AccountMaster()
    session.add(add_update_object(account_data, create_account))

    # Save data base to base_data
    base_data = {
        "baseCd": account_obj.get("baseCd"),
        "baseName": account_obj.get("baseName"),
        "zipCode": account_obj.get("zipCode"),
        "prefCode": account_obj.get("prefCode"),
        "address": account_obj.get("address"),
        "addressee": account_obj.get("addressee"),
        "telephoneNumber": account_obj.get("telephoneNumber"),
        "faxNumber": account_obj.get("faxNumber"),
        "eMailAddress": account_obj.get("eMailAddress"),
        "note": account_obj.get("note")
    }
    create_at_base = func.now()

    # Create new base
    create_base = BaseMaster()
    session.add(add_update_object(base_data, create_base))

    # Find the newly created account
    new_account_id = session.query(AccountMaster) \
                            .filter(AccountMaster.createdAt == create_at_account) \
                            .first()
    # Find the newly created base
    new_base_id = session.query(BaseMaster) \
                         .filter(BaseMaster.createdAt == create_at_base) \
                         .first()

    # Save the accountId and baseId of the base and account just created
    account_base_data = {
        "accountId": new_account_id.accountId,
        "baseId": new_base_id.baseId
    }

    # Create new account base
    create_account_base = AccountBaseMaster()
    session.add(add_update_object(account_base_data, create_account_base))

    session.commit()
    return (True, message_account_constant.MESSAGE_SUCCESS_CREATED)


def update_account_base_info(account_obj):
    """
    update 1 record for base by id.

    Arguments:
        account_obj: json body
    Returns:
        Response: Returning a message.
    """
    # Get accountId, accountName, emailAddress and baseId information in account_obj
    account_id = account_obj.get("accountId")
    account_name = account_obj.get("accountName")
    email_address = account_obj.get("emailAddress")
    base_id = account_obj.get("baseId")

    # Find the account with account_id in the database
    update_to_account = session.query(AccountMaster) \
                               .filter(AccountMaster.accountId == account_id, AccountMaster.isDeleted == 0) \
                               .first()

    # If account is none exist, return a message
    if update_to_account is None:
        return (False, message_account_constant.MESSAGE_ERROR_NOT_EXIST)

    # Find the account base with base_id in the database
    check_account_base = session.query(AccountBaseMaster) \
                                .filter(AccountBaseMaster.accountId == account_id
                                        and AccountBaseMaster.baseId == base_id
                                        and AccountBaseMaster.isDeleted == 0) \
                                .first()

    # If account base is none exist, return a message
    if check_account_base is None:
        return (False, message_account_base_constant.MESSAGE_ERROR_NOT_EXIST)

    # Find the base with base_id in the database
    update_to_base = session.query(BaseMaster) \
                            .filter(BaseMaster.baseId == base_id, BaseMaster.isDeleted == 0) \
                            .first()

    # If base is none exist, return a message
    if update_to_base is None:
        return (False, message_base_constant.MESSAGE_ERROR_NOT_EXIST)

    # Find the account with account_name in the database
    check_account_name = session.query(AccountMaster) \
                                .filter(AccountMaster.accountName == account_name,
                                        AccountMaster.accountId != update_to_account.accountId) \
                                .first()
    # Find the account with email_address in the database
    check_account_email = session.query(AccountMaster) \
                                 .filter(AccountMaster.emailAddress == email_address,
                                         AccountMaster.accountId != update_to_account.accountId) \
                                 .first()

    # If the account name already exists, return a message
    if check_account_name is not None:
        return (False, "This account name already exists!")

    # If the email address already exists, return a message
    if check_account_email is not None:
        return (False, "This email address already exists!")

    # Save data account to account_data
    account_data = {
        "extAccountId": account_obj.get("extAccountId"),
        "accountName": account_name,
        "emailAddress": email_address,
    }

    # Update account
    add_update_object(account_data, update_to_account)
    update_to_account.modifiedAt = func.now()

    # Save data base to base_data
    base_data = {
        "baseCd": account_obj.get("baseCd"),
        "baseName": account_obj.get("baseName"),
        "zipCode": account_obj.get("zipCode"),
        "prefCode": account_obj.get("prefCode"),
        "address": account_obj.get("address"),
        "addressee": account_obj.get("addressee"),
        "telephoneNumber": account_obj.get("telephoneNumber"),
        "faxNumber": account_obj.get("faxNumber"),
        "eMailAddress": account_obj.get("eMailAddress"),
        "note": account_obj.get("note")
    }

    # Update base
    add_update_object(base_data, update_to_base)
    update_to_base.modifiedAt = func.now()

    session.commit()
    return (True, message_account_constant.MESSAGE_SUCCESS_UPDATED)
