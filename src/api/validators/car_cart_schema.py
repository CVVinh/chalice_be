import jsonschema
from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validation_create_car_cart(json_body):
    try:
        jsonschema.validate(json_body, validation_create_car_cart_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(
            message=Message.E000002.format(
                check_param_error(e, validation_create_car_cart_schema)
            )
        )


validation_create_car_cart_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "vehicleId": {"type": ["integer"]},
        "accountId": {"type": "integer"},
        "statusCart": {"type": "integer"},
        "optionId": {"type": ["string", "null"]},
        "insuranceId": {"type": ["string", "null"]},
        "rentalStartDate": {"type": "string", "format": "date"},
        "rentalEndDate": {"type": "string", "format": "date"},
        "totalHour": {"type": "number"},
        "totalHourCar": {"type": "number"},
        "totalOption": {"type": ["number", "null"]},
        "totalInsurance": {"type": ["number", "null"]},
        "totalCost": {"type": "number"},
        "createdBy": {"type": "integer"},
        "modifiedBy": {"type": ["integer"]},
        "deletedBy": {"type": "integer"},
    },
    "required": [
        "accountId",
        "vehicleId",
        "statusCart",
        "rentalStartDate",
        "rentalEndDate",
        "totalHour",
        "totalHourCar",
        "totalCost",
    ],
}


def validation_update_car_cart(json_body):
    try:
        jsonschema.validate(json_body, validation_update_car_cart_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(
            message=Message.E000002.format(
                check_param_error(e, validation_update_car_cart_schema)
            )
        )


validation_update_car_cart_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "carCartId": {"type": "integer"},
        "statusCart": {"type": "integer"},
        "optionId": {"type": ["string", "null"]},
        "insuranceId": {"type": ["string", "null"]},
        "rentalStartDate": {"type": "string", "format": "date"},
        "rentalEndDate": {"type": "string", "format": "date"},
        "totalHour": {"type": "number"},
        "totalHourCar": {"type": "number"},
        "totalOption": {"type": ["number", "null"]},
        "totalInsurance": {"type": ["number", "null"]},
        "totalCost": {"type": "number"},
        "createdBy": {"type": ["integer"]},
        "modifiedBy": {"type": ["integer"]},
        "deletedBy": {"type": ["integer"]},
    },
    "required": [
        "carCartId",
        "rentalStartDate",
        "rentalEndDate",
        "totalHour",
        "totalHourCar",
        "totalCost",
    ],
}
