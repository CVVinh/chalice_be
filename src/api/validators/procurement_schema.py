import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_procument_put(json_body):
    try:
        jsonschema.validate(json_body, procument_put_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, procument_put_schema)))


def validate_procument_add(json_body):
    try:
        jsonschema.validate(json_body, procument_add_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, procument_add_schema)))


procument_add_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "procurementDetailList": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "object",
                        "properties": {
                            "itemId": {
                                "type": ["number", "null"]
                            }
                        },
                        "required": [
                            # "itemId"
                        ]
                    },
                    "quantity": {
                        "type": ["number", "null"]
                    }
                },
                "required": [
                    # "item",
                    # "quantity"
                ]
            }
        },
        "procurementManagement": {
            "type": "object",
            "properties": {
                "procurementName": {
                    "type": ["string", "null"]
                },
                "quotationRequestNote": {
                    "type": ["string", "null"]
                },
                "quotationDatetime": {
                    "type": ["string", "null"]
                },
                "quotationAccountId": {
                    "type": ["number", "null"]
                }
            },
            "required": [
                "procurementName",
                "quotationRequestNote",
                "quotationDatetime",
                "quotationAccountId"
            ]
        }
    },
    "required": [
        "procurementDetailList",
        "procurementManagement"
    ]
}


procument_put_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "procurementDetailList": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "object",
                        "properties": {
                            "itemId": {
                                "type": ["number", "null"]
                            },
                            "assetType": {
                                "type": ["number", "null"]
                            },
                            "makerModel": {
                                "type": ["string", "null"]
                            },
                            "itemName": {
                                "type": ["string", "null"]
                            }
                        },
                        "required": []
                    },
                    "quantity": {
                        "type": ["number", "null"]
                    },
                    "amount": {
                        "type": ["number", "null"]
                    },
                    "estimatedArrivalDate": {
                        "type": ["string", "null"],
                        "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"
                    },
                    "estimatedShippingDate": {
                        "type": ["string", "null"],
                        "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"
                    },
                    "price": {
                        "type": ["number", "null"]
                    }
                },
                "required": []
            }
        },
        "procurementManagement": {
            "type": "object",
            "properties": {
                "procurementId": {
                    "type": ["number", "null"]
                },
                "procurementName": {
                    "type": ["string", "null"]
                },
                "quotationRequestNote": {
                    "type": ["string", "null"]
                },
                "quotationDatetime": {
                    "type": ["string", "null"],
                    "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"
                },
                "quotationAccountId": {
                    "type": ["number", "null"]
                },
                "quotationNote": {
                    "type": ["string", "null"]
                },
                "approvalRequestNote": {
                    "type": ["string", "null"]
                },
                "approvalExpirationDate": {
                    "type": ["string", "null"],
                    "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))"
                },
                "approvalAccountId": {
                    "type": ["number", "null"]
                },
                "approvalNote": {
                    "type": ["string", "null"]
                },
                "isBack": {
                    "type": ["number", "boolean"]
                },
                "procurementStatus": {
                    "type": "number"
                }
            },
            "required": []
        }
    },
    "required": []
}
