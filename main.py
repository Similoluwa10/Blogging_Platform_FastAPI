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
def createUser(user: CreatUserRequest):
    response = services.create_user(user)    
    return response

@app.get("/user/{id}")
def getUser(id: int):
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
def getAllUsers():
    users = services.get_all_users()
    if users:
        return users
    return     
        
@app.put("/user/{id}")
def editUser(id: int, userUpdate: UpdateUserRequest):
    user = services.update_user(id, userUpdate)
    return user

@app.delete("/user/{id}")
def deleteUser(id: int):
    response = services.delete__user(id)
    return response



# routes: BlogPost
@app.post("/blog")
def createBlogPost(blogpost: CreateBlogpostRequest):
    blogpost = services.create_blogpost(blogpost)
    return blogpost

@app.get("/blog/{id}")
def getBlogPostById(id: int):
    blogpost = services.get_blogpost(id)
    return blogpost

# @app.get("/blog")
# def getBlogPostsByFilter():
#     return

@app.get("/blogs")
def getAllBlogPosts():
    blogposts = services.get_all_blogposts()
    return blogposts

@app.put("/blog/{id}")
def editBlogPost(id: int, blogpostUpdate: UpdateBlogpostRequest):
    blogpost = services.update_blogpost(id, blogpostUpdate)
    return blogpost

@app.delete("/blog/{id}")
def deleteBlogPost(id: int):
    response = services.delete_blogpost(id)
    return response
