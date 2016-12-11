import scrapy
import json
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from metacritic.items import MetacriticItem
from scrapy.http import Request
# https://accounts.google.com/signin/challenge/sl/password

BASE_URL = 'https://accounts.google.com'
USER_NAME = 'adityaa803@gmail.com'
PASSWORD = '19971202606'
PAGES = ['page1.aspx', 'page2.aspx', 'page3.aspx', 'page4.aspx']


class ShareSpider(BaseSpider):
    name = "gmail"
    start_urls = [BASE_URL + '/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form[@id="gaia_loginform"]',
            formdata={
                'Email': USER_NAME
            },
            callback=self.after_login)

    def after_login(self, response):
        hxs = Selector(response)
        print("email", hxs.css('#email-display::text').extract())
        base_url = BASE_URL + '/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#password'
        # print("adi", response)
        # yield Request(
        #     url=base_url, callback=self.action)
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form[@id="gaia_loginform"]',
            formdata={
                'Passwd': PASSWORD
            },
            dont_filter=True,
            callback=self.action)
        # for page in PAGES:
        #     yield Request(
        #         url=base_url + page + "?id=1",
        #         callback=self.action)

    def action(self, response):
        hxs = Selector(response)
        # print("title", hxs.css('.aKw::text').extract())
        print("title", hxs.css('.msg::text').extract())
        # print(response.request.meta.get('redirect_urls'))
        # yield scrapy.FormRequest.from_response(
        #     "https://mail.google.com/mail/u/0/?ui=2&ik=586f1c628c&rid=mail%3Ai.b764.0.1&view=cv&th=15857f84c725c385&th=15855d9d62506f7c&th=15855890565cc974&th=15853f949650b87a&th=15853f5695139021&prf=1&_reqid=159458&nsc=1&mb=0&rt=j&search=inbox",
        #     formxpath='//form',
        #     formdata={},
        #     callback=self.naction)
        # "https://mail.google.com/mail/u/0/#inbox"
        yield Request(
            url="https://mail.google.com/mail/u/0/?ui=2&ik=586f1c628c&rid=mail%3Ai.b764.0.1&view=cv&th=15857f84c725c385&th=15855d9d62506f7c&th=15855890565cc974&th=15853f949650b87a&th=15853f5695139021&prf=1&_reqid=159458&nsc=1&mb=0&rt=j&search=inbox",
            callback=self.naction)

    def naction(self, response):
        # hxs = Selector(response)
        # print("a", response.text)
        j = json.dumps(response.text)
        a = json.loads(j)
        print("json", len(a))
        # print("adititle", hxs.css('.msg::text').extract())
