from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from extras.context_request import request_var


async def add_context_request(request: Request, call_next):
    token = request_var.set(request)
    try:
        response = await call_next(request)
        return response
    finally:
        request_var.reset(token)
