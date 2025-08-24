from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.environ["DATABASE_URL"])
Base = declarative_base()

#initialize database connection
async def init_db_connection():     
    connection = engine.connect()
    print("connected to database")
    
    #create database tables
    Base.metadata.create_all(engine)
    print("creating database tables")
    
    connection.close()   
    print("closing connection")    
    
    
Session = sessionmaker(bind=engine)
session = Session()

