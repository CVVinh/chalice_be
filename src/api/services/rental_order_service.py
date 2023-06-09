from api.models.models import RentalOrders, RentalOrderDetail
from api.models import session
from api.utils.utils import paginate
from api.messages import MessageResponse
from datetime import datetime
from sqlalchemy import func

message_rental_order_constants = MessageResponse()
message_rental_order_constants.setName("Rental Order")

message_rental_order_details_constants = MessageResponse()
message_rental_order_details_constants.setName("Rental Order Details")


def create_rental_order(rental_order_data):
    """
    Create request and add record for rental order and rental order details.

    Argument:
        rental_order_data: request body
    Returns:
        The message.
    """
    # Extract details from rental_order_data
    details = rental_order_data.pop("details", [])

    # Create a new rental order
    new_rental_order = RentalOrders(**rental_order_data)
    session.add(new_rental_order)
    session.flush()  # Get the auto-generated rental order ID

    total_amount = 0

    # Create rental order details
    for detail in details:
        # Get the amount from the detail dictionary
        amount = detail.get('amount', 0)
        total_amount += amount

        # Remove the 'amount' attribute from the detail dictionary
        detail.pop('amount', None)

        # Create a new rental order detail
        new_rental_order_detail = RentalOrderDetail(
            rentalOrderId=new_rental_order.rentalOrdersId,
            amount=amount,
            **detail
        )
        session.add(new_rental_order_detail)

    # Update the total amount of the rental order
    new_rental_order.totalAmount = total_amount

    session.commit()

    return (True, message_rental_order_constants.MESSAGE_SUCCESS_CREATED)


def get_all_rental_order(request):
    """ 
    Get all rental order list

    Argument:
        query_params: parameter

    Returns:
        The message and a list of rental order.
    """
    rental_orders = session.query(RentalOrders).all()
    serialized_rental_orders = serialize_rental_order(rental_orders)
    paginated_lst = paginate(serialized_rental_orders, request)
    return (True, {
        "data": paginated_lst,
        "totalRecord": len(serialized_rental_orders),
        "message": message_rental_order_constants.MESSAGE_SUCCESS_GET_LIST,
        "status": 200
    })


def serialize_rental_order(rental_orders):
    """
    Serialzie object rental order to json 

    Argument:
        rental_orders: parameter

    Returns:
        json of object : serialized_rental_orders

    """
    serialized_rental_orders = []

    for rental_order in rental_orders:
        rental_order_details = session.query(RentalOrderDetail).filter_by(
            rentalOrderId=rental_order.rentalOrdersId).all()
        serialized_details = []

        for detail in rental_order_details:
            serialized_detail = {
                "rental_orders_detail_id": detail.rentalOrdersId,
                "vehicle_id": detail.vehicleId,
                "option_id": detail.optionId,
                "quantity": detail.quantity,
                "amount": detail.amount,
                "rental_start_date": str(detail.rentalStartDate),
                "rental_end_date": str(detail.rentalEndDate),
                # Add more fields as needed
            }
            serialized_details.append(serialized_detail)

        serialized_rental_order = {
            "rental_orders_id": rental_order.rentalOrdersId,
            "total_amount": rental_order.totalAmount,
            "payment_method_id": rental_order.paymentMethodId,
            "rental_status": rental_order.rentalStatus,
            "created_at": str(rental_order.createdAt),
            "created_by": rental_order.createdBy,
            "modified_at": str(rental_order.modifiedAt),
            "modified_by": rental_order.modifiedBy,
            "deleted_at": str(rental_order.deletedAt),
            "deleted_by": rental_order.deletedBy,
            "is_deleted": rental_order.isDeleted,
            "details": serialized_details
        }
        serialized_rental_orders.append(serialized_rental_order)

    return serialized_rental_orders


