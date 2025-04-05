from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr
    phone: str = Field(max_length=20)
    birthday: Optional[date] = None
    extra_info: Optional[str] = Field(default=None, max_length=250)


# Схема для створення контакту
class ContactCreate(ContactBase):
    pass


# Схема для оновлення контакту
class ContactUpdate(ContactBase):
    pass


# Схема відповіді (з бази)
class ContactResponse(ContactBase):
    id: int
    done: bool

    model_config = ConfigDict(from_attributes=True)
