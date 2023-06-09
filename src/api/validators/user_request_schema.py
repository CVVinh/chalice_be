import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_request_post(json_body):
    try:
        jsonschema.validate(json_body, request_post_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, request_post_schema)))


request_post_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "request_id": {"type": ["integer", "null"]},
        "request_menu": {"type": ["integer", "null"]},
        "asset_id": {"type": ["integer", "null"]},
        "asset_status": {"type": "integer"},
        "request_type": {"type": "integer"},
        "request_group_id": {"type": "integer"},
        "request_account_id": {"type": "integer"},
        "substitute_asset_id": {"type": "integer"},
        "request_datetime": {"type": "integer"},
        "request_completion_date": {"type": "integer"},
        "note": {"type": "string"},
        "account_id": {"type": "integer"},
        "account_name": {"type": "string"},
        "group_id": {"type": "integer"},
        "group_name": {"type": "string"},
    },
    "required": [
        "assetType",
        "expirationDateFrom",
        "expirationDateTo",
        "orderUnit",
        "itemTitle",
    ]
}
