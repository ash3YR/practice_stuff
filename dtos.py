from pydantic import BaseModel


class productdto(
    BaseModel
):  # productDTO class hai , which is inheritiing from BaseModel class of pydantic library
    id: int
    name: str
    price: float = 0.0
    count: int = 0
