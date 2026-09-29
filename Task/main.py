from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.models import TaskModel

Base.metadata.create_all(
    bind=engine
)  # ye line database ke tables ko create karne ke liye hai, agar tables exist nahi karte to ye line unhe create karegi


app = FastAPI(
    title="My API", description="This is my API", version="1.0.0"
)  # FastAPI class hai , aur app object hai jo FastAPI class ka instance hai
