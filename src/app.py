import copy
import json
import os

from chalice import Chalice, AuthResponse
from api import controllers
from api.utils import LOGGER

LOG_MASKED_KEY = [
    'email_address',
    'password'
]


def create_app():
    app = Chalice(app_name=os.environ.get('api_name', 'base-api'))
    app.debug = os.environ.get('chalice_debug', 'false') == 'true'
    app.api.cors = True
    controllers.init_app(app)

    return app


app = create_app()


# リクエストとレスポンスのログ出力
@app.middleware('http')
def request_response_logging(event, get_response):
    LOGGER.info("request-path:" + event.context["path"])
    LOGGER.info("request-method:" + event.method)

    if event.query_params:
        LOGGER.info("request-query_params:" +
                    json.dumps(event.to_dict()['query_params']))

    if event.raw_body:  # [memo]json以外のリクエストが追加された場合は、対応(特定パスはチェックしない等)が必要
        LOGGER.info("request-body:" +
                    str(maskValue(json.loads(event.raw_body.decode('utf-8'))))[:3000])

    response = get_response(event)

    LOGGER.info("response-code:" + str(response.status_code))
    LOGGER.info("response-body:" + str(maskValue(response.body))[:3000])

    return response


# LOG_MASKED_KEY に登録されているKEYのVALUEをマスクする
def maskValue(origin):
    obj = copy.deepcopy(origin)
    if isinstance(obj, dict):
        for each in obj:
            if each in LOG_MASKED_KEY:
                # obj[each] = '*' * len(obj[each])
                obj[each] = '***'
            elif isinstance(obj[each], dict):
                obj[each] = maskValue(obj[each])
            elif isinstance(obj[each], list):
                obj[each] = maskValue(obj[each])
    elif isinstance(obj, list):
        for item in obj:
            item = maskValue(item)
    return obj
