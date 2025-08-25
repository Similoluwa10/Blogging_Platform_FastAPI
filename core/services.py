from db.database import session
from db.models import User, BlogPost
from core.requests import (
    CreatUserRequest,
    UpdateUserRequest,
    CreateBlogpostRequest,
    UpdateBlogpostRequest,
)


def create_user(userCreate: CreatUserRequest):
    
    #check if username or email already exists    
    usernameExists = session.query(User).filter_by(username=userCreate.username)
    emailExists = session.query(User).filter_by(email=userCreate.email)
    if usernameExists:
        print(usernameExists)
        return{
            "message": "username already exists"
        }
        
    if emailExists:
        return{
            "message": "email already exists"
        }
        
   
    #if username and email are unique, attempt to insert into database
    try:        
        user = User(username=userCreate.username, email=userCreate.email, password=userCreate.password)
        session.add(user)
    except:
        #rollback if operation is unsuccessful
        session.rollback()
        raise
    else:
        session.commit()
        if user:
            return{
                "message": "user created successfully"
            }
            
    return{
        "message": "user creation unsuccessful"
    }


def get_user(id):
    #query database
    user = session.query(User).get(id)
    return user


def get_all_users():
    try: 
        users: list[User] = session.query(User).all()
    except:
        raise
    else:
        return users


def update_user(id, userUpdate: UpdateUserRequest):    
    try:
        user: User = session.query(User).get(id)
    except:
        raise
    else:
        if user:
            user.username = userUpdate.username
            user.email = userUpdate.email

            session.commit()
            return user


def delete__user(id):
    try: 
        user = session.query(User).get(id) 
    except:
        raise
    else:
        session.delete(user)
        session.commit()
        return {
            "message": "user successfully deleted"
            }




def create_blogpost(blogpostCreate: CreateBlogpostRequest):
    try: 
        blogpost = BlogPost(
            imageUrl=blogpostCreate.imageUrl,
            caption=blogpostCreate.caption,
            article=blogpostCreate.article,
        )
        session.add(blogpost)
    
    except:
        raise
    
    else:
        session.commit()
        return blogpost


def get_blogpost(id):
    try:
        blogpost = session.query(BlogPost).get(id)
    except:
        raise
    else:
        return blogpost


def get_all_blogposts():
    try:
        blogposts: list[BlogPost] = session.query(BlogPost).all()
    except:
        raise
    else:
        return blogposts


def update_blogpost(id, blogpostUpdate: UpdateBlogpostRequest):
    try: 
        blogpost: BlogPost = session.query(BlogPost).get(id)

    except:
        raise
    
    else:
        if blogpost:
            blogpost.imageUrl = blogpostUpdate.imageUrl
            blogpost.caption = blogpostUpdate.caption
            blogpost.article = blogpostUpdate.article

            session.commit()

            return blogpost


def delete_blogpost(id):
    try: 
        blogpost = session.query(BlogPost).get(id)
    except:
        raise
    else:
        if blogpost:
            session.delete(blogpost)
            session.commit()

            return {
                "message": "blogpost successfully deleted"
                    }
