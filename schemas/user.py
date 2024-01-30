from pydantic import BaseModel, Field
from .base import ORMModel


class LoginInfoSchema(BaseModel):
    username: str
    password: str


class UserInfoSchema(ORMModel):
    id: int
    username: str


class ChangePasswordSchema(BaseModel):
    old_password: str = Field(alias="oldPassword")
    new_password: str = Field(alias="newPassword")
    confirm_password: str = Field(alias="confirmPassword")
