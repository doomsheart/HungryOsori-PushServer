import scrapy
from scrapy.crawler import CrawlerProcess
import logging
import datetime

class CSHanyangCrawler(scrapy.Spider):
    name = 'cs.hanyang - crawler'
    start_urls = ['http://cs.hanyang.ac.kr/board/info_board.php']
    base_urls = "http://cs.hanyang.ac.kr/board/info_board.php?ptype=view&idx="
    logging.getLogger('scrapy').propagate = False

    def parse(self, response):
<<<<<<< HEAD
        query_notice_urls = "#content_in > div > table > tr:nth-child(25) > td.left > a::attr(href)"
        query_notice_number = "#content_in > div > table > tr:nth-child(25) > td:nth-child(2)"
=======
      
        query_notice_urls = "#content_in > div > table > tbody > tr > td > a::attr(href)"
        query_notice_number = "#content_in > div > table > tbody > tr > td"

>>>>>>> 9b430f7ed3a87e2c6788fc29761559500cdf07d9
        default_time = int(datetime.datetime.now().timestamp()) * 10

        numbers = [int(text) for text in response.css(query_notice_number).extract() if text.isdigit()]
        urls = response.css(query_notice_urls).extract()


        pairs = zip(numbers, urls)
        for number, pair in pairs:
#            print (number, pair)
            print(str(number) + "&^%987&^%" + pair + "&^%987&^%" + self.base_urls +str(number)+"&subkind=&offset=0")

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(CSHanyangCrawler)
process.start()