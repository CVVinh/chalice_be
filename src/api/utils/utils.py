import datetime
import pytz
import uuid
import re
from api.models import session
from api.utils.status_response import success_response, error_response
from sqlalchemy import or_
from collections.abc import MutableMapping
from api.messages import MessageResponse
from api.gen_codes import GenCodeConstant
gen_code_constant = GenCodeConstant()
message_check_operation_constant = MessageResponse()
message_check_operation_constant.setName("Asset")


def generate_id() -> str:
    return uuid.uuid4()


def get_current_jst_time():
    return datetime.now(tz=pytz.timezone("Asia/Tokyo"))


def convert_time_to_iso(date_time: datetime) -> str:
    return date_time.strftime("%Y-%m-%dT%H:%M:%S.%f%z")


# Convert nested dictionary into flattened dictionary


def convert_flatten(d, parent_key="", sep="_"):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k

        if isinstance(v, MutableMapping):
            items.extend(convert_flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def snake_to_camel(word):
    components = word.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def camel_to_snake(word):
    comp = re.compile("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")
    return comp.sub(r"_\1", word).lower()


def object_as_dict(self, is_detail=False):
    """
    Convert records in database into dictionary object
    Args:
        self: queries
        is_detail: an bool
    Returns:
        object: dict object from queries
    """
    try:
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
            format_day_and_bool_dict(dict_, key, is_detail)
        return dict_
    except Exception as e:
        return {}


def format_day_and_bool_dict(dict_, key, is_detail=False):
    """
    Convert value type datetime.date, datetime.datetime to string. type bool to integer
    Args:
        dict_: a dict
        key: a string
        is_detail: an bool
    """
    format_day = '%Y-%m-%d %H:%M:%S' if is_detail else '%Y-%m-%d'
    if isinstance(dict_[key], (datetime.date, datetime.datetime)):
        dict_[key] = dict_[key].strftime(format_day)
    elif isinstance(dict_[key], bool):
        dict_[key] = int(dict_[key])


def camel_case_object(self):
    """Convert keys in object_as_dict function into camelCase

    Args:
        dict: dict returned from object_as_dict

    Returns:
        dict: dict with camelCase keys
    """
    return {snake_to_camel(key): val for (key, val) in object_as_dict(self).items()}


def add_update_object(data, obj):
    """
    Convert field from parameter to dictionary.

    Args:
        data (obj): json body
        obj (obj): an model object
    Returns:
        dict: Returning dictionary.
    """
    fields = object_as_dict(obj)
    attr_dict = {field: data[field] for field in fields if field in data}
    for key, val in attr_dict.items():
        setattr(obj, key, val)
    return obj


def paginate(result_list, query_params):
    """
    Paginate processing and search with pageNum, pageSize.

    Arguments:
        result_list (list): a list
        query_params: MultiDict
    Returns:
        List: Returning a list.
    """
    page_num = 1
    page_size = len(result_list)
    if query_params:
        page_num = (
            int(query_params["pageNum"]) if query_params.get(
                "pageNum") else page_num
        )
        page_size = (
            int(query_params["pageSize"]) if query_params.get(
                "pageSize") else page_size
        )

    start = (page_num - 1) * page_size
    end = start + page_size
    return result_list[slice(start, end)]


def export(export_list):
    """
    Change the list to export CSV.

    Arguments:
        export_list (list): a list
    Returns:
        File: Returning a file.
    """
    if len(export_list) <= 0:
        return (False, "Failed!")
    str_body = ""
    str_header = "".join(f"{key}," for key in export_list[0].keys())
    for item in export_list:
        for key, value in item.items():
            if value is None:
                value = ""
            str_body += f"{str(value)},"
        str_body += "\n"
    return (True, (str_header + "\n" + str_body))


def check_param_error(self, json_schema):
    """
    Check if the parameters are error.

    Arguments:
        json_schema : json body
    Returns:
        String: Returning a string.
    """
    for param_error in json_schema["properties"].keys():
        if param_error in str(self):
            return param_error
