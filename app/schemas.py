from typing import Annotated
from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict

NameStr = Annotated[str, StringConstraints(min_length = 2, max_length = 50)]

class UserCreate(BaseModel):
    name: NameStr
    email: EmailStr
    age: int = Field(gt = 18)

class UserRead(BaseModel):
    id: int
    name: NameStr
    email: EmailStr
    age: int

    model_config = ConfigDict(from_attributes = True)

class TaskCreate(BaseModel):
    title: Annotated[str, StringConstraints(min_length = 2)]
    user_id: int

class TaskRead(BaseModel):
    title: Annotated[str, StringConstraints(min_length = 2)]
    user_id: int

    model_config = ConfigDict(from_attributes = True)