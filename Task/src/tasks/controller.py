from Task.src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel


def create_task(body: TaskSchema, db: Session):

    data = body.model_dump()  # ye line body ko dictionary me convert karne ke liye hai

    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        iscompleted=data["iscompleted"],
    )  # ye line new_task object create karne ke liye hai

    db.add(new_task)  # ye line new_task object ko database me add karne ke liye hai
    db.commit()  # ye line database me changes ko commit karne ke liye hai
    db.refresh(
        new_task
    )  # ye line new_task object ko database me refresh karne ke liye hai

    return {"message": "Task created successfully"}
