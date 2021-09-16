from scrapy import Request, Spider

from models.departamento import Departamento
from models.diario import Diario
from models.disposicion_boe import DisposicionBOE
from models.estado_consolidacion import EstadoConsolidacion
from models.estatus_legislativo import EstatusLegislativo
from models.origen_legislativo import OrigenLegislativo
from models.rango import Rango
from models.seccion import Seccion
from models.subseccion import Subseccion

# from w3lib.html import remove_tags


class BoeSpider(Spider):
    name = "boe_spider"
    start_urls = ["https://boe.es/diario_boe/ultimo.php"]

    def parse(self, response):
        dispositions_list = response.css(
            ".puntoHTML > a::attr('href')"
        ).extract()
        for disposition in dispositions_list:
            url = response.urljoin(disposition).replace("/txt.php", "/xml.php")
            yield Request(url, callback=self.save_xml_disposition)

    def save_xml_disposition(self, response):
        departamento = Departamento(
            departamento_id=response.xpath("//departamento/@codigo").get(),
            departamento_codigo=response.xpath("//departamento/@codigo").get(),
            departamento_nombre=response.xpath("//departamento/text()").get(),
        )
        yield departamento

        diario = Diario(
            diario_id=response.xpath("//diario/@codigo").get(),
            diario_codigo=response.xpath("//diario/@codigo").get(),
            diario_nombre=response.xpath("//diario/text()").get(),
        )
        yield diario

        estado_consolidacion = EstadoConsolidacion(
            estado_consolidacion_id=response.xpath(
                "//estado_consolidacion/@codigo"
            ).get(),
            estado_consolidacion_codigo=response.xpath(
                "//estado_consolidacion/@codigo"
            ).get(),
            estado_consolidacion_nombre=response.xpath(
                "//estado_consolidacion/text()"
            ).get(),
        )
        yield estado_consolidacion

        estatus_legislativo = EstatusLegislativo(
            estatus_legislativo_id=response.xpath(
                "//estatus_legislativo/text()"
            ).get(),
            estatus_legislativo_codigo=response.xpath(
                "//estatus_legislativo/text()"
            ).get(),
            estatus_legislativo_nombre=response.xpath(
                "//estatus_legislativo/text()"
            ).get(),
        )
        yield estatus_legislativo

        origen_legislativo = OrigenLegislativo(
            origen_legislativo_id=response.xpath(
                "//origen_legislativo/@codigo"
            ).get(),
            origen_legislativo_codigo=response.xpath(
                "//origen_legislativo/@codigo"
            ).get(),
            origen_legislativo_nombre=response.xpath(
                "//origen_legislativo/text()"
            ).get(),
        )
        yield origen_legislativo

        # Rango
        # Seccion
        # Subseccion

        disposicion_boe = DisposicionBOE(
            boe_disposicion_id=response.xpath("//identificador/text()").get(),
            fecha_actualizacion=response.xpath(
                "//documento/@fecha_actualizacion"
            ).get(),
            identificador=response.xpath("//identificador/text()").get(),
            titulo=response.xpath("//titulo/text()").get(),
            diario_numero=response.xpath("//diario_numero/text()").get(),
            numero_oficial=response.xpath("//numero_oficial/text()").get(),
            fecha_disposicion=response.xpath(
                "//fecha_disposicion/text()"
            ).get(),
            fecha_publicacion=response.xpath(
                "//fecha_publicacion/text()"
            ).get(),
            fecha_vigencia=response.xpath("//fecha_vigencia/text()").get(),
            fecha_derogacion=response.xpath("//fecha_derogacion/text()").get(),
            letra_imagen=response.xpath("//letra_imagen/text()").get(),
            pagina_inicial=response.xpath("//pagina_inicial/text()").get(),
            pagina_final=response.xpath("//pagina_final/text()").get(),
            suplemento_letra_imagen=response.xpath(
                "//suplemento_letra_imagen/text()"
            ).get(),
            suplemento_pagina_inicial=response.xpath(
                "//suplemento_pagina_inicial/text()"
            ).get(),
            suplemento_pagina_final=response.xpath(
                "//suplemento_pagina_final/text()"
            ).get(),
            judicialmente_anulada=response.xpath(
                "//judicialmente_anulada/text()"
            ).get(),
            vigencia_agotada=response.xpath("//vigencia_agotada/text()").get(),
            estatus_derogacion=response.xpath(
                "//estatus_derogacion/text()"
            ).get(),
            url_epub=response.xpath("//url_epub/text()").get(),
            url_pdf=response.xpath("//url_pdf/text()").get(),
            url_pdf_catalan=response.xpath("//url_pdf_catalan/text()").get(),
            url_pdf_euskera=response.xpath("//url_pdf_euskera/text()").get(),
            url_pdf_gallego=response.xpath("//url_pdf_gallego/text()").get(),
            url_pdf_valenciano=response.xpath(
                "//url_pdf_valenciano/text()"
            ).get(),
            analisis_notas=response.xpath("//analisis/notas/text()").get(),
            analisis_materias=response.xpath(
                "//analisis/materias/text()"
            ).get(),
            analisis_alertas=response.xpath("//analisis/alertas/text()").get(),
            referencias_anteriores=response.xpath(
                "//referencias/anteriores/text()"
            ).get(),
            referencias_posteriores=response.xpath(
                "//referencias/posteriores/text()"
            ).get(),
            texto=response.xpath("//texto").getall(),
            images=response.xpath("//img/@src").getall(),
            # "diario_id": response.xpath("//diario/@codigo").get()
            # or response.xpath("//diario/text()").get(),
            # "seccion_id": response.xpath("//seccion/text()").get(),
            # "subseccion_id": response.xpath("//subseccion/text()").get(),
            departamento_id=response.xpath("//departamento/@codigo").get(),
            # "rango_id": response.xpath("//rango/@codigo").get(),
            # "estatus_legislativo_id": response.xpath(
            #     "//estatus_legislativo/text()"
            # ).get(),
            # "origen_legislativo_id": response.xpath(
            #     "//origen_legislativo/@codigo"
            # ).get(),
            # "estado_consolidacion_id": response.xpath(
            #     "//estado_consolidacion/@codigo"
            # ).get(),
        )
        yield disposicion_boe
