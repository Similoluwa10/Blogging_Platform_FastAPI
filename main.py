from fastapi import FastAPI
from db.database import init_db_connection
from contextlib import asynccontextmanager
from core import services

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db_connection()
    yield

app = FastAPI(lifespan=lifespan)
    
#routes: User
@app.post("/user")
def createUser():
    return

@app.get("/user/{id}")
def getUser(id):
    return

@app.get("/users")
def getAllUsers():
    return

@app.put("/user/{id}")
def editUser(id):
    return

@app.delete("/user/{id}")
def deleteUser(id):
    return


#routes: BlogPost
@app.post("/blog")
def createBlogPost():
    return

@app.get("/blog/{id}")
def getBlogPostById(id: int):
    pass

@app.get("/blog")
def getBlogPostsByFilter():
    return

@app.get("/blogs")
def getAllBlogPosts():
    return

@app.put("/blog")
def editBlogPost():
    return

@app.delete("/blog")
def deleteBlogPost():
    return



