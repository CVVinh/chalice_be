import base64
import json
import os

from api.exceptions.custom_exception import UnauthorizedException
from api.utils import LOGGER


def get_logged_user(request):
    '''Cognito発行のJWTよりアカウントIDを取得して返します。JWTはAPI Gatewayのオーソライザーで検証済。'''

    # ローカルでは開発用に固定値を返す場合
    if os.environ.get('is_local', 'false') == 'true':
        return '111d1111-1eb1-111c-bc11-111c11a11ac1'   # account-1
        # return '111d1111-1eb1-111c-bc11-111c11a11ac2'   # account-2
        # return '111d1111-1eb1-111c-bc11-111c11a11ac3'   # account-3
        # return '111d1111-1eb1-111c-bc11-111c11a11ac4'   # account-4
        # return '111d1111-1eb1-111c-bc11-111c11a11ac5'   # account-5
        # return '111d1111-1eb1-111c-bc11-111c11a11ac6'   # account-6

    try:
        token = request.headers[os.environ.get('custom_auth_key', 'x-db_for_base-token').lower()]
        sections = token.split('.')
        payload = base64.b64decode(sections[1] + '=' * (-len(sections[1]) % 4))
        payload = json.loads(payload)
        sub = payload["sub"]
        LOGGER.info('account_id:' + sub)
        return sub
    except Exception as err:
        LOGGER.info(str(err))
        raise UnauthorizedException()
