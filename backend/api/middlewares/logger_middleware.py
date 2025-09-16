import datetime
import time
from collections.abc import Callable
from typing import Any
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from urllib3 import request

class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Any]
    ) -> Response:
        """
        Logs all incoming and outgoing request, response pairs. This method logs the request params,
        datetime of request, duration of execution. Logs should be printed using the custom logging module provided.
        Logs should be printed so that they are easily readable and understandable.

        :param request: Request received to this middleware from client (it is supplied by FastAPI)
        :param call_next: Endpoint or next middleware to be called (if any, this is the next middleware in the chain of middlewares, it is supplied by FastAPI)
        :return: Response from endpoint
        """

        # TODO:(Member) Finish implementing this method
        response = await call_next(request)
        return response

        def custom_log_info(message: str):
            print(f"[LOG] {message}")

        start_time = time.time()
        request_time = datetime.datetime.now().isoformat()

        custom_log_info(
                    f"Incoming Request: {request.method} {request.url.path} | "
                    f"Datetime of request: {request_time} | "
                )

        response = await call_next(request)

        process_time = time.time() - start_time

        custom_log_info(
            f"Outgoing Response: {response.status_code} | "
            f"Duration of execution: {process_time:.2f}s | "
        )

        return response