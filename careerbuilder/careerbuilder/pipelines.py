# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CareerbuilderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ##remove whitespace 
        field_names = adapter.field_names()


        #list fields that need to remove white space
        list_fields = ['KinhNghiem','NganhNghe']
        for field in list_fields: 
            value = adapter.get(field) #get content of the field
            adapter[field] = value[0].replace("\r\n","").replace(" ","")
           

        return item
