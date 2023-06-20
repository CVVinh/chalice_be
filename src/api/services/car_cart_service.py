# from logging import log
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
from datetime import datetime
import json

mesg_const = MessageResponse()
mesg_const.setName("Rental Order Cart Master")


def add_car_cart(car_cart_obj):
    """
    Create request and add record for car_cart

    Args:
        car_cart_obj: request body
    Returns:
        The message
    """
    create_car_cart = RentalOrderCart()
    session.add(add_update_object(car_cart_obj, create_car_cart))
    session.commit()
    return (True, mesg_const.MESSAGE_SUCCESS_CREATED)


def update_car_cart_info(car_cart_obj):
    """
    update 1 record for car_cart by id

    Args:
        car_cart_obj: request body
    Returns:
        Response: Returning a message
    """
    car_cart_id = car_cart_obj.get("carCartId")
    if (
        update_car_cart := session.query(RentalOrderCart)
        .filter(
            RentalOrderCart.carCartId == car_cart_id,
            RentalOrderCart.isDeleted == 0,
            RentalOrderCart.statusCart == 0,
        )
        .first()
    ):
        add_update_object(car_cart_obj, update_car_cart)
        session.commit()
        return (True, mesg_const.MESSAGE_SUCCESS_UPDATED)
    return (False, mesg_const.MESSAGE_ERROR_NOT_EXIST)


def delete_soft_car_cart(query_params):
    """
    Delete soft 1 record for car_cart by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    car_cart_id = query_params.get("carCartId")
    if (
        update_car_cart := session.query(RentalOrderCart)
        .filter(
            RentalOrderCart.carCartId == car_cart_id,
            RentalOrderCart.isDeleted == 0,
            RentalOrderCart.statusCart == 0,
        )
        .first()
    ):
        update_car_cart.isDeleted = 1
        update_car_cart.deletedAt = func.now()
        session.commit()
        return (True, mesg_const.MESSAGE_SUCCESS_DELETED)
    return (False, mesg_const.MESSAGE_ERROR_NOT_EXIST)


def delete_hard_car_cart(query_params):
    """
    Delete hard 1 record for car_cart by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    car_cart_id = query_params.get("carCartId")
    if (
        delete_car_cart := session.query(RentalOrderCart)
        .filter(
            RentalOrderCart.carCartId == car_cart_id,
            RentalOrderCart.isDeleted == 0,
        )
        .first()
    ):
        session.delete(delete_car_cart)
        session.commit()
        return (True, mesg_const.MESSAGE_SUCCESS_DELETED)
    return (False, mesg_const.MESSAGE_ERROR_NOT_EXIST)


def delete_soft_multi_car_cart(query_params):
    """
    Delete soft many record for car_cart by id

    Args:
        query_params: parameter
    Returns:
        Response: Returning a message
    """
    for item in query_params:
        if (
            update_car_cart := session.query(RentalOrderCart)
            .filter(
                RentalOrderCart.carCartId == item,
                RentalOrderCart.isDeleted == 0,
            )
            .first()
        ):
            update_car_cart.isDeleted = 1
            update_car_cart.deletedAt = func.now()
    session.commit()
    return (True, mesg_const.MESSAGE_SUCCESS_DELETED)


def get_car_cart_info(query_params):
    """
    get 1 record for car_cart by id

    Args:
        query_params: parameter search
    Returns:
        Response: Returning a message and a object inclue obj
        the car_cart
    """
    filter_param_get_list = filter_param_get_list_car_cart(
        query_params)

    if len(filter_param_get_list) > 0:
        return (
            True,
            {
                "mstRenOrdCartModel": filter_param_get_list,
                "total": len(filter_param_get_list),
                "message": mesg_const.MESSAGE_SUCCESS_GET_INFO,
                "status": 200,
            },
        )
    return (False, mesg_const.MESSAGE_ERROR_NOT_EXIST)


def get_car_cart_list(query_params):
    """
    Get 1 or many record for car_cart by params

    Args:
        query_params: param search
    Returns:
        Response: Returning a message, total record, lists
    """
    filter_param_get_list = filter_param_get_list_car_cart(
        query_params)
    handlerGroupByData = handlerInclueData(filter_param_get_list)
    paginated_lst = paginate(handlerGroupByData, query_params)
    return (
        True,
        {
            "mstRenOrdCart": paginated_lst,
            "total": len(paginated_lst),
            "message": mesg_const.MESSAGE_SUCCESS_GET_LIST,
            "status": 200,
        },
    )


def export_car_cart_list(query_params):
    return export(filter_param_get_list_car_cart(query_params))


def filter_param_get_list_car_cart(query_params):
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
        "carCartId",
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

    convert_arr_car_cart = [
        object_as_dict(item, True) for item in query_list.all()]

    return convert_arr_car_cart


