import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER


def validate_depre_rule_post(json_body):
    try:
        jsonschema.validate(json_body, depre_rule_post_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002)


depre_rule_post_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "depreciationRuleId": {"type": "integer"},
        "depreciationRuleName": {"type": "string"},
        "fiscalYear": {"type": "integer"},
        "baseYear": {"type": "string", "pattern": "(19|20)([00-99])"},
        "amountPerYear": {"type": "number"}
    },
    "required": []
}
