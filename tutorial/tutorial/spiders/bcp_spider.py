import scrapy

from bs4 import BeautifulSoup


class PescadoresSpider(scrapy.Spider):
    name = 'bcp'

    def start_requests(self):
        url='https://www.bcp.gov.py/webapps/web/cotizacion/monedas-mensual'
        for i in range(2001, 2002): #2019
            for j in range(1, 2): #13
                print("---------------Estoy en: " + str(i) + "." + str(j))
                yield scrapy.FormRequest(url=url,
                                         method='POST',
                                         formdata={'anho': str(i), 'mes': str(j)},
                                         callback=self.parse)
                print("---------------Anho: " + str(i))
                print("---------------Mes: " + str(j))

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
#        rows = soup.find_all('td')
        for row in soup.find_all('td'):
#        for row in rows:
            moneda = ''
            moneda = moneda + ',' + row.string
            print(moneda)
#        print(row.text)
