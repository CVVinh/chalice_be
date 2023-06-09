import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_post_asset_set_asset_list(json_body):
    try:
        jsonschema.validate(json_body, post_asset_set_asset_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, post_asset_set_asset_list_schema)))


post_asset_set_asset_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "assetIdSet ": {"type": ["integer", "null"], "minLength": 1},
        "assetId": {"type": ["integer", "null"], "minLength": 1},
        "isMain": {"type": ["integer", "boolean"], "minLength": 1}
    },
    "required": ["assetIdSet", "assetId"]
}
