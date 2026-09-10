from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    junior = "junior"
    mid = "mid"
    senior = "senior"

class UserStatus(str, Enum):
    inProgress = "inProgress"
    selected = "selected"
    rejected = "rejected"

class CreateUser(BaseModel):
    name:str = Field(min_length=1, max_length=100)
    role:UserRole = UserRole.junior

class UserUpdate(BaseModel):
    name:Optional[str] = Field(default=None, max_length=100)
    role:Optional[UserRole] = None
    status:Optional[UserStatus] = None

class UserResponse(BaseModel):
    id:str
    name:str
    role:UserRole
    status:UserStatus