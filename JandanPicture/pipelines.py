# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import re
import os
import urllib2

class JandanpicturePipeline(object):
	def __init__(self):
		self.file = codecs.open('data.dat', mode='a', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line.decode('unicode_escape'))

		ooover = 100
		xxbelow = 50

		page_id = re.findall(r'(\d+)', item['page'])[0]
		comment_id = '-'
		if len(item['comment_id']):
			comment_id = re.findall(r'(\d+)', item['comment_id'][0])[0]
		ooxx_id = '-'
		if len(item['ooxx_id']):
			ooxx_id = re.findall(r'(\d+)', item['ooxx_id'][0])[0]
		oo = '-'
		if len(item['oo']):
			oo = item['oo'][0]
		xx = '-'
		if len(item['xx']):
			xx = item['xx'][0]
		num = 0

		if oo != '-' and xx != '-' and int(oo) >= ooover and int(xx) < xxbelow:
			for picture_url in item['picture_urls']:
				url_name = picture_url.split('/')[-1]
				picture_path = 'ooxx\\'
				picture_name = page_id + '_' + comment_id + '_' + ooxx_id + '_' + oo + '_' + xx + '_' + str(num) + '_' + url_name
				picture = urllib2.urlopen(picture_url)
				image = open(picture_path + picture_name, 'wb')
				image.write(picture.read()) 
				image.close()
				num = num + 1

		return item