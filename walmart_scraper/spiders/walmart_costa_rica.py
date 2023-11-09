import scrapy

class WalmartCostaRicaSpider(scrapy.Spider):
    name = 'walmart_costa_rica'

    slug_list = [
        'leche-dos-pinos-semidescremada-1000ml-2/p',
        'pan-sandwich-bimbo-grande-720gr/p',
        'arroz-tio-pelon-entero-99-1800gr/p',
        'huevo-gallina-marca-don-cristobal-marron-30-unidades-kilo/p',
        'queso-monteverde-cheddar-300gr/p',
        'manzana-roja-empacada-1-5kg-10-a-13-unidades-por-kg-aproximadamente-4/p',
        'banano-seleccion-especial-kilo-2/p',
        'naranja-importada-1-5-kilo-4/p',
        'tomate-empacado-malla-1-5-kg-a-aproximadamente-4/p',
        'papa-empacado-malla-2kg-10-a-13-unidades-aproximadamente-4/p',
        'cebolla-mini-malla-en-red-1kg-14-a-15-unidades-aproximadamente-4/p',
        'lechuga-romana-unidad-5/p',
        'cristal-agua-tapa-plana-1-75l-4/p',
        'pechuga-entera-pollo-kg/p',
        'molida-hacienda-magra-res-magra-95-grasa-5-1kg-2-2/p'
    ]
    
    custom_settings = {
        'FEEDS': {
            'data/%(name)s_%(time)s.json': {
                'format': 'json',
                'fields': ['name', 'price'],
            },
        },
    }

    def start_requests(self):
        base_url = 'https://www.walmart.co.cr/'
        for slug in self.slug_list:
            url = base_url + slug
            yield scrapy.Request(url, self.parse_product)

    def parse_product(self, response):
        name = response.css('.vtex-store-components-3-x-productBrand--quickview::text').get()
        price = response.css('.vtex-flex-layout-0-x-flexRowContent--price-msi .vtex-store-components-3-x-price_sellingPrice--summary span::text').get()

        yield {
            'name': name,
            'price': price,
        }