from sqlalchemy.sql import func
from api.models.models import PaymentMethodsMaster
from api.models import session
from api.utils.utils import add_update_object, object_as_dict, export, paginate
from api.messages import MessageResponse

message_payment_method_constant = MessageResponse()
message_payment_method_constant.setName("Payment Methods Master")


def add_payment_method(payment_method_obj):
    """
    Create request and add record for payment_method
    
    Args:
        payment_method_obj: request body
    Returns:
        The message   
    """
    create_payment_method = PaymentMethodsMaster()
    session.add(add_update_object(payment_method_obj, create_payment_method))
    session.commit()
    return (True, message_payment_method_constant.MESSAGE_SUCCESS_CREATED)


def add_multi_payment_method(payment_method_obj):
    """
    Create request and add many record for payment_method
    
    Args:
        payment_method_obj: request body
    Returns:
        The message   
    """
    for item in payment_method_obj:
        create_payment_method = PaymentMethodsMaster()
        session.add(add_update_object(item, create_payment_method))
    session.commit()
    return (True, message_payment_method_constant.MESSAGE_SUCCESS_CREATED)


def update_payment_method_info(payment_method_obj):
    """
    update 1 record for payment_method by id

    Args:
        payment_method_obj: request body
    Returns:
        Response: Returning a message
    """
    payment_method_id = payment_method_obj.get("paymentMethodId")
    if(
        update_to_payment_method := session.query(PaymentMethodsMaster).filter(PaymentMethodsMaster.paymentMethodId == payment_method_id).first()
    ):
        add_update_object(payment_method_obj, update_to_payment_method)
        session.commit()
        return (True, message_payment_method_constant.MESSAGE_SUCCESS_UPDATED)
    return (False, message_payment_method_constant.MESSAGE_ERROR_NOT_EXIST)


def delete_payment_method(query_params):
    """
    Delete 1 record for payment_method by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    payment_method_id = query_params.get("payment_method_id")
    if(
        update_to_payment_method := session.query(PaymentMethodsMaster).filter(PaymentMethodsMaster.paymentMethodId == payment_method_id).first()
    ):
        session.delete(update_to_payment_method)
        session.commit()
        return (True, message_payment_method_constant.MESSAGE_SUCCESS_DELETED)
    return (False, message_payment_method_constant.MESSAGE_ERROR_NOT_EXIST)


def delete_multi_payment_method(query_params):
    """
    Delete many record for payment_method by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    for item in query_params:
        if(
            update_to_payment_method := session.query(PaymentMethodsMaster).filter(PaymentMethodsMaster.paymentMethodId == item).first()
        ):
            session.delete(update_to_payment_method)
    session.commit()
    return (True, message_payment_method_constant.MESSAGE_SUCCESS_DELETED)


def get_payment_method_info(query_params):
    """
    get 1 record for payment_method by id

    Args:
        query_params: parameter search
    Returns:
        Response: Returning a message and a object inclue obj the payment_method
    """
    payment_method_id = query_params.get("payment_method_id")
    if(
       payment_method_info := session.query(PaymentMethodsMaster).filter(PaymentMethodsMaster.paymentMethodId == payment_method_id).first() 
    ):
        tmp_payment_method_info = {
            **object_as_dict(payment_method_info, True), 
            "message": message_payment_method_constant.MESSAGE_SUCCESS_GET_INFO,
            "status": 200
        }
        return (True, tmp_payment_method_info)
    return (False, message_payment_method_constant.MESSAGE_ERROR_NOT_EXIST)


def get_payment_method_list(query_params):
    """
    Get 1 or many record for payment_method by params

    Args:
        query_params: param search
    Returns:
        Response: Returning a message, total record, lists 
    """
    filter_param_get_list = filter_param_get_list_payment_method(query_params)
    paginated_lst = paginate(filter_param_get_list, query_params)
    return (True, {"mstPaymentMethods": paginated_lst,
                   "total": len(paginated_lst),
                   "message": message_payment_method_constant.MESSAGE_SUCCESS_GET_LIST,
                   "status": 200})


def export_payment_method_list(query_params):
    return export(filter_param_get_list_payment_method(query_params))


def filter_param_get_list_payment_method(query_params):
    """
    Query and search base with parameters

    Args:
        query_params: param search
    Returns:
        Response: Returning a object list
    """
    query_list_payment_method = session.query(PaymentMethodsMaster)
    if query_params:
        if "payment_method_id" in query_params:
            query_list_payment_method = query_list_payment_method.filter(PaymentMethodsMaster.paymentMethodId == query_params["payment_method_id"])

        if "payment_method_name" in query_params:
            query_list_payment_method = query_list_payment_method.filter(PaymentMethodsMaster.paymentMethodName.like(f"%{query_params['payment_method_name']}%"))

    return [object_as_dict(payment_method) for payment_method in query_list_payment_method.all()]


