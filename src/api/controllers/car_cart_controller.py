from chalice.app import Blueprint
from sqlalchemy.sql import func
from api.exceptions.exception_handler import errors_handle
from api.models.transaction import transaction
from api.services import car_cart_service
from api.validators import car_cart_schema
from api.utils.status_response import success_response, error_response
from chalice.app import Response

car_cart_bp = Blueprint(__name__)


@car_cart_bp.route("/func/add-car-cart", methods=["POST"])
@errors_handle
@transaction()
def add_rental_order_cart_controller():
    request = car_cart_bp.current_request.json_body
    if request is not None and "params" in request:
        request = request["params"]
    car_cart_schema.validation_create_car_cart(request)
    success, result = car_cart_service.add_rental_order_cart(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@car_cart_bp.route("/func/add-multi-car-cart", methods=["POST"])
@errors_handle
@transaction()
def add_multi_rental_order_cart_controller():
    requests = car_cart_bp.current_request.json_body
    if requests is not None and "params" in requests:
        requests = requests["params"]
    for item in requests:
        car_cart_schema.validation_create_car_cart(item)
    success, result = car_cart_service.add_multi_rental_order_cart(requests)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@car_cart_bp.route("/func/update-car-cart-info", methods=["PUT"])
@errors_handle
@transaction()
def update_rental_order_cart_controller():
    request = car_cart_bp.current_request.json_body
    if request is not None and "params" in request:
        request = request["params"]
    car_cart_schema.validation_update_car_cart(request)
    success, result = car_cart_service.update_rental_order_cart_info(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@car_cart_bp.route("/func/delete-soft-car-cart", methods=["DELETE"])
@errors_handle
@transaction()
def delete_soft_rental_order_cart_controller():
    request = car_cart_bp.current_request.query_params
    if request is not None and "params" in request:
        request = request["params"]
    success, result = car_cart_service.delete_soft_rental_order_cart(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@car_cart_bp.route("/func/delete-hard-car-cart", methods=["DELETE"])
@errors_handle
@transaction()
def delete_hard_rental_order_cart_controller():
    request = car_cart_bp.current_request.query_params
    if request is not None and "params" in request:
        request = request["params"]
    success, result = car_cart_service.delete_hard_rental_order_cart(request)
    if success:
        return success_response({"message": result, "status": 200})
    return error_response({"message": str(result), "status": 400}, 400)


@car_cart_bp.route("/func/delete-soft-multi-car-cart", methods=["POST"])
@errors_handle
@transaction()
def delete_soft_multi_rental_order_cart_controller():
    request = car_cart_bp.current_request.json_body
    if request is not None and "params" in request:
        request = request["params"]
    _, result = car_cart_service.delete_soft_multi_rental_order_cart(request)
    return success_response({"message": result, "status": 200})


@car_cart_bp.route("/func/get-car-cart-info", methods=["POST"])
@errors_handle
@transaction()
def get_rental_order_cart_info_controller():
    request = car_cart_bp.current_request.json_body
    if request is not None and "params" in request:
        request = request["params"]
    success, result = car_cart_service.get_rental_order_cart_info(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@car_cart_bp.route("/func/get-car-cart-list", methods=["POST"])
@errors_handle
@transaction()
def get_rental_order_cart_list_controller():
    request = car_cart_bp.current_request.json_body
    if request is not None and "params" in request:
        request = request["params"]
    success, result = car_cart_service.get_rental_order_cart_list(request)
    if success:
        return success_response(result)
    return error_response({"message": str(result), "status": 400}, 400)


@car_cart_bp.route("/func/export-car-cart-list", methods=["GET"])
@errors_handle
@transaction()
def export_rental_order_cart_list_controller():
    request = car_cart_bp.current_request.query_params
    if request is not None and "params" in request:
        request = request["params"]
    success, result = car_cart_service.export_rental_order_cart_list(request)
    file_name = f"rental_order_cart_list{str(func.now())}"
    if success:
        return Response(
            result,
            headers={
                "Content-disposition": f"attachment; filename={file_name}.csv"
            }
        )
    return error_response({"message": str(result), "status": 400}, 400)
