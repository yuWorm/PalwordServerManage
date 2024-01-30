import functools
from datetime import timedelta, datetime, timezone
from typing import Union

from db.user import User
from exceptions.http import TokenError
from config import settings
from jose import jwt, JWTError
from extras.context_request import request


ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def parse_token(token: str) -> int:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise TokenError
        return user_id
    except JWTError:
        raise TokenError


def require_login(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # print("调用登录")
        token: str = request.headers.get("Authorization")
        if not token:
            raise TokenError
        if not token.startswith("Bearer "):
            raise TokenError

        raw_tokens = token.split(" ")
        if len(raw_tokens) != 2:
            raise TokenError

        raw_token = raw_tokens[1]

        user_id = await parse_token(raw_token)
        user: User = await User.get(id=user_id)
        if not user:
            raise TokenError

        request.current_user = user
        return await func(*args, **kwargs)

    return wrapper