def delete_rental_order(rental_order_id):
    """
    Set state of rental order and rental order details to delete , set date deleted

    Argument:
        rental_order_id: parameter
    Returns:
        The message.
    """
    rental_order = session.query(RentalOrders).filter_by(
        rentalOrdersId=rental_order_id).first()

    if rental_order is None:
        return (False, message_rental_order_constants.MESSAGE_ERROR_NOT_EXIST)

    # Update rental order
    rental_order.isDeleted = True
    rental_order.deletedAt = datetime.now()

    # Update rental order details
    rental_order_details = session.query(RentalOrderDetail).filter_by(
        rentalOrderId=rental_order.rentalOrdersId).all()
    for detail in rental_order_details:
        detail.isDeleted = True
        detail.deletedAt = datetime.now()

    session.commit()

    return (True, message_rental_order_constants.MESSAGE_SUCCESS_DELETED)


def restore_rental_order(rental_order_id):
    """
    Set state of rental order and rental order details to normally , remove deleted date

    Argument:
        rental_order_id: parameter
    Returns:
        The message.
    """
    rental_order = session.query(RentalOrders).filter_by(
        rentalOrdersId=rental_order_id).first()

    if rental_order is None:
        return (False, message_rental_order_constants.MESSAGE_ERROR_NOT_EXIST)

    # Update rental order
    rental_order.isDeleted = False
    rental_order.deletedAt = None

    # Update rental order details
    rental_order_details = session.query(RentalOrderDetail).filter_by(
        rentalOrderId=rental_order.rentalOrdersId).all()
    for detail in rental_order_details:
        detail.isDeleted = False
        detail.deletedAt = None

    session.commit()

    return (True, message_rental_order_constants.MESSAGE_SUCCESS_RESTORE)


def update_rental_order(rental_order_id, update_data):
    """
    update 1 record rental order.

    Arguments:
        update_data: json body
        rental_order_id: id of rental order
    Returns:
        Response: Returning a message.
    """
    rental_order = session.query(RentalOrders).filter_by(
        rentalOrdersId=rental_order_id).first()
    if rental_order is None:
        return (False, message_rental_order_constants.MESSAGE_ERROR_NOT_EXIST)

    # Update rental order fields
    rental_order.paymentMethodId = update_data.get(
        "paymentMethodId", rental_order.paymentMethodId)
    rental_order.rentalStatus = update_data.get(
        "rentalStatus", rental_order.rentalStatus)

    session.commit()

    return (True, message_rental_order_constants.MESSAGE_SUCCESS_UPDATED)


def update_rental_order_detail(rental_order_id, rental_order_detail_id, update_data):
    """
    update 1 record rental order details.

    Arguments:
        update_data: json body
        rental_order_id: id of rental order
        rental_order_detail_id: id of rental order details
    Returns:
        Response: Returning a message.
    """
    rental_order = session.query(RentalOrders).filter_by(
        rentalOrdersId=rental_order_id).first()

    if rental_order is None:
        return (False, message_rental_order_constants.MESSAGE_ERROR_NOT_EXIST)

    rental_order_detail = session.query(RentalOrderDetail).filter_by(
        rentalOrderId=rental_order_id, rentalOrdersId=rental_order_detail_id).first()

    if rental_order_detail is None:
        return (False, message_rental_order_details_constants.MESSAGE_ERROR_NOT_EXIST)

    # Update rental order detail fields
    rental_order_detail.vehicleId = update_data.get(
        "vehicleId", rental_order_detail.vehicleId)
    rental_order_detail.optionId = update_data.get(
        "optionId", rental_order_detail.optionId)
    rental_order_detail.quantity = update_data.get(
        "quantity", rental_order_detail.quantity)
    rental_order_detail.amount = update_data.get(
        "amount", rental_order_detail.amount)
    rental_order_detail.rentalStartDate = datetime.strptime(update_data.get(
        "rentalStartDate"), "%Y/%m/%d") if update_data.get("rentalStartDate") else rental_order_detail.rentalStartDate
    rental_order_detail.rentalEndDate = datetime.strptime(update_data.get(
        "rentalEndDate"), "%Y/%m/%d") if update_data.get("rentalEndDate") else rental_order_detail.rentalEndDate

    # Update the totalAmount in rental order
    rental_order.totalAmount = session.query(func.sum(
        RentalOrderDetail.amount)).filter_by(rentalOrderId=rental_order_id).scalar()

    session.commit()

    return (True, message_rental_order_details_constants.MESSAGE_SUCCESS_UPDATED)
