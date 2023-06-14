from chalice.app import Blueprint

from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import vehicles_service
from api.utils.status_response import success_response, error_response
from api.validators import vehicles_schema

vehicles_bp = Blueprint(__name__)


@vehicles_bp.route('/func/get-vehicles-list', methods=['GET'])
@errors_handle
@transaction()
def order_history_list_controller():
    request = vehicles_bp.current_request.query_params
    try:
        return vehicles_service.get_vehicles_list(request)
    except Exception as e:
        return error_response({"message": str(e)}, 400)

# Add an order history


@vehicles_bp.route('/func/add-vehicles', methods=['POST'])
@errors_handle
@transaction()
def add_order_history():
    request = vehicles_bp.current_request.json_body
    vehicles_schema.validate_post_vehicles_list(request)
    success, result = vehicles_service.create_vehicles(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


# Update an order history


@vehicles_bp.route('/func/update-vehicles', methods=['PUT'])
@errors_handle
@transaction()
def update_order_history_controller():
    request = vehicles_bp.current_request.json_body
    vehicles_schema.validate_put_vehicles_list(request)
    success, result = vehicles_service.update_vehicles(
        request)

    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)

# Delete an order history


@vehicles_bp.route('/func/delete-vehicles', methods=['DELETE'])
@errors_handle
@transaction()
def delete_order_history_endpoint():
    request = vehicles_bp.current_request.query_params
    success, result = vehicles_service.delete_vehicles(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


@vehicles_bp.route('/func/get-vehicles-by-id', methods=['GET'])
@errors_handle
@transaction()
def get_vehicles_by_id_controller():
    request = vehicles_bp.current_request.query_params
    try:
        return vehicles_service.get_vehicle_by_id(request)
    except Exception as e:
        return error_response({"message": str(e)}, 400)


@vehicles_bp.route('/func/get-vehicles-by-param', methods=['GET'])
@errors_handle
@transaction()
def get_vehicles_by_param_controller():
    request = vehicles_bp.current_request.query_params
    try:
        return vehicles_service.get_vehicle_by_params(request)
    except Exception as e:
        return error_response({"message": str(e)}, 400)