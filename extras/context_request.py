from contextvars import ContextVar
from typing import Any, Type
from fastapi import Request

# from db.user import User


class CurrentRequest(Request):
    """
    主要用来做语法提示
    """


def bind_request_context_var(context: ContextVar):
    class ContextVarBind:
        __slots__ = ()

        def __getattribute__(self, name):
            return getattr(context.get(), name)

        def __setattr__(self, name, value):
            setattr(context.get(), name, value)

        def __delattr__(self, name):
            delattr(context.get(), name)

        def __getitem__(self, index, value):
            return context.get()[index]

        def __setitem__(self, index, value):
            context.get()[index] = value

        def __delitem__(self, index):
            del context.get()[index]

    return ContextVarBind()


request_var: ContextVar[Request] = ContextVar("request")
request: Request | CurrentRequest | Any = bind_request_context_var(request_var)
