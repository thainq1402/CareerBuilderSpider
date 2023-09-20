# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CareerbuilderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass
class JobItem(scrapy.Item):
    TenCV       = scrapy.Field()
    CongTy      = scrapy.Field()
    DiaDiem     = scrapy.Field()
    NgayCapNhat = scrapy.Field()
    NganhNghe   = scrapy.Field()
    HinhThuc    = scrapy.Field()
    Luong       = scrapy.Field()
    KinhNghiem  = scrapy.Field()
    CapBac      = scrapy.Field()
    HanNopCV    = scrapy.Field()
    PhucLoi     = scrapy.Field()
    MoTa        = scrapy.Field()
    YeuCau      = scrapy.Field()
    ThongTinKhac= scrapy.Field()
    LinkCV      = scrapy.Field()


