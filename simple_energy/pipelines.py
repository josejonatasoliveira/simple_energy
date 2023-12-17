# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

class SimpleEnergyPipeline:
    
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_data(
            file_name TEXT,
            file_extension TEXT,
            file_uri TEXT,
            file_content TEXT,
            file_path TEXT
        )""")
        
    def process_item(self, item, spider):
        
        self.cursor.execute("""
            INSERT INTO file_data (file_name, file_extension, file_uri, file_content, file_path) VALUES (?, ?, ?, ?, ?)
        """,
        (
            item["file_name"],
            item["file_extension"],
            item["file_uri"],
            item["file_content"],
            item["file_path"]
        ))

        self.connection.commit()
        
        return item
