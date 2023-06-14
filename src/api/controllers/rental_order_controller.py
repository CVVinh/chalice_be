from chalice.app import Blueprint
from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import rental_order_service
from api.utils.status_response import success_response, error_response
from chalice import BadRequestError
from api.validators import rental_order_schema

rental_order_bp = Blueprint(__name__)


@rental_order_bp.route('/rentalOrder', methods=['POST'])
@errors_handle
@transaction()
def create_rental_order():
    request = rental_order_bp.current_request
    body = request.json_body
    rental_order_schema.validation_create_rental_order(body)
    success, result = rental_order_service.create_rental_order(body)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


@rental_order_bp.route('/rentalOrder', methods=['GET'])
@errors_handle
def get_all_rental_order():
    request = rental_order_bp.current_request.query_params
    success, result = rental_order_service.get_all_rental_order(request)
    if success:
        return success_response(result)
    return error_response({'message': str(result), 'status': 400}, 400)


@rental_order_bp.route('/rentalOrder/delete', methods=['PUT'])
@errors_handle
@transaction()
def delete_rental_order():
    request = rental_order_bp.current_request
    rental_order_id = request.query_params.get("rentalOrderId")
    if not rental_order_id:
        raise BadRequestError("rental_order_id is required")

    success, result = rental_order_service.delete_rental_order(rental_order_id)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


@rental_order_bp.route('/rentalOrder/restore', methods=['PUT'])
@errors_handle
@transaction()
def restore_rental_order():
    request = rental_order_bp.current_request
    rental_order_id = request.query_params.get("rentalOrderId")
    if not rental_order_id:
        raise BadRequestError('rental_order_id is required')

    success, result = rental_order_service.restore_rental_order(
        rental_order_id)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


@rental_order_bp.route('/rentalOrder/update', methods=['PUT'])
@errors_handle
@transaction()
def update_rental_order():
    request = rental_order_bp.current_request
    data = request.json_body
    rental_order_schema.validate_update_rental_order(data)
    rental_order_id = request.query_params.get("rentalOrderId")
    success, result = rental_order_service.update_rental_order(
        rental_order_id, data)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': result, 'status': 400}, 400)


@rental_order_bp.route('/rentalOrder/rentailOrderDetail/update',
                       methods=['PUT'])
@errors_handle
@transaction()
def update_rental_order_details():
    request = rental_order_bp.current_request
    data = request.json_body
    rental_order_schema.validate_update_rental_order_detail(data)
    rental_order_id = request.query_params.get("rentalOrderId")
    rental_order_detail_id = request.query_params.get('rentalOrderDetailsId')
    success, result = rental_order_service.update_rental_order_detail(
        rental_order_id, rental_order_detail_id, data)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': result, 'status': 400}, 400)
