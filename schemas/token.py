from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str


class LoginTokenSchema(TokenSchema):
    refresh_token: str
