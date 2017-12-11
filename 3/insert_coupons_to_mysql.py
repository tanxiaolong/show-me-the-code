#coding=utf8

import MySQLdb as ms
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
	user = ""
	pwd = ""
	db = ""
	def __init__(self,*args, **kwargs):
		self.host = args[0]
		self.user = args[1]
		self.pwd = args[2]
		self.db = args[3]
		if self.instance is None:
			self.instance = ms.connect(args[0],args[1],args[2],args[3])

	def getInstance(self):
		if self.instance is not None:
			return self.instance
		else:
			self.instance = ms.connect(self.host,self.user,self.pwd,self.db)
		return self.instance

	def insertOP(self, sql=""):
		cur = self.instance.cursor()
		rlt = cur.execute(sql)
		if rlt == 1:
			cur.close()
			self.instance.commit()
			#self.instance.close()
			return rlt
		return -1

if __name__ == "__main__":
	host = "localhost"
	user = "root"
	pwd = "letv"
	db = "test"
	dbObj = Db(host,user,pwd,db)
	coupon = Coupon()
        cps = coupon.gen(10,200)
        succ = 0
        for cp in cps:
                sql = "INSERT INTO coupon (cpcode) VALUES (\""+cp+"\")"
                rlt = dbObj.insertOP(sql)
                succ += rlt
	print(succ)

