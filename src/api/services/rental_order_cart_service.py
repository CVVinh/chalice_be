from sqlalchemy.sql import func
from api.models.models import (
    AccountMaster,
    InsurancesMaster,
    OptionsMaster,
    RentalOrderCart,
    VehiclesMaster,
)
from api.models import session
from api.utils.utils import add_update_object, object_as_dict, export, paginate
from api.messages import MessageResponse
from itertools import groupby

mesg_consts = MessageResponse()
mesg_consts.setName("Rental Order Cart Master")


def add_rental_order_cart(rental_order_cart_obj):
    """
    Create request and add record for rental_order_cart

    Args:
        rental_order_cart_obj: request body
    Returns:
        The message
    """
    create_rental_order_cart = RentalOrderCart()
    session.add(add_update_object(
        rental_order_cart_obj, create_rental_order_cart))
    session.commit()
    return (True, mesg_consts.MESSAGE_SUCCESS_CREATED)


def add_multi_rental_order_cart(rental_order_cart_obj):
    """
    Create request and add many record for rental_order_cart

    Args:
        rental_order_cart_obj: request body
    Returns:
        The message
    """
    for item in rental_order_cart_obj:
        create_rental_order_cart = RentalOrderCart()
        session.add(add_update_object(item, create_rental_order_cart))
    session.commit()
    return (True, mesg_consts.MESSAGE_SUCCESS_CREATED)


def update_rental_order_cart_info(rental_order_cart_obj):
    """
    update 1 record for rental_order_cart by id

    Args:
        rental_order_cart_obj: request body
    Returns:
        Response: Returning a message
    """
    rental_orders_cart_id = rental_order_cart_obj.get("rentalOrdersCartId")
    if (
        update_rental_order_cart := session.query(RentalOrderCart)
        .filter(
            RentalOrderCart.rentalOrdersCartId == rental_orders_cart_id,
            RentalOrderCart.isDeleted == 0,
        )
        .first()
    ):
        add_update_object(rental_order_cart_obj, update_rental_order_cart)
        session.commit()
        return (True, mesg_consts.MESSAGE_SUCCESS_UPDATED)
    return (False, mesg_consts.MESSAGE_ERROR_NOT_EXIST)


def delete_soft_rental_order_cart(query_params):
    """
    Delete soft 1 record for rental_order_cart by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    rental_orders_cart_id = query_params.get("rentalOrdersCartId")
    if (
        update_rental_order_cart := session.query(RentalOrderCart)
        .filter(
            RentalOrderCart.rentalOrdersCartId == rental_orders_cart_id,
            RentalOrderCart.isDeleted == 0,
        )
        .first()
    ):
        update_rental_order_cart.isDeleted = 1
        update_rental_order_cart.deletedAt = func.now()
        session.commit()
        return (True, mesg_consts.MESSAGE_SUCCESS_DELETED)
    return (False, mesg_consts.MESSAGE_ERROR_NOT_EXIST)


def delete_hard_rental_order_cart(query_params):
    """
    Delete hard 1 record for rental_order_cart by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """

    rental_orders_cart_id = query_params.get("rentalOrdersCartId")
    if (
        delete_rental_order_cart := session.query(RentalOrderCart)
        .filter(
            RentalOrderCart.rentalOrdersCartId == rental_orders_cart_id,
            RentalOrderCart.isDeleted == 0,
        )
        .first()
    ):
        session.delete(delete_rental_order_cart)
        session.commit()
        return (True, mesg_consts.MESSAGE_SUCCESS_DELETED)
    return (False, mesg_consts.MESSAGE_ERROR_NOT_EXIST)


def delete_soft_multi_rental_order_cart(query_params):
    """
    Delete soft many record for rental_order_cart by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    for item in query_params:
        if (
            update_rental_order_cart := session.query(RentalOrderCart)
            .filter(
                RentalOrderCart.rentalOrdersCartId == item,
                RentalOrderCart.isDeleted == 0,
            )
            .first()
        ):
            update_rental_order_cart.isDeleted = 1
            update_rental_order_cart.deletedAt = func.now()
    session.commit()
    return (True, mesg_consts.MESSAGE_SUCCESS_DELETED)


