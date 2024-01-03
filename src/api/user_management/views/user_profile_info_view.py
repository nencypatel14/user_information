import logging
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from database.db import get_db
from src.api.user_management.repository.user_info_repository import add_user_info, get_user_info, update_user_info
from src.api.user_management.schema.user_info_schema import UserInfo, UserInfoResponse, UpdateUserInformation


router = APIRouter(prefix="/user")

@router.post("/add", response_model=UserInfoResponse)
async def add_user(user_data: UserInfo, db: Session = Depends(get_db)):
    try:
        logging.info(f"add user: {user_data}")

        if not user_data.first_name or user_data.email: 
            logging.warning("please enter first_name or email.")
            raise Exception("Please Enter valid first_name or email")

        user = add_user_info(user_data.__dict__,db)
        logging.info(f"added user info: {user} with profile_id: {user.profile_id}")
        return user
    except Exception as e:
        raise Exception("Internal_Server_Error")
    
@router.get("/get/{id}", response_model=UserInfoResponse)
async def get_user(id: str, db: Session = Depends(get_db)):
    try:    
        logging.info(f"get user with data: {id}")
        user = get_user_info(id, db)
        return user
    except Exception as e:
        raise Exception("Internal_Server_Error")
    
@router.delete("/delete/")
async def delete_user(profile_id: str = None, db:Session = Depends(get_db)):
    if not profile_id:  
        logging.warning("Please Enter prfile_id.")
        return{"message":"Please Enter valid profile_id."}

    user = get_user_info(profile_id, db)
    logging.info(f"Delete user: {user} from database with profile_id: {user.profile_id}")

    db.delete(user)
    db.commit()
    logging.info("Delete user: Success")
    return "Delete User Information"

@router.post("/update/")
async def update_user(user_data: UpdateUserInformation, db: Session = Depends(get_db)):
    try:
        logging.info(f"update user id: {user_data} with data: {user_data}")

        data = {k: v for k, v in user_data.__dict__.items() if v is not None}

        user = update_user_info(data, db=db)
        if user:
            return jsonable_encoder(user)
            
        logging.info(f"Updated user information with profile_id: {user.profile_id}")
    except ArithmeticError as e:
        logging.error(f"Error - id: {e}")
        raise Exception("Internal_server_error")
    

# @router.delete("/delete/{profile_id}")

