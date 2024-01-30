from datetime import timedelta

from fastapi import APIRouter

from config import settings
from db.user import User
from exceptions.http import LoginUserError, UserPasswordError
from extras.context_request import request
from schemas.base import Success
from schemas.token import LoginTokenSchema
from schemas.user import ChangePasswordSchema
from schemas.user import UserInfoSchema, LoginInfoSchema
from services.auth import create_access_token, require_login

user_router = APIRouter(prefix="/user", tags=["用户"])


@user_router.post("/login", response_model=LoginTokenSchema, name="登录")
async def login(login_info: LoginInfoSchema):
    user = await User.authenticate(login_info.username, login_info.password)
    if not user:
        raise LoginUserError
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        {"user_id": user.id}, expires_delta=access_token_expires
    )
    return LoginTokenSchema(access_token=access_token, refresh_token="xxx")


@user_router.get(
    "/userinfo", response_model=UserInfoSchema, name="用户信息", description="用户信息"
)
@require_login
async def userinfo():
    return UserInfoSchema.from_orm(request.current_user)


@user_router.post("/change_password", response_model=Success, name="修改密码")
@require_login
async def change_password(data: ChangePasswordSchema):
    if not request.current_user.verify(data.old_password):
        raise UserPasswordError

    if data.new_password != data.confirm_password:
        raise UserPasswordError("两次密码不一样，请在检查一下")

    await request.current_user.reset_password(data.new_password)
    return Success("修改成功")
