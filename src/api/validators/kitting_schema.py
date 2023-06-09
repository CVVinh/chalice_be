import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_kitting_list(json_body):
    try:
        jsonschema.validate(json_body, kitting_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, kitting_schema)))


kitting_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "kittingMasterId": {"type": "integer"},
        "kittingMasterName": {"type": "string"},
        "masterPCNumber": {"type": "integer"},
        "kittingMethod": {"type": "string"},
        "note": {"type": "string"}
    },
    "required": [
    ]
}
