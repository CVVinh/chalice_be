import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_account_list(json_body):
    try:
        jsonschema.validate(json_body, account_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, account_list_schema)))


def validate_account_base_list(json_body):
    try:
        jsonschema.validate(json_body, account_base_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, account_base_list_schema)))


account_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "accountCd": {"type": "string"},
        "extAccountId": {"type": "integer"},
        "accountName": {"type": "string"},
        "emailAddress": {
            "type": "string",
            "pattern": r"^[\w\.-]+@[\w\.-]+\.\w+$"
        }
    },
    "required": [
        "accountCd",
        "accountName",
        "emailAddress"
    ]
}

account_base_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "accountCd": {"type": "string"},
        "extAccountId": {"type": "integer"},
        "accountName": {"type": "string"},
        "emailAddress": {
            "type": "string",
            "pattern": r"^[\w\.-]+@[\w\.-]+\.\w+$"
        },
        "baseCd": {"type": "string"},
        "baseName": {"type": "string"},
        "zipCode": {"type": "string"},
        "prefCode": {"type": "integer"},
        "address": {"type": "string"},
        "addressee": {"type": "string"},
        "telephoneNumber": {"type": ["string", "null"]},
        "faxNumber": {"type": ["string", "null"]},
        "eMailAddress": {
            "type": ["string", "null"],
            "pattern": r"^[\w\.-]+@[\w\.-]+\.\w+$"
        },
        "note": {"type": ["string", "null"]}
    },
    "required": [
        "accountCd",
        "accountName",
        "emailAddress",
        "baseCd",
        "prefCode"
    ]
}
