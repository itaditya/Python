# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["google.com"]
    start_urls = ['http://google.com/']

    def parse(self, response):
        pass
