# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from db.database import create_db_and_tables
from db.crud import save_item

# Load database metadata before running any pipeline
create_db_and_tables()


class SaveToDBItemPipeline:
    def process_item(self, item, spider):
        save_item(item)
