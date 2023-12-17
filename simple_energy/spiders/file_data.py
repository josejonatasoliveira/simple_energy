import os

import scrapy

from simple_energy.items import SimpleEnergyItem


class FileDataSpider(scrapy.Spider):
    name = "file_data"
    allowed_domains = ["simpleenergy.com.br"]
    start_urls = ["https://simpleenergy.com.br/teste/"]

    def parse(self, response):
       
        token = response.css('input[name="csrf"]::attr(value)').extract_first()
        requests = []
        
        for code in self.crawler.settings["CODES"]:
            
            form_data = {'codigo': code, 'csrf': token}
            
            request = scrapy.FormRequest(
                url=response.url, 
                formdata=form_data,
                callback=self.parse_data,
                dont_filter=True
            )
            
            requests.append(request)
        
        return requests

    def on_file_downloaded(self, response):
        item = response.meta['item']

        item['file_content'] = str(response.body)
        item['file_path'] = response.url.split("/")[-1]

        yield item

    def parse_data(self, response):
        """ This function parse a properties file on the page

        @url https://simpleenergy.com.br/teste/
        @returns items 1
        @scrapes file_name file_uri
        """
        uris = response.xpath('//a[@download]/@href').extract()
        
        for link in uris:
            item = SimpleEnergyItem()
            item['file_uri'] = link
            
            file_name, file_extension = os.path.splitext(os.path.basename(link))
            item['file_name'] = file_name
            item['file_extension'] = file_extension
            
            request = scrapy.Request(url=response.urljoin(link), callback=self.on_file_downloaded)
            request.meta['item'] = item
            yield request