import scrapy
import json

class PescadoresSpider(scrapy.Spider):
    name = 'pescadores'
    def start_requests(self):
        url='http://www.sas.gov.py/tmpl/grillas/ProgPescadores.php'
        for i in range(206):
            print("---------------Estoy en iteracion: " + str(i))
            yield scrapy.FormRequest(url=url,
                                     method='POST',
                                     formdata={'rows': '17', 'page': str(i + 1)},
                                     callback=self.parse)

    def parse(self, response):
        rows =json.loads(response.body)['rows']
        for row in rows:
            yield {
                'Numero': row['cell'][0],
                'C.I.': row['cell'][1],
                'Nombre': row['cell'][3],
                'Departamento': row['cell'][4],
                'Asociacion': row['cell'][5],
                'Subsidio': row['cell'][6]
            }