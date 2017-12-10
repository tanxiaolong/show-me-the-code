#coding=utf8

import random

class Coupon:
	options = 'abcdefghijklmnopqrstuvwxyz'
	options += options.upper()
	options += "1234567890"

	def __init__(self,isN,isA):
		self.isN = isN
		self.isA = isA
	def gen(self,bits,count):
		rlt = []
		for i in range(count):
			item = ''
			for j in range(bits):
				item += random.choice(self.options)
			rlt.append(item)
		return rlt

if __name__ == "__main__":
	# 100 位，要数字，要字母，生成 100 个
	c = Coupon(True,True)
	coupons = c.gen(bits=100,count=100)
	print(coupons)

