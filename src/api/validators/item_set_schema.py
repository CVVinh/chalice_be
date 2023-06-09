import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_item_set_post(json_body):
    try:
        jsonschema.validate(json_body, item_set_post_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, item_set_post_schema)))


item_set_post_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "itemSetType": {
            "type": "number"
        },
        "itemSetName": {
            "type": "string"
        },
        "itemSetJanCode": {
            "type": "string"
        },
        "itemSetMakerId": {
            "type": "number"
        },
        "itemSetMakerModel": {
            "type": "string"
        },
        "itemSetOs": {
            "type": "number"
        },
        "itemSetExpirationDateFrom": {
            "type": "string",
            "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"

        },
        "itemSetExpirationDateTo": {
            "type": "string",
            "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"
        },
        "mainItemInfo": {
            "type": "object",
            "properties": {
                "mainItemId": {
                    "type": "number"
                }
            },
            "required": [
                "mainItemId"
            ]
        },
        "itemList": {
            "type": "array",
            "items": {
                "type": "number"
            }
        }
    },
    "required": [
        "itemSetName",
        "itemSetExpirationDateFrom",
        "itemSetExpirationDateTo",
        "mainItemInfo",
        "itemList"
    ]
}
