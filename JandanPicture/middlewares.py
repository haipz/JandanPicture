#coding: utf-8

import random
import base64
import socket
import os
from proxy import *

class RandomUserAgent(object):
	def __init__(self, agents):
		self.agents = agents

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.getlist('USER_AGENTS'))

	def process_request(self, request, spider):
		request.headers.setdefault('User-Agent', random.choice(self.agents))

class ProxyMiddleware(object):
	def __init__(self):
		self.ins = Proxy(2)
		self.proxies = self.ins.get_proxy()
		print '[PROXY] Proxy number: ' + str(len(self.proxies))

	def process_request(self, request, spider):
		proxy = {'ip_port': '', 'user_pass': ''}
		_proxy = random.choice(self.proxies)
		proxy['ip_port'] = _proxy['HTTP']

		if proxy['user_pass'] is not None:
			request.meta['proxy'] = "http://%s" % proxy['ip_port']
			encoded_user_pass = base64.encodestring(proxy['user_pass'])
			request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
		else:
			request.meta['proxy'] = "http://%s" % proxy['ip_port']