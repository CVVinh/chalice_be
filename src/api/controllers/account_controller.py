from chalice.app import Blueprint
from chalice import AuthResponse

from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import account_service
from api.validators import account_schema
from api.utils.status_response import success_response, error_response


account_bp = Blueprint(__name__)


@account_bp.authorizer()
def demo_auth(auth_request):
    token = auth_request.token
    # This is just for demo purposes as shown in the API Gateway docs.
    # Normally you'd call an oauth provider, validate the
    # jwt token, etc.
    # In this example, the token is treated as the status for demo
    # purposes.
    if token == 'allow':
        return AuthResponse(routes=['/api/accounts'], principal_id='user')
    else:
        # By specifying an empty list of routes,
        # we're saying this user is not authorized
        # for any URLs, which will result in an
        # Unauthorized response.
        return AuthResponse(routes=[], principal_id='user')


@account_bp.route('/api/accounts', methods=['GET'], authorizer=demo_auth)
@errors_handle
@transaction()
def account_list_controller():
    request = account_bp.current_request.query_params
    success, result = account_service.get_all_account(request)
    if success:
        return success_response(result)
    return error_response({'message': str(result), 'status': 400}, 400)


@account_bp.route('/func/add-account', methods=['POST'])
@errors_handle
@transaction()
def add_account_controller():
    request = account_bp.current_request.json_body
    account_schema.validate_account_list(request)
    success, result = account_service.add_account(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({'message': str(result), 'status': 400}, 400)


@account_bp.route('/func/update-account', methods=['PUT'])
@errors_handle
@transaction()
def update_account_controller():
    request = account_bp.current_request.json_body
    account_schema.validate_account_list(request)
    success, result = account_service.update_account_info(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({'message': str(result), 'status': 400}, 400)


@account_bp.route('/func/delete-account', methods=['DELETE'])
@errors_handle
@transaction()
def delete_account_controller():
    request = account_bp.current_request.query_params
    success, result = account_service.delete_account(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({'message': str(result), 'status': 400}, 400)


@account_bp.route('/func/add-account-base', methods=['POST'])
@errors_handle
@transaction()
def add_account_base_controller():
    request = account_bp.current_request.json_body
    account_schema.validate_account_base_list(request)
    success, result = account_service.add_account_base(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({'message': str(result), 'status': 400}, 400)


@account_bp.route('/func/update-account-base', methods=['PUT'])
@errors_handle
@transaction()
def update_account_base_controller():
    request = account_bp.current_request.json_body
    account_schema.validate_account_base_list(request)
    success, result = account_service.update_account_base_info(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({'message': str(result), 'status': 400}, 400)
