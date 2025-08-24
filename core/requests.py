from pydantic import BaseModel, EmailStr, SecretStr
from typing import Union, Optional, List, Dict

#input validation is handled by pydantic
class CreatUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UpdateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class CreateBlogpostRequest(BaseModel):
    imageUrl: str
    caption: str
    article: str


class UpdateBlogpostRequest(BaseModel):
    imageUrl: str
    caption: str
    article: str
