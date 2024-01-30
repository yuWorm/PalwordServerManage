from fastapi import HTTPException
from starlette import status


class BaseHTTPException(HTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "请求异常"

    def __init__(self, detail: str = None, status_code: int = None):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = detail
        else:
            self.detail = self.default_detail
        super().__init__(self.status_code, self.detail)


class TokenError(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "登录信息异常"


class LoginUserError(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "账号或密码错误"


class RCONTimeoutError(BaseHTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "命令发送识别，请稍后在重试"


class RCONSettingError(BaseHTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "RCON服务配置异常，请检测RCON服务在进行使用"


class ContainerNotFoundError(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "游戏容器未找到，请前往文档寻找解决办法"


class DockerRuntimeError(BaseHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "docker容器异常"


class UserPasswordError(BaseHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "密码错误"
