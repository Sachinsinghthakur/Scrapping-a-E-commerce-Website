# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter

import pymongo

class LeclercproductsPipeline:

#our class method from_crawler will get our mongodb cluster url to connect with our mongo db cluster from settings.py
#       and pass it __init__ method to connect with cluster and database as we should not expose our credentials in any functions


    def __init__(self,mongo_cluster_url):

            self.conn = pymongo.MongoClient(mongo_cluster_url)

            self.db=self.conn["SachinThakur"]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_cluster_url=crawler.settings.get('MONGO_CLUSTER_URL')
        )


    def process_item(self, item, spider):

#taking the collection name item belongs and delete it as we don't need to store this information along with all other product fields
        collection_name = item["collection"]

        self.collection = self.db[collection_name]

        del item["collection"]

        self.collection.insert(dict(item))
        
        return item