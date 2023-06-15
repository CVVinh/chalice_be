from chalice.app import Blueprint

from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import models_service
from api.utils.status_response import success_response, error_response
from api.validators import models_schema

models_bp = Blueprint(__name__)


@models_bp.route('/func/get-models-list', methods=['GET'])
@errors_handle
@transaction()
def stores_list_controller():
    request = models_bp.current_request.query_params

    try:
        return models_service.get_models_list(request)
    except Exception as e:
        return error_response({"message": str(e)}, 400)

# Add an order history


@models_bp.route('/func/add-models', methods=['POST'])
@errors_handle
@transaction()
def add_models():
    request = models_bp.current_request.json_body
    models_schema.validate_post_models_list(request)
    success, result = models_service.create_models(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)


# Update an order history


@models_bp.route('/func/update-models', methods=['PUT'])
@errors_handle
@transaction()
def update_models_controller():
    request = models_bp.current_request.json_body
    models_schema.validate_put_models_list(request)
    success, result = models_service.update_models(
        request)

    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)

# Delete an order history


@models_bp.route('/func/delete-models', methods=['DELETE'])
@errors_handle
@transaction()
def delete_models_endpoint():
    request = models_bp.current_request.query_params
    success, result = models_service.delete_models(
        request)
    if success:
        return success_response({'message': result, 'status': 200})
    return error_response({'message': str(result), 'status': 400}, 400)
