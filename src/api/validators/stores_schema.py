import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_post_stores_list(json_body):
    try:
        jsonschema.validate(json_body, post_stores_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, post_stores_list_schema)))


def validate_put_stores_list(json_body):
    try:
        jsonschema.validate(json_body, put_stores_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, put_stores_list_schema)))


post_stores_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "storeId": {
            "type": "number"
        },
        "storeName": {
            "type": "string"
        },
    },
    "required": ["storeName"]
}

put_stores_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "storeId": {
            "type": "number"
        },
        "storeName": {
            "type": "string"
        },
    },
    "required": ["storeId", "storeName"]
}
