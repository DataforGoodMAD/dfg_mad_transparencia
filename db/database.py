import os
from sqlmodel import SQLModel, create_engine, Session
from models import *

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


POSTGRES_USERNAME = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    client_encoding="utf8",
)


def create_db_and_tables(engine=engine):
    SQLModel.metadata.create_all(engine)


# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )

# Base = declarative_base()


# def create_tables():
#     return Base.metadata.create_all(bind=engine)


@contextmanager
def get_db_session(engine=engine):
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


if __name__ == "__main__":
    create_db_and_tables()
