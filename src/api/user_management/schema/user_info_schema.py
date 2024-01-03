from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class UserInfo(BaseModel):
    # profile_img: Optional[str]
    # first_name: str
    # last_name: Optional[str]
    # email: str
    # phone_number: Optional[str]
    # address: Optional[str]

    profile_img: Optional[str] = None
    first_name: str = None
    last_name: Optional[str] = None
    email: str = None
    phone_number: Optional[str] = None
    address: Optional[str] = None


class UserInfoResponse(BaseModel):
    profile_id: UUID 
    profile_img: Optional[str]
    first_name: str
    last_name: Optional[str]
    email: str
    phone_number: Optional[str]
    address: Optional[str]

    # class config:
    #     orm_mode = True

class UpdateUserInformation(BaseModel):
    profile_id: str
    profile_img: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
