from chalice.app import Blueprint

from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import stores_service
from api.utils.status_response import success_response, error_response
from sqlalchemy.sql import func
from chalice import Response
from api.validators import stores_schema

stores_bp = Blueprint(__name__)


@stores_bp.route('/func/get-stores-list', methods=['GET'])
@errors_handle
@transaction()
def stores_list_controller():
    request = stores_bp.current_request.query_params
    success, result = stores_service.get_stores_list(request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)

# Add an order history


@stores_bp.route('/func/add-stores', methods=['POST'])
@errors_handle
@transaction()
def add_stores():
    request = stores_bp.current_request.json_body
    stores_schema.validate_post_stores_list(request)
    success, result = stores_service.create_stores(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


# Update an order history


@stores_bp.route('/func/update-stores', methods=['PUT'])
@errors_handle
@transaction()
def update_stores_controller():
    request = stores_bp.current_request.json_body
    stores_schema.validate_put_stores_list(request)
    success, result = stores_service.update_stores(
        request)

    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)

# Delete an order history


@stores_bp.route('/func/delete-stores', methods=['DELETE'])
@errors_handle
@transaction()
def delete_stores_endpoint():
    request = stores_bp.current_request.query_params
    success, result = stores_service.delete_stores(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)
