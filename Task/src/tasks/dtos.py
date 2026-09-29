from pydantic import BaseModel


class TaskSchema(
    BaseModel
):  # Task class hai , which is inheritiing from BaseModel class of pydantic library
    title: str
    description: str
    iscompleted: bool = False
