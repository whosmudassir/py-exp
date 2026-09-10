from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import uuid
from app.schemas.userSchema import UserStatus, UserRole, UserResponse, UserUpdate, CreateUser
from app.storage.store import load_data, save_data

router = APIRouter(prefix="/api/v1/users", tags=["users"])


#----CREATE----
@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload:CreateUser):
    users = load_data()
    new_user = {
        "id": str(uuid.uuid4()),
        "name":payload.name,
        "role":payload.role,
        "status": UserStatus.inProgress
    }
    users.append(new_user)
    save_data(users)
    return new_user


#----READ----
@router.get('/', response_model=list[UserResponse])
def get_users():
    users = load_data()
    return users

@router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id:str):
    users = load_data()
    for user in users:
        if user["id"]==user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    

#----UPDATE----
@router.patch('/{user_id}', response_model=UserResponse)
def update_user(user_id:str, payload:UserUpdate):
    users = load_data()
    for index, user in enumerate(users):
        if user["id"]==user_id:
            updated_user = user.copy()
            if payload.name is not None:
                updated_user["name"]=payload.name
            if payload.role is not None:
                updated_user["role"]=payload.role
            if payload.status is not None:
                updated_user["status"]=payload.status
            users[index]=updated_user
            save_data(users)
            return updated_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")    

#----DELETE----
@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id):
    users = load_data()
    for index, user in enumerate(users):
        if user["id"]==user_id:
            del users[index]
            save_data(users)   
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
        
    



