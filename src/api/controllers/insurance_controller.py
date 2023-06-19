from chalice.app import Blueprint
from sqlalchemy.sql import func
from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import isurance_service
from api.validators import isurance_schema
from api.utils.status_response import success_response, error_response
from chalice.app import Response

insurance_bp = Blueprint(__name__)


@insurance_bp.route('/func/add-insurance', methods=['POST'])
@errors_handle
@transaction()
def add_isurances_controller():
    request = insurance_bp.current_request.json_body
    if request is not None and 'params' in request:
        request = request['params']
    isurance_schema.validate_post_isurance_list(request)
    success, result = isurance_service.add_isurances(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@insurance_bp.route('/func/add-multi-insurance', methods=['POST'])
@errors_handle
@transaction()
def add_multi_isurances_controller():
    requests = insurance_bp.current_request.json_body
    if requests is not None and 'params' in requests:
        requests = requests['params']
    for item in requests:
        isurance_schema.validate_post_isurance_list(item)
    success, result = isurance_service.add_multi_isurances(requests)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@insurance_bp.route('/func/update-insurance-info', methods=['PUT'])
@errors_handle
@transaction()
def update_isurances_controller():
    request = insurance_bp.current_request.json_body
    if request is not None and 'params' in request:
        request = request['params']
    isurance_schema.validate_put_isurance_list(request)
    success, result = isurance_service.update_isurances_info(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@insurance_bp.route('/func/delete-insurance', methods=['DELETE'])
@errors_handle
@transaction()
def delete_isurances_controller():
    request = insurance_bp.current_request.query_params
    if request is not None and 'params' in request:
        request = request['params']
    success, result = isurance_service.delete_isurances(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@insurance_bp.route('/func/delete-multi-insurance', methods=['POST'])
@errors_handle
@transaction()
def delete_multi_isurances_controller():
    request = insurance_bp.current_request.json_body
    if request is not None and 'params' in request:
        request = request['params']
    _, result = isurance_service.delete_multi_isurances(request)
    return success_response({"message": result, "status": 200})


@insurance_bp.route('/func/get-insurance-info', methods=['GET'])
@errors_handle
@transaction()
def get_isurances_info_controller():
    request = insurance_bp.current_request.query_params
    if request is not None and 'params' in request:
        request = request['params']
    success, result = isurance_service.get_isurances_info(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@insurance_bp.route('/func/get-insurance-list', methods=['POST'])
@errors_handle
@transaction()
def get_isurances_list_controller():
    request = insurance_bp.current_request.json_body
    if request is not None and 'params' in request:
        request = request['params']
    success, result = isurance_service.get_isurances_list(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@insurance_bp.route('/func/export-insurance-list', methods=['POST'])
@errors_handle
@transaction()
def export_isurances_list_controller():
    request = insurance_bp.current_request.json_body
    if request is not None and 'params' in request:
        request = request['params']
    success, result = isurance_service.export_isurances_list(request)
    file_name = f"isurance_list{str(func.now())}"
    if success:
        return Response(
            result,
            headers={
                "Content-disposition": f"attachment; filename={file_name}.csv"
            },
        )
    return error_response({"message": str(result), "status": 400}, 400)
