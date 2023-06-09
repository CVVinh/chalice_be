import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_disposal_list(json_body):
    try:
        jsonschema.validate(json_body, disposal_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, disposal_list_schema)))


disposal_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "disposalId": {"type": "integer", "minLength": 1},
        "assetId": {"type": "integer", "minLength": 1},
        "outsourcingCompanyId": {"type": ["integer", "null"], "minLength": 1},
        "disposalStatus": {"type": "integer", "minLength": 1}
    },
    "required": []
}
