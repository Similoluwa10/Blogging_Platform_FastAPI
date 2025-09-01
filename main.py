from fastapi import FastAPI
from db.database import init_db_connection
from contextlib import asynccontextmanager
from db.models import User
from core import services
from core.requests import CreatUserRequest, UpdateUserRequest, CreateBlogpostRequest, UpdateBlogpostRequest

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db_connection()
    yield


app = FastAPI(lifespan=lifespan)


# routes: User
@app.post("/user")
def create_user(user: CreatUserRequest):
    response = services.create_user(user)    
    return response

@app.get("/user/{id}")
def get_user(id: int):
    user = services.get_user(id)
    if user:
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "blogposts": user.blog_posts,
        }
    return{
        "message": "error in retrieving user"
    }

@app.get("/users")
def get_all_users():
    users = services.get_all_users()
    if users:
        return users
    return     
        
@app.put("/user/{id}")
def edit_user(id: int, userUpdate: UpdateUserRequest):
    response = services.update_user(id, userUpdate)
    return response

@app.delete("/user/{id}")
def delete_user(id: int):
    response = services.delete__user(id)
    return response


# routes: BlogPost
@app.post("/blog")
def create_blogpost(blogpost: CreateBlogpostRequest):
    response = services.create_blogpost(blogpost)
    return response

@app.get("/blog/{id}")
def get_blogpost(id: int):
    response = services.get_blogpost(id)
    return response

@app.get("/blogs")
def get_all_blogposts():
    response = services.get_all_blogposts()
    return response

@app.put("/blog/{id}")
def edit_blogpost(id: int, blogpostUpdate: UpdateBlogpostRequest):
    response = services.update_blogpost(id, blogpostUpdate)
    return response

@app.delete("/blog/{id}")
def delete_blogpost(id: int):
    response = services.delete_blogpost(id)
    return response

#to add response model to controllers
#create blogpost and user response models
