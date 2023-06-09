import jsonschema
from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_post_payment_method_list(json_body):
    try:
        jsonschema.validate(json_body, post_payment_method_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, post_payment_method_list_schema)))


def validate_put_payment_method_list(json_body):
    try:
        jsonschema.validate(json_body, put_payment_method_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, put_payment_method_list_schema)))


post_payment_method_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "paymentMethodName": {"type": "string"},
    },
    "required": ["paymentMethodName"]
}


put_payment_method_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "paymentMethodId": {"type": "integer"},
        "paymentMethodName": {"type": "string"},
    },
    "required": ["paymentMethodId", "paymentMethodName"]
}