def handlerInclueData(list_data):
    """
    Handler including foreign key data

    Args:
        list_data: array object

    Returns:
        Response: Returning a object list
    """
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
            "options": [object_as_dict(ele, True) for ele in obj_option],
            "insurances": [object_as_dict(ele, True) for ele in obj_insurances]
        }
        result_list.append(object)
    return result_list


def get_list_car_cart(query_params):
    """
    Get all account list.

    Argument:
        query_params: parameter
    Returns:
        The message and a list of accounts.
    """
    parameters = [
        "carCartId",
        "accountId",
        "vehicleId",
        "optionId",
        "insuranceId",
        "statusCart",
    ]
    query_list = session.query(RentalOrderCart).filter(
        RentalOrderCart.isDeleted == 0)

    if query_params:
        for param in parameters:
            if param in query_params:
                query_list = query_list.filter(
                    getattr(RentalOrderCart, param) == query_params[param]
                )

    if query_list.first is None:
        return (True, {
            "carCartList": None,
            "message": mesg_const.MESSAGE_ERROR_NOT_EXIST,
            "status": 404
        })
    else:
        result_list = get_car_cart(query_list)
        return (True, {
            "carCartList": result_list,
            "message": mesg_const.MESSAGE_SUCCESS_GET_LIST,
            "status": 200,
        })


def datetime_cv(o):
    if isinstance(o, datetime):
        return o.isoformat()


def get_car_cart(car_card_obj):
    result_list = []
    for car_cart in car_card_obj.all():
        list = {
            "carCartId": car_cart.carCartId,
            "accountId": car_cart.accountId,
            "vehicleId": car_cart.vehicleId,
            "optionId": car_cart.optionId,
            "insuranceId": car_cart.insuranceId,
            "rentalStartDate": car_cart.rentalStartDate,
            "rentalEndDate": car_cart.rentalEndDate,
            "totalHour": car_cart.totalHour,
            "totalHourCar": car_cart.totalHourCar,
            "totalOption": car_cart.totalOption,
            "totalInsurance": car_cart.totalInsurance,
            "totalCost": car_cart.totalCost,
            "statusCart": car_cart.statusCart,
            "createdAt": car_cart.createdAt,
            "createdBy": car_cart.createdBy,
            "modifiedAt": car_cart.modifiedAt,
            "modifiedBy": car_cart.modifiedBy,
            "deletedAt": car_cart.deletedAt,
            "deletedBy": car_cart.deletedBy,
            "isDeleted": car_cart.isDeleted
        }
        options = []
        insurances = []
        option_id = car_cart.optionId
        insurance_id = car_cart.insuranceId
        vehicle_id = car_cart.vehicleId
        if option_id is not None:
            option_ids = [int(id) for id in option_id.split(",")]
            for id in option_ids:
                option = session.query(OptionsMaster).get(int(id))
                if option:
                    option_data = {
                        "optionId": option.optionId,
                        "optionName": option.optionName,
                        "optionValue": option.optionValue,
                    }
                    options.append(option_data)
        if insurance_id is not None:
            insurance_ids = [int(id) for id in insurance_id.split(",")]
            for id in insurance_ids:
                insurance = session.query(InsurancesMaster).get(int(id))
                if insurance:
                    insurance_data = {
                        "insuranceId": insurance.insuranceId,
                        "insuranceName": insurance.insuranceName,
                        "insuranceValue": insurance.insuranceValue,
                    }
                    insurances.append(insurance_data)
        vehicle = session.query(VehiclesMaster).filter(
            VehiclesMaster.vehicleId == vehicle_id).first()
        if vehicle is None:
            return (False, "Vehicle Master dose not exit!")
        vehicle_data = {
            "vehicleId": vehicle.vehicleId,
            "vehicleName": vehicle.vehicleName,
            "makerId": vehicle.makerId,
            "storeId": vehicle.storeId,
            "vehicleStatus": vehicle.vehicleStatus,
            "vehicleSeat": vehicle.vehicleSeat,
            "vehicleModel": vehicle.vehicleModel,
            "vehicleValue": vehicle.vehicleValue,
            "vehicleDescribe": vehicle.vehicleDescribe,
            "year": vehicle.year,
            "mileage": vehicle.mileage,
            "vehicleEngine": vehicle.vehicleEngine,
            "vehicleRating": vehicle.vehicleRating,
            "vehicleConsumedEnergy": vehicle.vehicleConsumedEnergy
        }
        list["vehicles"] = vehicle_data
        list["options"] = options
        list["insurances"] = insurances
        list["rentalStartDate"] = datetime_cv(car_cart.rentalStartDate)
        list["rentalEndDate"] = datetime_cv(car_cart.rentalEndDate)
        json_data = json.dumps(list, default=datetime_cv)
        data = json.loads(json_data)
        result_list.append(data)

    return result_list
