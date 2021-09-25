from entities.user import User


def test_check_user_01(user_service):
    response = user_service.get_user(2)
    json_response = response.json()
    data_json_response = json_response["data"]

    assert data_json_response["email"] == "janet.weaver@reqres.in"


def test_check_user_02(user_service):
    response = user_service.get_user(2)
    json_response = response.json()
    data_json_response = json_response["data"]
    keys = ["email", "first_name"]

    assert all(key in data_json_response for key in keys)


def test_check_user_03(user_service, first_user):
    response = user_service.get_user(1)
    json_response = response.json()
    data_json_response = json_response["data"]
    actual_user = User(
        data_json_response["id"],
        data_json_response["email"],
        data_json_response["first_name"],
        data_json_response["last_name"],
        data_json_response["avatar"],
    )
    assert actual_user == first_user
