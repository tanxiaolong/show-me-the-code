#coding=utf8

import redis
import random

class Coupon:
	options = 'abcdefghijklmnopqrstuvwxyz'
        options += options.upper()
        options += "1234567890"

        def __init__(self):
                pass
        def gen(self,bits,count):
                rlt = [] 
                for i in range(count):
                        item = ''
                        for j in range(bits):
                                item += random.choice(self.options)
                        rlt.append(item)
                return rlt	

class Db():
	instance = None
	host = ""
	port = ""
	pwd = ""
	db = ""
	def __init__(self,*args, **kwargs):
		self.host = args[0]
		self.port = args[1]
		self.pwd = args[2]
		self.db = args[3]
		if self.instance is None:
			pool = redis.ConnectionPool(host=self.host, port=self.port,password=self.pwd,db=self.db)
			self.instance = redis.Redis(connection_pool=pool)

	def getInstance(self):
		if self.instance is not None:
			return self.instance
		else:
			pool = redis.ConnectionPool(host=self.host, port=self.port,password=self.pwd,db=self.db)
			self.instance = redis.Redis(connection_pool=pool)
		return self.instance

	def hashSet(self, key, cpcode, used=False):
		isSuc = self.instance.hset(key,cpcode,used)
		if isSuc == 1:
			return isSuc
		return -1

if __name__ == "__main__":
	host = "localhost"
	port = "14490"
	pwd = "hdnb@2017"
	db = "0"
	dbObj = Db(host,port,pwd,db)
	coupon = Coupon()
        cps = coupon.gen(10,200)
        succ = 0
        for cp in cps:
                rlt = dbObj.hashSet("tanxiaolong",cp,False)
                succ += rlt
	print(succ)



