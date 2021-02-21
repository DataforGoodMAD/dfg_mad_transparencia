from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, Date, UnicodeText
from db.database import Base


class Departamento(Base):

    __tablename__ = "departamento"

    departamento_codigo = Column(Integer, primary_key=True)
    departamento_nombre = Column(String)
