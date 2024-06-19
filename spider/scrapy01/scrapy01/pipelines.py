# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DouBanPipeline:
    def open_spider(self,spider):
        self.file = open('movie2.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        info = f'{item.get("title")},{item.get("star")}\n'
        # with open('movie2.txt','a',encoding='utf-8') as f:
        #     f.write(info)
        self.file.write(info)
        return item
        
    def close_spider(self,spider):
        self.file.close()
