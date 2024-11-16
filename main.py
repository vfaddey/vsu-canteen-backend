from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.dishes.router import router as dish_router
from src.orders.router import router as order_router

app = FastAPI(
    root_path="/api",
    swagger_ui_init_oauth={"clientId": "your-client-id"}
)

app.include_router(dish_router)
app.include_router(order_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)