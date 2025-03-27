from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

# Connect SQLite
sqlite_url = "sqlite:///event_logs.db"
engine = create_engine(sqlite_url, echo=True)

def enable_foreign_keys():
    with engine.connect() as connection:
        connection.exec_driver_sql("PRAGMA foreign_keys=ON;")  # Enable FK constraints

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

    # Call this function at startup
    enable_foreign_keys()

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
