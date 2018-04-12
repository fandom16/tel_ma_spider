import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/tag/humor/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.xpath('span/small/text()').extract_first(),
#             }

#         next_page = response.css('li.next a::attr("href")').extract_first()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)

class TelecontactLocationSpider(scrapy.Spider):
    name = "pharmacie's locations"
    #cities = ('casablanca','tit mellil','bouskoura','ain harrouda','mohammedia','mediouna')
    start_urls = [
    'http://www.telecontact.ma/trouver/index.php?nxo=moteur&nxs=process&string=pharmacie&ou=tit+mellil&aproximite=&produit=', 
    'http://www.telecontact.ma/trouver/index.php?nxo=moteur&nxs=process&string=pharmacie&ou=bouskoura&aproximite=&produit=', 
    'http://www.telecontact.ma/trouver/index.php?nxo=moteur&nxs=process&string=pharmacie&ou=ain+harrouda&aproximite=&produit=', 
    'http://www.telecontact.ma/trouver/index.php?nxo=moteur&nxs=process&string=pharmacie&ou=mohammedia&aproximite=&produit=', 
    'http://www.telecontact.ma/trouver/index.php?nxo=moteur&nxs=process&string=pharmacie&ou=mediouna&aproximite=&produit=',
    'http://www.telecontact.ma/trouver/index.php?nxo=moteur&nxs=process&string=pharmacie&ou=casablanca&aproximite=&produit=', 
]
    base_url = "http://www.telecontact.ma"

    def parse(self, response):
        yield {
            'script' : response.xpath('//*[@id="content_right_bloc"]/script[2]/text()').extract(),
            'ville' : response.xpath("//b/text()")[3].extract()
        }
        #//*[@id="content_right_bloc"]/script[2]
        #//*[@id="engine-results"]/div/div/div[1]/ul

        next_page = response.xpath("//*[@id='engine-results']/div/div/div[1]/ul/li/a[contains(., 'Suivant')]/@href").extract()
        if next_page is not None:
            try:
                yield response.follow(self.base_url + next_page[0].replace(" ", "+"), self.parse)    
            except Exception as e:
                pass
            