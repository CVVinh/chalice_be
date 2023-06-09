import jsonschema

from api.exceptions.custom_exception import ApplicationException
from api.messages import Message
from api.utils import LOGGER
from api.utils.utils import check_param_error


def validate_post_outsourcing_company_list(json_body):
    try:
        jsonschema.validate(json_body, post_outsourcing_company_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, post_outsourcing_company_list_schema)))


def validate_put_outsourcing_company_list(json_body):
    try:
        jsonschema.validate(json_body, put_outsourcing_company_list_schema)
    except Exception as e:
        LOGGER.debug(e)
        raise ApplicationException(message=Message.E000002.format(
            check_param_error(e, put_outsourcing_company_list_schema)))


post_outsourcing_company_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "outsourcingCompanyName": {"type": ["string", "null"], "maxLength": 200},
        "area": {"type": ["string", "null"], "maxLength": 200},
        "pilotNumber": {"type": ["string", "null"]},
        "zipCode": {"type": ["string", "null"], "maxLength": 10, "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"},
        "prefCode": {"type": "integer"},
        "city": {"type": ["string", "null"], "maxLength": 200},
        "street": {"type": ["string", "null"], "maxLength": 200},
        "building": {"type": ["string", "null"], "maxLength": 200},
        "department": {"type": ["string", "null"], "maxLength": 200},
        "pic": {"type": ["string", "null"], "maxLength": 200},
        "directNumber": {"type": ["string", "null"], "pattern": "^(\\([0-9]{3}\\))?0[0-9]{10}$"},
        "directEmailAddress": {"type": ["string", "null"], "pattern": "^\\S+@\\S+\\.\\S+$", "format": "email", "maxLength": 200}
    },
    "required": ["outsourcingCompanyName", "zipCode", "pilotNumber", "department"],
    "if": {
        "properties": {"pilotNumber": {"maxLength": 8}}
    },
    "then": {
        "properties": {"pilotNumber": {"pattern": "^(\\([0-9]{3}\\))?[0-9]{8}$"}}
    },
    "else": {
        "properties": {"pilotNumber": {"pattern": "^(\\([0-9]{3}\\))?0[0-9]{10}$"}}
    }

}

put_outsourcing_company_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "outsourcingCompanyName": {"type": ["string", "null"], "maxLength": 200},
        "area": {"type": ["string", "null"], "maxLength": 200},
        "pilotNumber": {"type": ["string", "null"]},
        "zipCode": {"type": ["string", "null"], "maxLength": 10, "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"},
        "prefCode": {"type": "integer"},
        "city": {"type": ["string", "null"], "maxLength": 200},
        "street": {"type": ["string", "null"], "maxLength": 200},
        "building": {"type": ["string", "null"], "maxLength": 200},
        "department": {"type": ["string", "null"], "maxLength": 200},
        "pic": {"type": ["string", "null"], "maxLength": 200},
        "directNumber": {"type": ["string", "null"], "pattern": "^(\\([0-9]{3}\\))?0[0-9]{10}$"},
        "directEmailAddress": {"type": ["string", "null"], "pattern": "^\\S+@\\S+\\.\\S+$", "format": "email", "maxLength": 200}
    },
    "required": [],
    "if": {
        "properties": {"pilotNumber": {"maxLength": 8}}
    },
    "then": {
        "properties": {"pilotNumber": {"pattern": "^(\\([0-9]{3}\\))?[0-9]{8}$"}}
    },
    "else": {
        "properties": {"pilotNumber": {"pattern": "^(\\([0-9]{3}\\))?0[0-9]{10}$"}}
    }

}
