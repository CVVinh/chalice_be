from chalice.app import Blueprint

from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import makers_service
from api.utils.status_response import success_response, error_response
from api.validators import makers_schema

makers_bp = Blueprint(__name__)


@makers_bp.route('/func/get-makers-list', methods=['GET'])
@errors_handle
@transaction()
def makers_list_controller():
    request = makers_bp.current_request.query_params
    try:
        return makers_service.get_makers_list(request)
    except Exception as e:
        return error_response({"message": str(e)}, 400)
# Add an order history


@makers_bp.route('/func/add-makers', methods=['POST'])
@errors_handle
@transaction()
def add_makers():
    request = makers_bp.current_request.json_body
    makers_schema.validate_post_makers_list(request)
    success, result = makers_service.create_makers(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


# Update an order history


@makers_bp.route('/func/update-makers', methods=['PUT'])
@errors_handle
@transaction()
def update_makers_controller():
    request = makers_bp.current_request.json_body
    makers_schema.validate_put_makers_list(request)

    success, result = makers_service.update_makers(
        request)

    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)

# Delete an order history


@makers_bp.route('/func/delete-makers', methods=['DELETE'])
@errors_handle
@transaction()
def delete_makers_endpoint():
    request = makers_bp.current_request.query_params
    success, result = makers_service.delete_makers(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)
