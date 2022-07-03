# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import pymysql
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter


class MongoPipeline:

    def __init__(self, mongo_uri, mongo_db, mongo_port):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_port = mongo_port

    @classmethod
    def from_crawler(cls, crawler):
        """
        当前方法主要是获取setting配置作用
        :param crawler:
        :return:
        """
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_port=crawler.settings.get('MONGO_PORT'),

        )

    def open_spider(self, spider):
        """
        建立mongo连接
        :param spider:
        :return:
        """
        self.client = pymongo.MongoClient(host=self.mongo_uri, port=self.mongo_port)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        """
        插入mongo
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
        self.client.close()


class MySqlPipeline:

    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        """
        当前方法主要是获取setting配置作用
        :param crawler:
        :return:
        """
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),

        )

    def open_spider(self, spider):
        """
        建立mongo连接
        :param spider:
        :return:
        """
        self.db = pymysql.connect(host=self.host, db=self.database, user=self.user, password=self.password, port=self.port)
        self.cursor =  self.db.cursor()

    def process_item(self, item, spider):
        """
        插入mongo
        :param item:
        :param spider:
        :return:
        """
        data = dict(item)
        keys = ", ".join(data.keys())
        values = ", ".join((['%s']) * len(data))
        sql = "insert into {table} ({key}) values({values})".format(table=item.table, key=keys, values=values)

        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item

    def close_spider(self, spider):
        """
        关闭mongo
        :param spider:
        :return:
        """
        self.db.close()


class ImagePipelines(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        yield Request(url=item['qhimg_url'])