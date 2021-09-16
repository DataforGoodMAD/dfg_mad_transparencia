from contextlib import contextmanager
import os

from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, client_encoding="utf8", echo=True)


def create_db_and_tables(engine=engine):
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_db_session(engine=engine):
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


# if __name__ == "__main__":
#     create_db_and_tables()
