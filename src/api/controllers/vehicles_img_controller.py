from chalice.app import Blueprint

from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import vehicles_img_service
from api.utils.status_response import success_response, error_response
# from api.validators import vehicles_img_schema

vehicles_img_bp = Blueprint(__name__)


@vehicles_img_bp.route('/func/get-vehicles-img-list', methods=['GET'])
@errors_handle
@transaction()
def vehicles_img_list_controller():
    request = vehicles_img_bp.current_request.query_params
    success, result = vehicles_img_service.get_vehicles_img_list(request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)

# Add an order history


@vehicles_img_bp.route('/func/add-vehicles-img', methods=['POST'])
@errors_handle
@transaction()
def add_vehicles_img():
    request = vehicles_img_bp.current_request.json_body
    # vehicles_img_schema.validate_post_vehicles_img_list(request)
    success, result = vehicles_img_service.create_vehicles_img(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


# Update an order history


@vehicles_img_bp.route('/func/update-vehicles_img', methods=['PUT'])
@errors_handle
@transaction()
def update_vehicles_img_controller():
    request = vehicles_img_bp.current_request.json_body
    # vehicles_img_schema.validate_put_vehicles_img_list(request)
    success, result = vehicles_img_service.update_vehicles_img(
        request)

    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)

# Delete an order history


@vehicles_img_bp.route('/func/delete-vehicles_img', methods=['DELETE'])
@errors_handle
@transaction()
def delete_vehicles_img_endpoint():
    request = vehicles_img_bp.current_request.query_params
    success, result = vehicles_img_service.delete_vehicles_img(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)
