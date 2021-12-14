# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WebCrawlingPipeline:
    def process_item(self, item, spider):
        return item


import mysql.connector as mysql


class MySQLStorePipeline(object):

    # init method to initialize the database and
    # create connection and tables
    def __init__(self):
        # Creating connection to database
        self.create_connection()

        # calling method to create table
        self.create_table()

    # create connection method to create database
    # or use database to store scraped data
    def create_connection(self):
        # connecting to database.
        self.connection = mysql.connect(host="localhost", user="root", password="Welcome@123",
                                        database="shopclues")

        # collecting reference to cursor of connection
        self.cursor = self.connection.cursor()

    # Create table method using SQL commands to create table
    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS Mobiles""")
        self.cursor.execute("""create table Mobiles(title text ,price text ,image text, discount text)""")

    # store items to databases.
    def process_item(self, item, spider):
        self.put_items_in_table(item)
        return item

    def put_items_in_table(self, item):
        # extracting item and adding to table using SQL commands.
        self.cursor.execute("""insert into Mobiles values (%s,%s,%s,%s)""", (item['title'],item['price'],item['image'],item['discount']))
        self.connection.commit()
