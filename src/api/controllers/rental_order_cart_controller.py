from chalice.app import Blueprint
from sqlalchemy.sql import func
from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import rental_order_cart_service
from api.validators import rental_order_cart_schema
from api.utils.status_response import success_response, error_response
from chalice import Response

rental_order_cart_bp = Blueprint(__name__)


@rental_order_cart_bp.route('/func/add-rental-order-cart', methods=['POST'])
@errors_handle
@transaction()
def add_rental_order_cart_controller():
    request = rental_order_cart_bp.current_request.json_body
    rental_order_cart_schema.validation_create_rental_order_cart(request)
    success, result = rental_order_cart_service.add_rental_order_cart(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@rental_order_cart_bp.route('/func/add-multi-rental-order-cart', methods=['POST'])
@errors_handle
@transaction()
def add_multi_rental_order_cart_controller():
    requests = rental_order_cart_bp.current_request.json_body
    for item in requests:
        rental_order_cart_schema.validation_create_rental_order_cart(item)
    success, result = rental_order_cart_service.add_multi_rental_order_cart(
        requests)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@rental_order_cart_bp.route('/func/update-rental-order-cart-info', methods=['PUT'])
@errors_handle
@transaction()
def update_rental_order_cart_controller():
    request = rental_order_cart_bp.current_request.json_body
    rental_order_cart_schema.validation_update_rental_order_cart(request)
    success, result = rental_order_cart_service.update_rental_order_cart_info(
        request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@rental_order_cart_bp.route('/func/delete-soft-rental-order-cart', methods=['DELETE'])
@errors_handle
@transaction()
def delete_soft_rental_order_cart_controller():
    request = rental_order_cart_bp.current_request.query_params
    success, result = rental_order_cart_service.delete_soft_rental_order_cart(
        request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@rental_order_cart_bp.route('/func/delete-hard-rental-order-cart', methods=['DELETE'])
@errors_handle
@transaction()
def delete_hard_rental_order_cart_controller():
    request = rental_order_cart_bp.current_request.query_params
    success, result = rental_order_cart_service.delete_hard_rental_order_cart(
        request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@rental_order_cart_bp.route('/func/delete-soft-multi-rental-order-cart', methods=['POST'])
@errors_handle
@transaction()
def delete_soft_multi_rental_order_cart_controller():
    request = rental_order_cart_bp.current_request.json_body
    _, result = rental_order_cart_service.delete_soft_multi_rental_order_cart(
        request)
    return success_response({"message": result, "status": 200})


@rental_order_cart_bp.route('/func/get-rental-order-cart-info', methods=['POST'])
@errors_handle
@transaction()
def get_rental_order_cart_list_controller():
    request = rental_order_cart_bp.current_request.json_body
    success, result = rental_order_cart_service.get_rental_order_cart_info(
        request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@rental_order_cart_bp.route('/func/get-rental-order-cart-list', methods=['POST'])
@errors_handle
@transaction()
def get_rental_order_cart_list_controller():
    request = rental_order_cart_bp.current_request.json_body
    success, result = rental_order_cart_service.get_rental_order_cart_list(
        request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@rental_order_cart_bp.route('/func/export-rental-order-cart-list', methods=['GET'])
@errors_handle
@transaction()
def export_rental_order_cart_list_controller():
    request = rental_order_cart_bp.current_request.query_params
    success, result = rental_order_cart_service.export_rental_order_cart_list(
        request)
    file_name = f"rental_order_cart_list{str(func.now())}"
    if success:
        return Response(
            result,
            headers={
                "Content-disposition": f"attachment; filename={file_name}".csv
            },
        )
    return error_response({"message": str(result), "status": 400}, 400)
