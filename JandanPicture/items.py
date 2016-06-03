# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class JandanpictureItem(Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass

class CommentItem(Item):
	page = Field()
	comment_id = Field()
	ooxx_id = Field()
	author = Field()
	picture_urls = Field()
	oo = Field()
	xx = Field()