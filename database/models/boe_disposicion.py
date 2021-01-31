from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, Date, UnicodeText
from database.database import Base


class BoeBase(Base):

    __tablename__ = "boe_disposicion"

    identificador = Column(String(50), primary_key=True)
    titulo = Column(String(500))
    diario = Column(String(500))
    diario_numero = Column(Integer)
    seccion = Column(Integer, ForeignKey("seccion.id"))
    subseccion = Column(String(10), ForeignKey("subseccion.id"))
    departamento = Column(Integer, ForeignKey("departamento.id"))
    rango = Column(Integer, ForeignKey("rango.id"))
    # numero_oficial
    fecha_disposicion = Column(Date)
    fecha_publicacion = Column(Date)
    fecha_vigencia = Column(Date)
    fecha_derogacion = Column(Date)
    letra_imagen = Column(String(10), ForeignKey("subseccion.id"))
    pagina_inicial = Column(Integer)
    pagina_final = Column(Integer)
    # suplemento_letra_imagen
    # suplemento_pagina_inicial
    # suplemento_pagina_final
    estatus_legislativo = Column(Integer, ForeignKey("estatus_legislativo.id"))
    origen_legislativo = Column(Integer, ForeignKey("origen_legislativo.id"))
    estado_consolidacion = Column(Integer, ForeignKey("estado_consolidacion.id"))
    judicialmente_anulada = Column(Boolean)
    vigencia_agotada = Column(Boolean)
    estatus_derogacion = Column(String(100))
    url_epub = Column(String(500))
    url_pdf = Column(String(500))
    url_pdf_catalan = Column(String(500))
    url_pdf_euskera = Column(String(500))
    url_pdf_gallego = Column(String(500))
    url_pdf_valenciano = Column(String(500))
    analisis_notas = Column(String(500))
    analisis_materias = Column(String(500))
    analisis_alertas = Column(String(500))
    referencias_anteriores = Column(String(500))
    referencias_posteriores = Column(String(500))
    texto = Column(UnicodeText())
    images = Column(String(500))
