import jsonschema
from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_post_option_list(json_body):
    try:
        jsonschema.validate(json_body, post_option_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, post_option_list_schema)))


def validate_put_option_list(json_body):
    try:
        jsonschema.validate(json_body, put_option_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, put_option_list_schema)))


post_option_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "optionName": {"type": "string"},
    },
    "required": ["optionName"]
}


put_option_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "optionId": {"type": "integer"},
        "optionName": {"type": "string"},
    },
    "required": ["optionId", "optionName"]
}