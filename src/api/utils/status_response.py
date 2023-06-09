from datetime import datetime

from chalice import Response


def error_response(message, http_status_code, headers=None):
    body = {'timestamp': int(datetime.now().timestamp())}
    body = {**body, **message}
    response = Response(body=body, status_code=http_status_code,
                        headers=headers)
    return response


def success_response(data, headers=None):
    body = {'timestamp': int(datetime.now().timestamp())}
    if data is not None:
        body = {**body, **data}
    response = Response(body=body, status_code=200,
                        headers=headers)
    return response


def response(respond: Response):
    body = {'timestamp': int(datetime.now().timestamp())}
    if respond.body is not None:
        body = {**body, **respond.body}
    return Response(body=body, status_code=respond.status_code,
                    headers=None)


def success_response_code():
    body = {'timestamp': int(datetime.now().timestamp())}
    response = Response(body=body)
    return response
