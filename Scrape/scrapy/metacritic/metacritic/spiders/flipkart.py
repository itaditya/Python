from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from metacritic.items import MetacriticItem


class MetacriticSpider(BaseSpider):
    name = "flipkart"  # Name of the spider, to be used when crawling
    # Where the spider is allowed to go
    allowed_domains = ["https://www.amazon.in/"]
    start_urls = [
        "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=pendrive"
    ]

    def parse(self, response):
        # pass  # To be changed later
        hxs = Selector(response)  # The XPath selector
        # sites = hxs.xpath('//li[contains(@class, "Wbt_B2")]')
        # sites = hxs.css('a')
        sites = hxs.css('.s-access-detail-page')
        # sel = Selector(
        #     text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>')
        # print(sel.css('div.shout time').extract())
        items = []
        for (i, site) in enumerate(sites):
            item = MetacriticItem()
            # item['title'] = site.select('a[contains(@class,"_2k0gmP"]').extract()
            # item['title'] = site.select('text()').extract()
            # print("adi2", site.select('span'))
            item['title'] = site.css('::text').extract()
            item['link'] = site.css('::attr(href)').extract()
            # if(item['title'] != ""):
            items.append(item)
            # print(i, "index", item)
        print("adi", len(items))
        return items
