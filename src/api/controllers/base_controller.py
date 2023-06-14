from chalice.app import Blueprint

from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import base_service
from api.validators import base_schema
from api.utils.status_response import success_response, error_response
from sqlalchemy.sql import func
from chalice import Response

base_bp = Blueprint(__name__)


@base_bp.route('/func/add-base', methods=['POST'])
@errors_handle
@transaction()
def add_base_controller():
    request = base_bp.current_request.json_body
    base_schema.validate_base_list(request)
    success, result = base_service.add_base(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({'message': str(result), "status": 400}, 400)


@base_bp.route('/func/update-base-info', methods=['PUT'])
@errors_handle
@transaction()
def update_base_info_controller():
    request = base_bp.current_request.json_body
    base_schema.validate_base_list(request)
    success, result = base_service.update_base_info(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({'message': str(result), "status": 400}, 400)


@base_bp.route('/func/delete-base', methods=['DELETE'])
@errors_handle
@transaction()
def delete_base_controller():
    request = base_bp.current_request.json_body
    success, result = base_service.delete_base(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({'message': str(result), "status": 400}, 400)


@base_bp.route('/func/get-base-info', methods=['GET'])
@errors_handle
@transaction()
def get_base_info_controller():
    request = base_bp.current_request.query_params
    success, result = base_service.get_base_info(request)
    if success:
        return success_response(result)
    return error_response({'message': str(result), "status": 400}, 400)


@base_bp.route('/func/get-base-list', methods=['GET'])
@errors_handle
@transaction()
def get_base_list_controller():
    request = base_bp.current_request.query_params
    success, result = base_service.get_base_list(request)
    if success:
        return success_response(result)
    return error_response({'message': str(result), "status": 400}, 400)


@base_bp.route('/func/export-base-list', methods=['GET'])
@errors_handle
@transaction()
def export_base_list_controller():
    request = base_bp.current_request.query_params
    success, result = base_service.export_base_list(request)
    file_name = f"base_list_{str(func.now())}"
    if success:
        return Response(
            result,
            headers={
                "Content-disposition": f"attachment; filename={file_name}.csv"
            },
        )
    return error_response({'message': str(result)}, 400)


@base_bp.route('/func/get-base-user-info', methods=['GET'])
@errors_handle
@transaction()
def account_list_controller():
    request = base_bp.current_request.query_params
    success, result = base_service.get_base_user_info(request)
    if success:
        return success_response(result)
    return error_response({'message': str(result), 'status': 400}, 400)
