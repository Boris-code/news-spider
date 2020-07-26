# -*- coding: utf-8 -*-
"""
Created on 2020-07-26 21:17:41
---------
@summary:
---------
@author: Boris
"""

import spider
from spider.network.item import Item
from spider.utils.log import log

from extractor.article_extractor import ArticleExtractor


class NewsSpider(spider.SingleSpider):
    def start_requests(self, *args, **kws):
        # 下发列表任务
        yield spider.Request("http://column.caijing.com.cn/")

    def parser(self, request, response):
        # 解析列表
        article_list_url = response.xpath('//div[@class="kjxw_tit"]/a/@href').extract()
        for url in article_list_url:
            log.debug("下发文章任务 url = {}".format(url))
            yield spider.Request(url, callback=self.parser_artile)

    def parser_artile(self, request, response):
        log.debug("解析文章 url = {}".format(request.url))
        article_extractor = ArticleExtractor(request.url, response.text)

        item = Item()
        item.url = request.url
        item.content = article_extractor.get_content()
        item.title = article_extractor.get_title()
        item.release_time = article_extractor.get_release_time()
        item.author = article_extractor.get_author()

        log.debug(item)


if __name__ == "__main__":
    NewsSpider(parser_count=50).start()  # parser_count 为线程数
