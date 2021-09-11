# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from db.database import create_db_and_tables, get_db_session

# from models.boe_disposition import BoeDisposition
from models.departamento import Departamento

# Load database metadata before running any pipeline
create_db_and_tables()


class SaveToDBItemPipeline:
    def process_item(self, item, spider):
        with get_db_session() as session:
            session.add(item)
            session.commit()
