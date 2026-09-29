from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes

Base.metadata.create_all(
    bind=engine
)  # ye line database ke tables ko create karne ke liye hai, agar tables exist nahi karte to ye line unhe create karegi


app = FastAPI(
    title="My API", description="This is my API", version="1.0.0"
)  # FastAPI class hai , aur app object hai jo FastAPI class ka instance hai


app.include_router(
    task_routes
)  # ye line task_routes ko app me include karne ke liye hai
