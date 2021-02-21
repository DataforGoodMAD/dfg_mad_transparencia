# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from db.database import get_db, create_tables, engine

create_tables()


class SaveToDBItemPipeline:
    def process_item(self, item, spider):
        item.commit_item(engine=engine, excluded_fields=['id'])
        return item
