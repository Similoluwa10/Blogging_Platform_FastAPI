from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.environ["DATABASE_URL"])
Base = declarative_base()

#code to create tables
Base.metadata.create_all(engine)

# initialize database connection
async def init_db_connection():     
    with engine.connect() as conn:
        print("connected to database")


Session = sessionmaker(bind=engine)
session = Session()
