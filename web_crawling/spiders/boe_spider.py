from scrapy import Request, Spider
from scrapy.spiders import CrawlSpider

from models.epigrafe import Epigrafe
from models.departamento import Departamento
from models.diario import Diario
from models.disposicion_boe import DisposicionBOE
from models.estado_consolidacion import EstadoConsolidacion
from models.estatus_legislativo import EstatusLegislativo
from models.origen_legislativo import OrigenLegislativo
from models.rango import Rango
from models.seccion import Seccion
from models.subseccion import Subseccion


class BoeSpider(CrawlSpider):
    name = "boe_spider"
    start_urls = ["https://boe.es/diario_boe/ultimo.php"]
    _base_url = "https://boe.es"

    def parse_start_url(self, response):
        link_sumario = response.css(
            "div.linkSumario li.puntoXML a::attr(href)"
        ).get()
        return Request(
            f"{self._base_url}{link_sumario}",
            callback=self.process_epigrafes,
        )

    def _build_items_by_epigrafe(self, epigrafes_xml):
        items_by_epigrafe = []
        for epigrafe_xml in epigrafes_xml:
            items = epigrafe_xml.xpath(".//item")
            for item in items:
                item_url = item.xpath(".//urlXml/text()").get()
                items_by_epigrafe.append(
                    {"url": item_url, "epigrafe": epigrafe_xml}
                )
        return items_by_epigrafe

    def process_epigrafes(self, response):
        epigrafes_xml = response.xpath("//epigrafe")
        items_by_epigrafe = self._build_items_by_epigrafe(epigrafes_xml)
        for item in items_by_epigrafe:
            item_url = item["url"]
            url = f"{self._base_url}{item_url}"
            yield Request(
                url,
                callback=self.save_xml_disposition,
                cb_kwargs=dict(epigrafe_xml=item["epigrafe"]),
            )

    def save_xml_disposition(self, response, epigrafe_xml):

        epigrafe = Epigrafe(
            epigrafe_id=epigrafe_xml.xpath("@nombre").get(),
            epigrafe_codigo=epigrafe_xml.xpath("@nombre").get(),
            epigrafe_nombre=epigrafe_xml.xpath("@nombre").get(),
        )
        yield epigrafe

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

        rango = Rango(
            rango_id=response.xpath("//rango/@codigo").get(),
            rango_codigo=response.xpath("//rango/@codigo").get(),
            rango_nombre=response.xpath("//rango/text()").get(),
        )
        yield rango

        rango = Rango(
            rango_id=response.xpath("//rango/@codigo").get(),
            rango_codigo=response.xpath("//rango/@codigo").get(),
            rango_nombre=response.xpath("//rango/text()").get(),
        )
        yield rango

        seccion = Seccion(
            seccion_id=response.xpath("//seccion/text()").get(),
            seccion_codigo=response.xpath("//seccion/text()").get(),
            seccion_nombre=response.xpath("//seccion/text()").get(),
        )
        yield seccion

        if response.xpath("//subseccion/text()").get():
            subseccion = Subseccion(
                subseccion_id=response.xpath("//subseccion/text()").get(),
                subseccion_codigo=response.xpath("//subseccion/text()").get(),
                subseccion_nombre=response.xpath("//subseccion/text()").get(),
            )
            yield subseccion

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
            texto=str(response.xpath("//texto").getall()),
            images=str(response.xpath("//img/@src").getall()),
            epigrafe_id=epigrafe_xml.xpath("@nombre").get(),
            diario_id=response.xpath("//diario/@codigo").get(),
            seccion_id=response.xpath("//seccion/text()").get(),
            subseccion_id=response.xpath("//subseccion/text()").get(),
            departamento_id=response.xpath("//departamento/@codigo").get(),
            rango_id=response.xpath("//rango/@codigo").get(),
            estatus_legislativo_id=response.xpath(
                "//estatus_legislativo/text()"
            ).get(),
            origen_legislativo_id=response.xpath(
                "//origen_legislativo/@codigo"
            ).get(),
            estado_consolidacion_id=response.xpath(
                "//estado_consolidacion/@codigo"
            ).get(),
        )
        yield disposicion_boe
