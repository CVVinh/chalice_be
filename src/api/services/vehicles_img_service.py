from api.models.models import VehicleImage, VehiclesMaster
from api.models import session
from api.messages import MessageResponse
from api.utils.utils import add_update_object, object_as_dict, paginate

message_vehicle_img_constant = MessageResponse()
message_vehicle_img_constant.setName("vehicle_img")


def get_vehicles_img_list(query_params):
    """
    Get all record for vehicle_img by params.

    Argument:
        query_params: param search
    Returns:
        Response: Returning a message, lists.
    """
    # Get data of list in DB
    try:
        result_list = session.query(VehicleImage).all()
        vehicle_img_list = [object_as_dict(img)for img in result_list]

        # Paginate by pageNum & pageSize
        paginated_lst = paginate(vehicle_img_list, query_params)
        return True, {
            "vehicle_img_list": paginated_lst,
            "totalRecords": len(vehicle_img_list),
            "message": message_vehicle_img_constant.MESSAGE_SUCCESS_GET_LIST,
            "status": 200
        }
    except Exception as e:
        return False, {
            "message": str(e),
            "status": 500
        }


def create_vehicles_img(query_params):
    """
    Create request and add record for base.

    Argument:
        base_obj: request body
    Returns:
        The message.
    """
    vehicle_img_id = query_params.get("vehicleImageid")
    image = query_params.get("image")
    # Kiểm tra xem vehicle_img đã tồn tại trong cơ sở dữ liệu chưa
    existing_vehicle_img = session.query(VehicleImage).filter(
        VehicleImage.vehicleImageid == vehicle_img_id
    ).first()
    if existing_vehicle_img:
        return (False, "vehicle_img already exists")
    # vehicle_image = query_params.get("vehicleImage")
    # Lưu trữ hình ảnh vào thư mục "img"
    # file_content = image
    # with open(f'src/api/img/{image}.jpg', 'wb') as file:
    #     file.write(file_content)
    # Thêm thông tin hình ảnh vào cơ sở dữ liệu
    new_vehicle_img = VehicleImage(vehicleImageid=vehicle_img_id,
                                   image=f'{image}')
    session.add(new_vehicle_img)
    # session.add(add_update_object(query_params, img))
    session.commit()

    return (True, message_vehicle_img_constant.MESSAGE_SUCCESS_CREATED)


def update_vehicles_img(query_params):
    """
    update 1 record for vehicle_img by id.

    Arguments:
        prefecture_obj: json body
    Returns:
        Response: Returning a message.
    """
    vehicle_img_id = query_params.get("vehicleImageid")

    # Check if the vehicle_img exists in the database
    existing_vehicle_img = session.query(VehicleImage).filter(
        VehicleImage.vehicleImageid == vehicle_img_id
    ).first()
    if existing_vehicle_img:
        # Update the existing vehicle_img object
        add_update_object(query_params, existing_vehicle_img)

        session.commit()

        return True, message_vehicle_img_constant.MESSAGE_SUCCESS_UPDATED
    else:
        return False, message_vehicle_img_constant.MESSAGE_ERROR_NOT_EXIST


def delete_vehicles_img(query_params):
    """
    Delete 1 record for vehicle_img by id.

    Argument:
        query_params: parameter
    Returns:
        The message.
    """
    vehicle_img_id = query_params.get("vehicleImageid")

    # Set vehicle.storeId = None if it match with vehicle_img_id
    vehicle_has_vehicle_img_id = session.query(VehiclesMaster).filter(
        VehiclesMaster.vehicleImageid == vehicle_img_id
    ).all()

    for vehicle in vehicle_has_vehicle_img_id:
        if vehicle.vehicleImageid == vehicle_img_id:
            vehicle.vehicleImageid = None

    vehicle_img = session.query(VehicleImage).filter(
        VehicleImage.vehicleImageid == vehicle_img_id
    ).first()

    if vehicle_img is None:
        return (False, message_vehicle_img_constant.MESSAGE_ERROR_NOT_EXIST)

    session.delete(vehicle_img)
    session.commit()

    return True, {
        "message": message_vehicle_img_constant.MESSAGE_SUCCESS_DELETED,
        "status": 200
    }
