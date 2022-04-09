import logging

from sqlalchemy.exc import SQLAlchemyError

from db.database import get_db_session


def save_item(item):
    with get_db_session() as session:
        try:
            session.add(item)
            session.commit()
        except SQLAlchemyError as e:
            logging.warning(e)
