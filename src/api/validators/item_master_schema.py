import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_item_list(json_body):
    try:
        jsonschema.validate(json_body, item_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, item_list_schema)))


def validate_item_post(json_body):
    try:
        jsonschema.validate(json_body, item_post_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, item_post_schema)))


item_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "itemId": {"type": ["integer", "null"], "minLength": 1},
        "itemVersion": {"type": "integer", "minLength": 1},
        "assetType": {"type": "integer", "minLength": 1},
        "janCode": {"type": "string"},
        "makerId": {"type": "integer", "minLength": 1},
        "makerModel": {"type": "string"},
        "expirationDateFrom": {"type": "string", "format": "date", "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"},
        "expirationDateTo": {"type": "string", "format": "date", "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"},
    },
    "required": [
    ]
}
item_post_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {"type": ["integer", "null"]},
        "itemName": {"type": "string"},
        "assetType": {"type": "integer"},
        "janCode": {"type": ["string", "null"]},
        "makerId": {"type": "integer"},
        "makerModel": {"type": ["string", "null"]},
        "assetType": {"type": "integer"},
        "expirationDateFrom": {"type": "string",
                               "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"},
        "expirationDateTo": {"type": "string",
                             "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"},
        "osId": {"type": ["integer", "null"]},
        "orderUnit": {"type": "integer"},
        "orderUnitMax": {"type": ["integer", "null"]},
        "itemTitle": {"type": "string"},
        "itemDescription": {"type": ["string", "null"]},
        # "itemImage": {"type": "string"},
        "price": {"type": ["integer", "null"]},
        "tax": {"type": ["integer", "null"]},
        "createdAt": {"type": ["string", "null"], "format": "date-time"},
        "modifiedAt": {"type": ["string", "null"], "format": "date-time"}
    },
    "required": [
        "assetType",
        "expirationDateFrom",
        "expirationDateTo",
        "orderUnit",
        "itemTitle",
    ]
}
