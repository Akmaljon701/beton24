from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes import auth, users, costumers, orders, journey, seh, cars
from db import Base, engine

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Crud group",
    responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
               401: {'desription': 'Unauthorized'}}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.login_router, prefix='/auth', tags=['User auth section'],)
app.include_router(users.router_user, prefix='/user', tags=['User apis'],)
app.include_router(costumers.router_costumer, prefix='/costumer', tags=['Costumer apis'],)
app.include_router(orders.router_order, prefix='/order', tags=['Order apis'],)
app.include_router(journey.router_journey, prefix='/journey', tags=['Journey apis'],)
app.include_router(seh.router_seh, prefix='/seh', tags=['Seh apis'],)
app.include_router(cars.router_cars, prefix='/cars', tags=['Cars apis'],)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Crud group",
        version="3.8.10",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
