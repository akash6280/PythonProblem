# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WebCrawlingPipeline:
    def process_item(self, item, spider):
        return item


from mysql.connector import connect, Error
import mysql


class MySQLStorePipeline(object):
    host = 'localhost'
    user = 'newuser'
    password = 'password'
    db = 'payroll_services'

    def __init__(self):
        self.connection = mysql.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("""INSERT INTO payroll_services.Mobile (title) 
                        VALUES (%s)""", (item['title']))
        print("hello")
        print(item)
        self.connection.commit()
        return item
