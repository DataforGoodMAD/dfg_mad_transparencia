from sqlmodel import SQLModel, Field

# from sqlalchemy import Column, ForeignKey, String, Integer
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.sqltypes import Boolean, Date, UnicodeText
# from db.database import Base


class Departamento(SQLModel, table=True):
    departamento_id: int = Field(default=None, primary_key=True)
    departamento_codigo: int
    departamento_nombre: str
