# -*- coding: utf-8 -*-
#
# Copyright © 2016 Haipz <haipz@gmail.com | @haipz.com>
#
# Distributed under terms of the MIT license.

import sys
reload(sys)
import os

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from JandanPicture.items import CommentItem

class JandanPictureSpider(CrawlSpider):
	start_page = int(input("start page: "))

	name = 'JandanPicture'
	allowed_domains = ['jandan.net']
	start_urls = [
		'http://jandan.net/ooxx/page-' + str(start_page),
	]

	rules = [
		Rule(LinkExtractor(restrict_xpaths='//a[@class="previous-comment-page"]'),  callback='parse_item', follow=True),
	]

	def parse_item(self, response):
		for comment in response.xpath('//li[starts-with(@id, "comment-")]'):
			item = CommentItem()

			item['page'] = response.url
			item['picture_urls'] = comment.xpath('.//a[@class="view_img_link"]/@href').extract()
			item['comment_id'] = comment.xpath('./@id').extract()
			item['ooxx_id'] = comment.xpath('.//span[@class="righttext"]/a/text()').extract()
			item['author'] = comment.xpath('.//div[@class="author"]/strong/text()').extract()
			item['oo'] = comment.xpath('.//span[starts-with(@id, "cos_support-")]/text()').extract()
			item['xx'] = comment.xpath('.//span[starts-with(@id, "cos_unsupport-")]/text()').extract()

			yield item