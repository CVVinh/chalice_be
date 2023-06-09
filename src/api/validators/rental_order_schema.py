import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validation_create_rental_order(data):
    try:
        jsonschema.validate(data, validation_create_rental_order_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, validation_create_rental_order_schema)))


validation_create_rental_order_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
            "totalAmount": {"type": "number"},
            "paymentMethodId": {"type": "integer"},
            "rentalStatus": {"type": "integer"},
            "details": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "vehicleId": {"type": "integer"},
                        "optionId": {"type": "integer"},
                        "quantity": {"type": "integer"},
                        "amount": {"type": "number"},
                        "rentalStartDate": {"type": "string", "format": "date"},
                        "rentalEndDate": {"type": "string", "format": "date"}
                    },
                    "required": ["vehicleId", "optionId", "quantity", "amount", "rentalStartDate", "rentalEndDate"]
                }
            }
    },
    "required": ["totalAmount", "paymentMethodId", "rentalStatus", "details"]
}


def validate_update_rental_order(data):
    try:
        jsonschema.validate(data, update_rental_order_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, update_rental_order_schema)))


update_rental_order_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "paymentMethodId": {"type": "integer"},
        "rentalStatus": {"type": "integer"}
    },
    "required": ["paymentMethodId", "rentalStatus"]
}


def validate_update_rental_order_detail(data):
    try:
        jsonschema.validate(data, update_rental_order_detail_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, update_rental_order_detail_schema)))


update_rental_order_detail_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "vehicleId": {"type": "integer"},
        "optionId": {"type": "integer"},
        "quantity": {"type": "integer"},
        "amount": {"type": "number"},
        "rentalStartDate": {"type": "string", "format": "date"},
        "rentalEndDate": {"type": "string", "format": "date"}
    },
    "required": ["vehicleId", "optionId", "quantity", "amount", "rentalStartDate", "rentalEndDate"]
}
