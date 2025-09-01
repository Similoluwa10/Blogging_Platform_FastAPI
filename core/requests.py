from pydantic import BaseModel, EmailStr, SecretStr
from typing import Union, Optional, List, Dict

#input validation is handled by pydantic
class CreatUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


#update request fields are optional
class UpdateUserRequest(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]


class CreateBlogpostRequest(BaseModel):
    imageUrl: str
    caption: str
    article: str


class UpdateBlogpostRequest(BaseModel):
    imageUrl: str
    caption: str
    article: str