def get_rental_order_cart_info(query_params):
    """
    get 1 record for rental_order_cart by id

    Args:
        query_params: parameter search
    Returns:
        Response: Returning a message and a object inclue obj
        the rental_order_cart
    """
    filter_param_get_list = filter_param_get_list_rental_order_cart(
        query_params)

    if len(filter_param_get_list) > 0:
        return (
            True,
            {
                "mstRenOrdCartModel": filter_param_get_list,
                "total": len(filter_param_get_list),
                "message": mesg_consts.MESSAGE_SUCCESS_GET_INFO,
                "status": 200,
            },
        )
    return (False, mesg_consts.MESSAGE_ERROR_NOT_EXIST)


def get_rental_order_cart_list(query_params):
    """
    Get 1 or many record for rental_order_cart by params

    Args:
        query_params: param search
    Returns:
        Response: Returning a message, total record, lists
    """
    filter_param_get_list = filter_param_get_list_rental_order_cart(
        query_params)
    handlerGroupByData = handlerInclueData(filter_param_get_list)

    paginated_lst = paginate(handlerGroupByData, query_params)
    return (
        True,
        {
            "mstRenOrdCart": paginated_lst,
            "total": len(paginated_lst),
            "message": mesg_consts.MESSAGE_SUCCESS_GET_LIST,
            "status": 200,
        },
    )


def export_rental_order_cart_list(query_params):
    return export(filter_param_get_list_rental_order_cart(query_params))


def filter_param_get_list_rental_order_cart(query_params):
    """
    Query and search base with parameters

    Args:
        query_params: param search
    Returns:
        Response: Returning a object list

    """
    query_list = session.query(RentalOrderCart).filter(
        RentalOrderCart.isDeleted == 0)
    parameters = [
        "rentalOrdersCartId",
        "accountId",
        "vehicleId",
        "optionId",
        "insuranceId",
        "statusCart",
    ]
    if query_params:
        for param in parameters:
            if param in query_params:
                query_list = query_list.filter(
                    getattr(RentalOrderCart, param) == query_params[param]
                )

    convert_arr_rental_order_cart = [
        object_as_dict(item) for item in query_list.all()]

    return convert_arr_rental_order_cart


def handlerInclueData(list_data):
    # sort data before groupby
    sorted_data = sorted(list_data, key=lambda x: (
        x["accountId"], x["vehicleId"]))

    # group by data by field
    grouped_data = groupby(sorted_data, key=lambda x: (
        x["accountId"], x["vehicleId"]))

    result_list = []
    # handler groupby
    for key, group in grouped_data:
        code, item_of_list = key, list(group)
        obj_account = (
            session.query(AccountMaster)
            .filter(AccountMaster.isDeleted == 0,
                    AccountMaster.accountId == code[0])
            .first()
        )
        obj_vehical = (
            session.query(VehiclesMaster)
            .filter(VehiclesMaster.vehicleId == code[1])
            .first()
        )
        obj_option = []
        obj_insurances = []

        for ele in item_of_list:
            if ele["optionId"] is not None:
                list_options = (
                    session.query(OptionsMaster)
                    .filter(OptionsMaster.optionId == ele["optionId"])
                    .first()
                )
                obj_option.append(list_options)

            if ele["insuranceId"] is not None:
                list_insurances = (
                    session.query(InsurancesMaster)
                    .filter(InsurancesMaster.insuranceId == ele["insuranceId"])
                    .first()
                )
                obj_insurances.append(list_insurances)
        object = {
            "rentalOrderCart": item_of_list,
            "account": {**object_as_dict(obj_account, True)},
            "vehical": {**object_as_dict(obj_vehical, True)},
            "options": [object_as_dict(item) for item in obj_option],
            "insurances": [object_as_dict(item) for item in obj_insurances],
        }
        result_list.append(object)
    return result_list
