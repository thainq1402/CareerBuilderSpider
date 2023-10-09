# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CareerbuilderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ##Get field name 
        field_names = adapter.field_names()


        # remove white space in field 'KinhNghiem'
        list_fields = ['KinhNghiem']
        for field in list_fields: 
            value = adapter.get(field) #get content of the field
            adapter[field] = value[0].replace("\r\n","").replace(" ","")
        
        #remove white space in field 'NganhNghe'
        ##ETL NganhNghe
        name_field = 'NganhNghe'
        value = adapter.get(name_field) # get the list NganhNghe
        cleaned_item = [item.strip() for item  in value[0]]
        adapter[name_field]=cleaned_item
        print("==========================================")
          







        return item
