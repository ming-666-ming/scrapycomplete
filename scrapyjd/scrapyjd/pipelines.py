# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo

from itemadapter import ItemAdapter


class MongoPipeline:
    def __init__(self, mongo_db, mongo_url, mongo_port):
        self.mongo_db = mongo_db
        self.mongo_url = mongo_url
        self.port = mongo_port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_port=crawler.settings.get('MONGO_PORT')
        )

    def open_spider(self, spider):
        """
        开启mongodb
        :param spider:
        :return:
        """
        self.conn = pymongo.MongoClient(host=self.mongo_url, port=self.port)
        self.db = self.conn[self.mongo_db]

    def process_item(self, item, spider):
        """

        :param item:
        :param spider:
        :return:
        """
        self.db[item.collection].insert_one(dict(item))
        return item

    def close_spider(self, spider):
        """
        关闭mongo
        :param spider:
        :return:
        """
        self.conn.close()