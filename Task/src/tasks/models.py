from sqlalchemy import column, Integer, String, DateTime, Boolean
from utils.db import Base  # Base is responsible to connect model to actual db


class TaskModel(
    Base
):  # kuch bhi naam dede sakte hai class ko, ye class table ka representation hai database me
    __tablename__ = "tasks"  # ye table ka name hai jo database me create hoga

    id = column(Integer, primary_key=True, index=True)
    title = column(String, nullable=False)
    description = column(String, nullable=True)
    iscompleted = column(Boolean, default=False)
