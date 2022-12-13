from typing import Dict

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


from UsersAPI.endpoints.exceptions import add_exceptions_handlers, api

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="User api",
        version="1.0.0",
        description="API for users, just define the users and use them",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
app.include_router(api.router)
add_exceptions_handlers(app)


@app.get('/')
def root() -> Dict[str, str]:
    return {'message': 'Welcome to Users API'}


if __name__ == '__main__':
    uvicorn.run('UsersAPI.main:app', host='0.0.0.0', port=8000, reload=True)
