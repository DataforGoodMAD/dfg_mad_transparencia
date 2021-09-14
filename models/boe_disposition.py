from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, date


class BoeDisposition(SQLModel):
    boe_disposicion_id: str = Field(default=None, primary_key=True)
    fecha_actualizacion: datetime
    identificador: str
    titulo: str
    diario_numero: Optional[int]
    numero_oficial: Optional[str]
    fecha_disposicion: date
    fecha_publicacion: date
    fecha_vigencia: Optional[date]
    fecha_derogacion: Optional[date]
    letra_imagen: Optional[str]
    pagina_inicial: int
    pagina_final: int
    suplemento_letra_imagen: Optional[str]
    suplemento_pagina_final: Optional[int]
    suplemento_pagina_inicial: Optional[int]
    judicialmente_anulada: bool
    vigencia_agotada: bool
    estatus_derogacion: bool
    url_epub: Optional[str]
    url_pdf: Optional[str]
    url_pdf_catalan: Optional[str]
    url_pdf_euskera: Optional[str]
    url_pdf_gallego: Optional[str]
    url_pdf_valenciano: Optional[str]
    analisis_notas: Optional[str]
    analisis_materias: Optional[str]
    analisis_alertas: Optional[str]
    referencias_anteriores: Optional[str]
    referencias_posteriores: Optional[str]
    texto: Optional[list[str]]
    imagenes: Optional[str]

    # diario_id: Optional[str] = Field(
    #     default=None, foreign_key="diario.diario_id"
    # )
    # seccion_id: str = Field(default=None, foreign_key="seccion.seccion_id")
    # subseccion_id: Optional[str] = Field(
    #     default=None, foreign_key="subseccion.subseccion_id"
    # )
    departamento_id: str = Field(
        default=None, foreign_key="departamento.departamento_id"
    )
    # rango_id: Optional[str] = Field(default=None, foreign_key="rango.rango_id")
    # estatus_legislativo_id: str = Field(
    #     default=None, foreign_key="estatus_legislativo.estatus_legislativo_id"
    # )
    # origen_legislativo_id: Optional[str] = Field(
    #     default=None, foreign_key="origen_legislativo.origen_legislativo_id"
    # )
    # estado_consolidacion_id: Optional[str] = Field(
    #     default=None,
    #     foreign_key="estado_consolidacion.estado_consolidacion_id",
    # )
