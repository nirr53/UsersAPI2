import traceback

from fastapi import Request, status, FastAPI
from fastapi.responses import JSONResponse


def handle_error(error_type: Exception, error_message: str, status_code: int) -> JSONResponse:
    """ Handle errors coming from resources

    :param error_type: Type of error
    :param error_message: Error message to add to json response
    :param status_code: HTTP status code
    :return: Json response contains error message, error type and http status code
    """
    traceback_msg = traceback.format_exception(etype=type(error_type), value=error_type, tb=error_type.__traceback__)
    return JSONResponse(
        status_code=status_code,
        content={
            'status': "failure",
            'error_message': error_message,
            'error_type': error_type.__class__.__name__,
            'error_traceback': "".join(traceback_msg),
        }
    )


def global_unhandled_error_handler(request: Request, exc: Exception) -> JSONResponse:
    """ Handle unhandled errors

    :param request: Incoming http request
    :param exc: Current active exception
    :return: Json response contains error message, error type and http status code
    """
    msg = f'Unhandled exception is caught, exception: {exc.args[0]}'
    return handle_error(exc, msg, status.HTTP_503_SERVICE_UNAVAILABLE)


def add_exceptions_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, global_unhandled_error_handler)
