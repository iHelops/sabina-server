from uuid import uuid4
from dtos import UserDto
from exceptions import ApiError
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
import mongoengine


def registration(email: str, phone: str, first_name: str, last_name: str, password: str):
    session = str(uuid4())
    user = User(
        email=email,
        phone=phone,
        first_name=first_name,
        last_name=last_name,
        password=generate_password_hash(password),
        sessions=[session]
    )

    try:
        user.save()
    except mongoengine.errors.NotUniqueError:
        raise ApiError.BadRequest('email already exist')

    user_dict = dict(user.to_mongo())
    user_data = {**UserDto(user_dict).get_dict(), 'session': session}
    return user_data


def login(email: str, password: str):
    user = User.objects(email=email).first()
    if not user or not check_password_hash(user.password, password):
        raise ApiError.BadRequest('wrong login or password')

    session = str(uuid4())
    if len(user.sessions) == 5:
        user.update(pull__sessions=user.sessions[0])

    user.update(push__sessions=session)

    user_dict = dict(user.to_mongo())
    user_data = {**UserDto(user_dict).get_dict(), 'session': session}
    return user_data


def check_auth(session: str):
    try:
        user = User.objects(sessions=session).first()
        user_dict = dict(user.to_mongo())
        user_data = UserDto(user_dict).get_dict()
        return user_data
    except AttributeError:
        raise ApiError.UnauthorizedError()
