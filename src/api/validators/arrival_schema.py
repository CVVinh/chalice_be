import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_post_arrival_list(json_body):
    try:
        jsonschema.validate(json_body, post_arrival_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, post_arrival_list_schema)))


def validate_put_arrival_list(json_body):
    try:
        jsonschema.validate(json_body, put_arrival_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, put_arrival_list_schema)))


post_arrival_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "baseId": {"type": ["integer", "null"], "minLength": 1},
        "orderId": {"type": ["integer", "null"], "minLength": 1},
        "arrivalOn": {"type": "string", "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"},
        "itemId": {"type": "integer", "minLength": 1},
        "itemIdSet": {"type": "integer", "minLength": 1},
        "inspectionStatus": {"type": "integer"},
        "inspectionStatusNote": {"type": ["string", "null"], "maxLength": 400},
        "inspectionAccountId": {"type": ["integer", "null"], "minLength": 1, "maxLength": 36},
        "failureAction": {"type": "integer"},
        "failureActionNote": {"type": ["string", "null"], "maxLength": 400},
        "quantity": {"type": ["integer", "null"]},
        "arrivalType": {"type": ["integer", "null"]},
        "accountId": {"type": ["integer", "null"]},
        "usingFrom": {"type": ["string", "null"], "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"},
        "usingTo": {"type": ["string", "null"], "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"}
    },
    "required": ["inspectionStatus", "failureAction"]
}


put_arrival_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "baseId": {"type": ["integer", "null"], "minLength": 1},
        "orderId": {"type": ["integer", "null"], "minLength": 1},
        "arrivalOn": {"type": "string", "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"},
        "itemId": {"type": "integer", "minLength": 1},
        "inspectionStatus": {"type": "integer"},
        "inspectionStatusNote": {"type": ["string", "null"], "maxLength": 400},
        "inspectionAccountId": {"type": ["integer", "null"], "minLength": 1, "maxLength": 36},
        "failureAction": {"type": "integer"},
        "failureActionNote": {"type": ["string", "null"], "maxLength": 400},
        "accountId": {"type": ["integer", "null"]},
        "usingFrom": {"type": ["string", "null"], "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"},
        "usingTo": {"type": ["string", "null"], "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"}
    },
    "required": []
}
