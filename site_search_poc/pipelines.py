# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import json
import time
from itemadapter import ItemAdapter


class SiteSearchPocPipeline:
    def open_spider(self, spider):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.file = open(f"items{timestr}.json", "w+")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
