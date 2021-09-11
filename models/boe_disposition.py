from sqlmodel import SQLModel
from sqlmodel.main import Field
from db.models.departamento import Departamento
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, Date, UnicodeText
from db.database import Base


class BoeDisposition(SQLModel):

    id: int = Field(default=None, primary_key=True)
    fecha_actualizacion : string,
    identificador : string, primary_key=True,
    titulo : string,
    diario : string,
    diario_numero : integer,
    # seccion = Column(Integer, ForeignKey("seccion.id"))
    # subseccion = Column(String, ForeignKey("subseccion.id"), nullable=True)
    departamento_codigo: int = Field(
        foreign_key="departamento.departamento_codigo"
    )
    # rango = Column(Integer, ForeignKey("rango.id"))
    # numero_oficial
    fecha_disposicion : date,
    fecha_publicacion : date,
    fecha_vigencia : date,
    fecha_derogacion = Column(Date)
    # letra_imagen = Column(String, ForeignKey("subseccion.id"))
    pagina_inicial = Column(Integer)
    pagina_final = Column(Integer)
    # suplemento_letra_imagen
    # suplemento_pagina_inicial
    # suplemento_pagina_final
    # estatus_legislativo = Column(Integer, ForeignKey("estatus_legislativo.id"))
    # origen_legislativo = Column(Integer, ForeignKey("origen_legislativo.id"))
    # estado_consolidacion = Column(Integer, ForeignKey("estado_consolidacion.id"))
    # judicialmente_anulada = Column(Boolean)
    judicialmente_anulada = Column(String)
    # vigencia_agotada = Column(Boolean)
    estatus_derogacion = Column(String)
    url_epub = Column(String)
    url_pdf = Column(String)
    url_pdf_catalan = Column(String)
    url_pdf_euskera = Column(String)
    url_pdf_gallego = Column(String)
    url_pdf_valenciano = Column(String)
    analisis_notas = Column(String)
    analisis_materias = Column(String)
    analisis_alertas = Column(String)
    referencias_anteriores = Column(String)
    referencias_posteriores = Column(String)
    texto = Column(UnicodeText)
    texto_plano = Column(UnicodeText)
    images = Column(String)

    departamento = relationship(Departamento)
