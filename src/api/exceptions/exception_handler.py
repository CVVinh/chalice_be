import traceback
from datetime import datetime


from chalice import Response
from marshmallow import ValidationError

from api.exceptions.custom_exception import ApplicationException, UnauthorizedException
from api.utils import LOGGER


def errors_handle(fn):
    def decorator():
        try:
            return fn()
        except ApplicationException as e:
            body = {
                'timestamp': int(datetime.now().timestamp()),
                'message': e.message,
                'status': 400
            }
            return Response(status_code=400, body=body)
        except UnauthorizedException:
            body = {'timestamp': int(
                datetime.now().timestamp()), 'message': 'unauthorized', 'status': 401}
            return Response(status_code=401, body=body)
        except ValidationError as e:
            msg = []
            get_msg_nest_lst(e.messages, msg)

            body = {'timestamp': int(
                datetime.now().timestamp()), 'message': msg[0], 'status': 400}
            return Response(status_code=400, body=body)
        except Exception as e:
            traceback.print_exc()
            LOGGER.error(str(e))
            body = {'timestamp': int(
                datetime.now().timestamp()), "message": 'Got error {!r}, errno is {}'.format(e, e.args[0]), 'status': 500}
            return Response(status_code=500, body=body)

    def get_msg_nest_lst(dict_msg, msg):
        for key, values in dict_msg.items():
            type_msg_obj = type(values)
            if type_msg_obj is list:
                return msg.append(values[0])
            elif type_msg_obj is dict:
                dict_msg = type(list(values.values())[0])
                if dict_msg is list:
                    return msg.append(list(values.values())[0][0])
                elif dict_msg is str:
                    return msg.append(list(values.values())[0])
                else:
                    return get_msg_nest_lst(list(values.values())[0], msg)

    return decorator
