from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

load_dotenv()


DB_PATH = "/media/ram/New Volume/my-svelte-app/backend/test.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

print(">>> Using database at:", DATABASE_URL) 

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

