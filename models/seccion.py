from typing import Optional
from sqlmodel import SQLModel, Field


class Seccion(SQLModel, table=True):
    seccion_id: Optional[str] = Field(default=None, primary_key=True)
    seccion_codigo: str
    seccion_nombre: Optional[str]
