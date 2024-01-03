from sqlalchemy import Column, DateTime, Boolean, String
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from database.db import Base

class UserInformation(Base):
    __tablename__ = "user_info"

    profile_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)  
    profile_img = Column(String)
    first_name = Column(String(length=20), nullable=False)
    last_name = Column(String(length=20), nullable=False)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)

    is_active = Column(Boolean, default=False)  
    created_at = Column(DateTime, default=datetime.utcnow())
    created_by = Column(String, default=False)
    modify_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    modify_by = Column(String)  
    