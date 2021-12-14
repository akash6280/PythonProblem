import scrapy

from web_crawling.items import MobileItem


class ShopcluesSpider(scrapy.Spider):
    # name of spider
    name = 'shopclues'

    # list of allowed domains
    allowed_domains = ['www.shopclues.com']
    # starting url
    start_urls = ['https://www.shopclues.com/mobiles-smartphones.html?facet_brand[]=Redmi&fsrc=facet_brand']

    def parse(self, response):
        # creating items dictionary
        items = MobileItem()
        # Extract product information
        titles = response.css('img::attr(title)').extract()
        images = response.css('img::attr(data-img)').extract()
        prices = response.css('.p_price::text').extract()
        discounts = response.css('.prd_discount::text').extract()

        for items in zip(titles, prices, images, discounts):
            item = MobileItem(
                title=items[0],
                price=items[1].strip(),
                image=items[2],
                discount=items[3]
            )
            yield item
