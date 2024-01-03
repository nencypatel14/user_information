import logging
from sqlalchemy.orm import Session
from src.api.user_management.model.user_info_model import UserInformation

def add_user_info(data: dict, db: Session):
    try:
        logging.info(f"adding user info:{data}")
        user = UserInformation(**data)
        db.add(user)
        db.commit()
        db.refresh(user)
        logging.info(f"adding user info: {data} with profile_id: {user.profile_id}")
    except Exception as e:
        logging.error(f"Error: add_user: {e}")
        raise Exception("Internal_Server_Error")
    else:
        logging.info("add user info: Success")
        return user

def get_user_info(profile_id: str, db: Session):
    try:
        logging.info(f"Searching user from databse with profile_id: {profile_id}")
        user = db.query(UserInformation).filter(UserInformation.profile_id == profile_id).first()
        logging.info(f"get user information with profile_id: {user.profile_id}")
    except Exception as e:
        logging.info(f"Error: get_user: {e}")
        raise Exception("Internal_Server_Error")
    else:
        logging.info("get user information: Success")
        return user
    
def update_user_info(data: dict, db: Session):
    try:
        id = data["profile_id"]
        data.pop("profile_id")

        logging.info(f"serching user from database with input id: {id}")
        user = db.query(UserInformation).filter(UserInformation.profile_id == id).first()

        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        logging.info(f"Error: update_user: {e}")
        raise Exception("Internal_Server_Error")
    