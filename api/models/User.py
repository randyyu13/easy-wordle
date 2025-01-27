from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[int]  # ID can be None for new users
    is_guest: bool
    guest_id: Optional[str]  # Guest ID may be None if it's a registered user
    username: str
    email: EmailStr  # Ensures valid email format
