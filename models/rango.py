from typing import Optional
from sqlmodel import SQLModel, Field


class Rango(SQLModel, table=True):
    rango_id: Optional[int] = Field(default=None, primary_key=True)
    rango_codigo: str
    rango_nombre: Optional[str]
