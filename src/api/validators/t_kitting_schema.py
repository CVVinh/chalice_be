import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_post_t_kitting_list(json_body):
    try:
        jsonschema.validate(json_body, post_t_kitting_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, post_t_kitting_list_schema)))


def validate_put_t_kitting_list(json_body):
    try:
        jsonschema.validate(json_body, put_t_kitting_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, put_t_kitting_list_schema)))


post_t_kitting_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "assetId": {"type": "integer", "minLength": 1},
        "accountId": {"type": "integer", "minLength": 1},
        "kittingStatus": {"type": "integer"},
        "kittingUserId": {"type": ["integer", "null"], "minLength": 1}
    },
    "required": ["assetId", "accountId"]
}

put_t_kitting_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "assetId": {"type": "integer", "minLength": 1},
        "kittingStatus": {"type": "integer"},
        "kittingUserId": {"type": ["integer", "null"], "minLength": 1},
        "hardwareConfirmAccountId": {"type": ["integer", "null"]},
        "softwareConfirmAccountId": {"type": ["integer", "null"]},
        "kittingConfirmAccountId": {"type": ["integer", "null"]},
        "functionalConfirmAccountId": {"type": ["integer", "null"]},
        "kittingComment": {"type": ["string", "null"]},
    },
    "required": []
}
