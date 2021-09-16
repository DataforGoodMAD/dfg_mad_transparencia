from typing import Optional
from sqlmodel import SQLModel, Field


class Departamento(SQLModel, table=True):
    departamento_id: Optional[int] = Field(default=None, primary_key=True)
    departamento_codigo: str
    departamento_nombre: Optional[str]
