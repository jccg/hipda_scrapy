import scrapy

class DmozSpider(scrapy.Spider):
    name = "hipda"
    allowed_domains = ["hi-pda.com"]
    start_urls = [
        "http://www.hi-pda.com/forum/index.php"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)