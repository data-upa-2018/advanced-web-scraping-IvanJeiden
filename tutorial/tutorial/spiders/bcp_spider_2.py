import scrapy

from bs4 import BeautifulSoup


class BCPSpider(scrapy.Spider):
    name = "bcp2"

    def start_requests(self):
        url='https://www.bcp.gov.py/webapps/web/cotizacion/monedas-mensual'
        for i in range(2001, 2019):
            for j in range(1, 13):
#                print("---------------Estoy en: " + str(i) + "." + str(j))
                yield scrapy.FormRequest(url=url,
                                         method='POST',
                                         formdata={'anho': str(i), 'mes': str(j)},
                                         callback=self.parse,
                                         meta={'i': i, 'j': j})
#                print("---------------Anho: " + str(i))
#                print("---------------Mes: " + str(j))

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        counter = 0
        item = {'Anho': response.meta['i'], 'Mes': response.meta['j']}
        if soup.table:
            rows = soup.findAll('td')
            for row in rows:
                counter = counter + 1
                if counter == 2:
                    item['Moneda'] = row.string
                if counter == 3:
                    item['ME / USD'] = row.string
                if counter == 4:
                    item['G / ME'] = row.string
                    yield item
                    counter = 0
