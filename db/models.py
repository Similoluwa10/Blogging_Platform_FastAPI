from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from db.database import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    blog_posts = relationship("BlogPost", back_populates="user")


class BlogPost(Base):
    __tablename__ = "blogposts"

    id = Column(Integer(), primary_key=True)
    imageUrl = Column(String(50), nullable=True)
    caption = Column(String(50))
    article = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    user_id = Column(Integer(), ForeignKey("users.id"))
    user = relationship("User", back_populates="blog_posts")
    
