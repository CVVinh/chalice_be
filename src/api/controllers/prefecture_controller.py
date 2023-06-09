from chalice.app import Blueprint

from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import prefecture_service
from api.validators import prefecture_schema
from api.utils.status_response import success_response, error_response

prefecture_bp = Blueprint(__name__)


@prefecture_bp.route('/func/get-prefecture-list', methods=['GET'])
@errors_handle
@transaction()
def prefecture_list_controller():
    request = prefecture_bp.current_request.query_params
    success, result = prefecture_service.get_prefecture_list(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "stasus": 400}, 400)


@prefecture_bp.route('/func/add-prefecture', methods=['POST'])
@errors_handle
@transaction()
def add_prefecture_controller():
    request = prefecture_bp.current_request.json_body
    prefecture_schema.validate_account_list(request)
    success, result = prefecture_service.add_prefecture(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "stasus": 400}, 400)


@prefecture_bp.route('/func/update-prefecture', methods=['PUT'])
@errors_handle
@transaction()
def update_prefecture_controller():
    request = prefecture_bp.current_request.json_body
    prefecture_schema.validate_account_list(request)
    success, result = prefecture_service.update_prefecture(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "stasus": 400}, 400)


@prefecture_bp.route('/func/delete-prefecture', methods=['DELETE'])
@errors_handle
@transaction()
def delete_prefecture_controller():
    request = prefecture_bp.current_request.json_body
    success, result = prefecture_service.delete_prefecture(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "stasus": 400}, 400)
