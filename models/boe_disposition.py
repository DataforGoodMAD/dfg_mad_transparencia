from sqlmodel import SQLModel
from sqlmodel.main import Field
from db.models.departamento import Departamento
from datetime import datetime, date
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import bool, Date, UnicodeText
from db.database import Base


class BoeDisposition(SQLModel):
    boe_disposicion_id: str = Field(default=None, primary_key=True)
    fecha_actualizacion: datetime
    identificador: str
    titulo: str
    diario_numero: int
    numero_oficial: int
    fecha_disposicion: date
    fecha_publicacion: date
    fecha_vigencia: date
    fecha_derogacion: date
    letra_imagen: str
    pagina_inicial: int
    pagina_final: int
    suplemento_letra_imagen: str
    suplemento_pagina_final: int
    suplemento_pagina_inicial: int
    judicialmente_anulada: bool
    vigencia_agotada: bool
    estatus_derogacion: bool
    url_epub: str
    url_pdf: str
    url_pdf_catalan: str
    url_pdf_euskera: str
    url_pdf_gallego: str
    url_pdf_valenciano: str
    texto: str
    imagenes: str
    diario_id: str = Field(default=None, foreign_key="diario.diario_id")
    seccion_id: str = Field(default=None, foreign_key="seccion.seccion_id")
    subseccion_id: str = Field(
        default=None, foreign_key="subseccion.subseccion_id"
    )
    departamento_id: str = Field(
        default=None, foreign_key="departamento.departamento_id"
    )
    rango_id: str = Field(default=None, foreign_key="rango.rango_id")
    estatus_legislativo_id: str = Field(
        default=None, foreign_key="estatus_legislativo.estatus_legislativo_id"
    )
    origen_legislativo_id: str = Field(
        default=None, foreign_key="origen_legislativo.origen_legislativo_id"
    )
    estado_consolidacion: str = Field(
        default=None,
        foreign_key="estado_consolidacion.estado_consolidacion_id",
    )
