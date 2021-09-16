from typing import Optional
from sqlmodel import SQLModel, Field


class Subseccion(SQLModel, table=True):
    subseccion_id: Optional[int] = Field(default=None, primary_key=True)
    subseccion_codigo: str
    subseccion_nombre: Optional[str]
