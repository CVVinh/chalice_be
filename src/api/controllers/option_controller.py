from chalice.app import Blueprint
from sqlalchemy.sql import func
from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import option_service
from api.validators import option_schema
from api.utils.status_response import success_response, error_response
from chalice import Response

option_bp = Blueprint(__name__)

@option_bp.route('/func/add-option', methods=['POST'])
@errors_handle
@transaction()
def add_option_controller():
    request = option_bp.current_request.json_body
    option_schema.validate_post_option_list(request)
    success, result = option_service.add_option(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@option_bp.route('/func/add-multi-option', methods=['POST'])
@errors_handle
@transaction()
def add_multi_option_controller():
    requests = option_bp.current_request.json_body
    for item in requests:
        option_schema.validate_post_option_list(item)
    success, result = option_service.add_multi_option(requests)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@option_bp.route('/func/update-option-info', methods=['PUT'])
@errors_handle
@transaction()
def update_option_controller():
    request = option_bp.current_request.json_body
    option_schema.validate_put_option_list(request)
    success, result = option_service.update_option_info(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@option_bp.route('/func/delete-option', methods=['DELETE'])
@errors_handle
@transaction()
def delete_option_controller():
    request = option_bp.current_request.query_params
    success, result = option_service.delete_option(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@option_bp.route('/func/delete-multi-option', methods=['POST'])
@errors_handle
@transaction()
def delete_multi_option_controller():
    request = option_bp.current_request.json_body
    _, result = option_service.delete_multi_option(request)
    return success_response({"message": result, "status": 200})


@option_bp.route('/func/get-option-info', methods=['GET'])
@errors_handle
@transaction()
def get_option_info_controller():
    request = option_bp.current_request.query_params
    success, result = option_service.get_option_info(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@option_bp.route('/func/get-option-list', methods=['GET'])
@errors_handle
@transaction()
def get_option_list_controller():
    request = option_bp.current_request.query_params
    success, result = option_service.get_option_list(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@option_bp.route('/func/export-option-list', methods=['GET'])
@errors_handle
@transaction()
def export_option_list_controller():
    request = option_bp.current_request.query_params
    success, result = option_service.export_option_list(request)
    file_name = f"option_list{str(func.now())}"
    if success:
        return Response(
            result, 
            headers={
                "Content-disposition": f"attachment; filename={file_name}".csv
            },
        )
    return error_response({"message": str(result), "status": 400}, 400)
