import scrapy

class ShopcluesItem(scrapy.Item):
    
	name=scrapy.Field()
	price=scrapy.Field()
	discount=scrapy.Field()
	pass

class myspider(scrapy.Spider):
	name="shopclues_spider"
	def start_requests(self):
		urls=[
				"https://www.shopclues.com/mobiles-smartphones.html?facet_brand[]=Samsung&fsrc=facet_brand&bs=2"
				]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)
		
			
	def parse(self, response):
		items=ShopcluesItem()
		
		name = response.css('span.prod_name::text').extract()
		price = response.css('span.p_price::text').extract()
		discount = response.css('span.prd_discount::text').extract()
		
		items['name']=name
		items['price']=price
		items['discount']=discount
		
		yield items
	