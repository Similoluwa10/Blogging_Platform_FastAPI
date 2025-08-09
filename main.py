from fastapi import FastAPI

app = FastAPI()


#routes: User
@app.post("/user")
def createUser():
    pass

@app.get("/user/{id}")
def getUser(id):
    pass

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