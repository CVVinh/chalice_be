import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validation_create_rental_order_cart(json_body):
    """Validates that the creation of a reserved rent order cart is valid .

    Args:
        json_body ([type]): [description]

    Raises:
        ApplicationException: [description]
    """
    try:
        jsonschema.validate(
            json_body, validation_create_rental_order_cart_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(
            message=Message.E000002.format(
                check_param_error(
                    e, validation_create_rental_order_cart_schema)
            )
        )


validation_create_rental_order_cart_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "vehicleId": {"type": ["integer"]},
        "accountId": {"type": ["integer"]},
        "statusCart": {"type": ["integer"]},
        "optionId": {"type": ["integer"]},
        "insuranceId": {"type": ["integer"]},
        "rentalStartDate": {"type": "string", "format": "date"},
        "rentalEndDate": {"type": "string", "format": "date"},
        "createdBy": {"type": ["integer"]},
        "modifiedBy": {"type": ["integer"]},
        "deletedBy": {"type": ["integer"]},
    },
    "required": [
        "accountId",
        "vehicleId",
        "statusCart",
        "rentalStartDate",
        "rentalEndDate",
    ],
}


def validation_update_rental_order_cart(json_body):
    try:
        jsonschema.validate(
            json_body, validation_update_rental_order_cart_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(
            message=Message.E000002.format(
                check_param_error(
                    e, validation_update_rental_order_cart_schema)
            )
        )


validation_update_rental_order_cart_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "rentalOrdersCartId": {"type": "integer"},
        "accountId": {"type": "integer"},
        "vehicleId": {"type": "integer"},
        "statusCart": {"type": "integer"},
        "optionId": {"type": "integer"},
        "insuranceId": {"type": "integer"},
        "rentalStartDate": {"type": "string", "format": "date"},
        "rentalEndDate": {"type": "string", "format": "date"},
        "createdBy": {"type": ["integer"]},
        "modifiedBy": {"type": ["integer"]},
        "deletedBy": {"type": ["integer"]},
    },
    "required": ["rentalOrdersCartId"],
}
