from api.utils import LOGGER
from botocore.exceptions import ClientError
import traceback
import base64
import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_rds_key():

    # localは環境変数から返す
    if ('local' == 'local'):
        return {
            'db_host': 'localhost',
            'db_name': 'db_for_base',
            'username': 'user',
            'password': 'JyCydsk8'
        }

    region_name = os.environ.get('secret_region')
    boto3_session = boto3.session.Session()
    client = boto3_session.client(
        service_name="secretsmanager",
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=os.environ["secret_id"])
    except ClientError as e:
        LOGGER.info(traceback.format_exc())
        LOGGER.info(str(e))
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = json.loads(get_secret_value_response['SecretString'])
        else:
            secret = base64.b64decode(
                get_secret_value_response['SecretBinary'])
    return secret
