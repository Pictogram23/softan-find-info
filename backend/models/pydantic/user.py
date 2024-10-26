from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    token: Optional[str] = None
    refresh_token: Optional[str] = None
    google_uid: Optional[str] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    token: Optional[str] = None
    refresh_token: Optional[str] = None
    google_uid: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    token: Optional[str] = None
    refresh_token: Optional[str] = None
    google_uid: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
