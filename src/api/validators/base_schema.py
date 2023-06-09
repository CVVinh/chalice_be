import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_base_list(json_body):
    try:
        jsonschema.validate(json_body, base_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, base_list_schema)))


base_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "baseCd": {"type": "string"},
        "baseName": {"type": "string"},
        "prefCode": {"type": "integer"},
        "note": {"type": "string"},
        "eMailAddress": {"type": "string"},
        "address": {"type": "string"},
        "telephoneNumber": {"type": "string"},
        "faxNumber": {"type": "string"}
    },
    "required": []
}
