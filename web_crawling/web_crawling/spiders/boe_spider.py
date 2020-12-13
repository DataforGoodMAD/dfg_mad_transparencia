import scrapy
import json
import os
from w3lib.html import remove_tags


class BoeSpider(scrapy.Spider):
    name = "boe_spider"
    # start_urls = [
    #     f"https://boe.es/boe/dias/2020/11/{day}/"
    #     for day in [
    #         "03",
    #         "04",
    #         "05",
    #         "06",
    #         "07",
    #         "09",
    #         "10",
    #         "11",
    #         "12",
    #         "13",
    #         "14",
    #         "15",
    #         "16",
    #         "17",
    #         "18",
    #         "19",
    #         "20",
    #         "21",
    #         "22",
    #         "23",
    #         "24",
    #         "25",
    #         "26",
    #         "27",
    #         "28",
    #         "29",
    #         "30",
    #     ]
    # ]
    start_urls = ["https://boe.es/diario_boe/ultimo.php"]

    def parse(self, response):
        for dispo in response.css(".puntoHTML > a::attr('href')").extract():
            url = response.urljoin(dispo).replace("/txt.php", "/xml.php")
            yield scrapy.Request(url, callback=self.save_xml_dispo)

    def save_xml_dispo(self, response):
        tags = {
            "documento": response.xpath("//documento/text()").get(),
            "metadatos": response.xpath("//metadatos/text()").get(),
            "identificador": response.xpath("//identificador/text()").get(),
            "titulo": response.xpath("//titulo/text()").get(),
            "diario": response.xpath("//diario/@codigo").get()
            or response.xpath("//diario/text()").get(),
            "diario_numero": response.xpath("//diario_numero/text()").get(),
            "seccion": response.xpath("//seccion/text()").get(),
            "subseccion": response.xpath("//subseccion/text()").get(),
            "departamento": response.xpath("//departamento/text()").get(),
            "rango": response.xpath("//rango/text()").get(),
            "numero_oficial": response.xpath("//numero_oficial/text()").get(),
            "fecha_disposicion": response.xpath("//fecha_disposicion/text()").get(),
            "fecha_publicacion": response.xpath("//fecha_publicacion/text()").get(),
            "fecha_vigencia": response.xpath("//fecha_vigencia/text()").get(),
            "fecha_derogacion": response.xpath("//fecha_derogacion/text()").get(),
            "letra_imagen": response.xpath("//letra_imagen/text()").get(),
            "pagina_inicial": response.xpath("//pagina_inicial/text()").get(),
            "pagina_final": response.xpath("//pagina_final/text()").get(),
            "suplemento_letra_imagen": response.xpath(
                "//suplemento_letra_imagen/text()"
            ).get(),
            "suplemento_pagina_inicial": response.xpath(
                "//suplemento_pagina_inicial/text()"
            ).get(),
            "suplemento_pagina_final": response.xpath(
                "//suplemento_pagina_final/text()"
            ).get(),
            "estatus_legislativo": response.xpath("//estatus_legislativo/text()").get(),
            "origen_legislativo": response.xpath("//origen_legislativo/text()").get(),
            "estado_consolidacion": response.xpath(
                "//estado_consolidacion/text()"
            ).get(),
            "judicialmente_anulada": response.xpath(
                "//judicialmente_anulada/text()"
            ).get(),
            "vigencia_agotada": response.xpath("//vigencia_agotada/text()").get(),
            "estatus_derogacion": response.xpath("//estatus_derogacion/text()").get(),
            "url_epub": response.xpath("//url_epub/text()").get(),
            "url_pdf": response.xpath("//url_pdf/text()").get(),
            "url_pdf_catalan": response.xpath("//url_pdf_catalan/text()").get(),
            "url_pdf_euskera": response.xpath("//url_pdf_euskera/text()").get(),
            "url_pdf_gallego": response.xpath("//url_pdf_gallego/text()").get(),
            "url_pdf_valenciano": response.xpath("//url_pdf_valenciano/text()").get(),
            "analisis_notas": response.xpath("//analisis/notas/text()").get(),
            "analisis_materias": response.xpath("//analisis/materias/text()").get(),
            "analisis_alertas": response.xpath("//analisis/alertas/text()").get(),
            "referencias_anteriores": response.xpath(
                "//referencias/anteriores/text()"
            ).get(),
            "referencias_posteriores": response.xpath(
                "//referencias/posteriores/text()"
            ).get(),
            "texto": response.xpath("//texto").getall(),
            "images": response.xpath("//img/@src").getall(),
        }
        # Add text with HTML tags removed
        plain_text = [remove_tags(text, encoding="latin1") for text in tags["texto"]]
        tags["texto_plano"] = plain_text
        # Save to JSON file
        path = f"../data/{tags['fecha_publicacion']}/{tags['seccion']}/{tags['subseccion']}/{tags['departamento']}"
        filename = f"{tags['identificador']}.json"
        os.makedirs(path, exist_ok=True)
        with open(f"{path}/{filename}", "w") as file:
            json.dump(tags, file)
