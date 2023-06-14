from chalice.app import Blueprint
from sqlalchemy.sql import func
from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import payment_method_service
from api.validators import payment_method_schema
from api.utils.status_response import success_response, error_response
from chalice import Response

payment_method_bp = Blueprint(__name__)


@payment_method_bp.route('/func/add-payment-method', methods=['POST'])
@errors_handle
@transaction()
def add_payment_method_controller():
    request = payment_method_bp.current_request.json_body
    payment_method_schema.validate_post_payment_method_list(request)
    success, result = payment_method_service.add_payment_method(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@payment_method_bp.route('/func/add-multi-payment-method', methods=['POST'])
@errors_handle
@transaction()
def add_multi_payment_method_controller():
    requests = payment_method_bp.current_request.json_body
    for item in requests:
        payment_method_schema.validate_post_payment_method_list(item)
    success, result = payment_method_service.add_multi_payment_method(requests)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@payment_method_bp.route('/func/update-payment-method-info', methods=['PUT'])
@errors_handle
@transaction()
def update_payment_method_controller():
    request = payment_method_bp.current_request.json_body
    payment_method_schema.validate_put_payment_method_list(request)
    success, result = payment_method_service.update_payment_method_info(
        request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@payment_method_bp.route('/func/delete-payment-method', methods=['DELETE'])
@errors_handle
@transaction()
def delete_payment_method_controller():
    request = payment_method_bp.current_request.query_params
    success, result = payment_method_service.delete_payment_method(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@payment_method_bp.route('/func/delete-multi-payment-method', methods=['POST'])
@errors_handle
@transaction()
def delete_multi_payment_method_controller():
    request = payment_method_bp.current_request.json_body
    _, result = payment_method_service.delete_multi_payment_method(request)
    return success_response({"message": result, "status": 200})


@payment_method_bp.route('/func/get-payment-method-info', methods=['GET'])
@errors_handle
@transaction()
def get_payment_method_info_controller():
    request = payment_method_bp.current_request.query_params
    success, result = payment_method_service.get_payment_method_info(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@payment_method_bp.route('/func/get-payment-method-list', methods=['GET'])
@errors_handle
@transaction()
def get_option_list_controller():
    request = payment_method_bp.current_request.query_params
    success, result = payment_method_service.get_payment_method_list(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@payment_method_bp.route('/func/export-payment-method-list', methods=['GET'])
@errors_handle
@transaction()
def export_payment_method_list_controller():
    request = payment_method_bp.current_request.query_params
    success, result = payment_method_service.export_payment_method_list(
        request)
    file_name = f"payment_method_list{str(func.now())}"
    if success:
        return Response(
            result,
            headers={
                "Content-disposition": f"attachment; filename={file_name}".csv
            },
        )
    return error_response({"message": str(result), "status": 400}, 400)
