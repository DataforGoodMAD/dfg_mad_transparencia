from typing import Optional
from sqlmodel import SQLModel, Field


class EstadoConsolidacion(SQLModel, table=True):
    estado_consolidacion_id: Optional[str] = Field(
        default=None, primary_key=True
    )
    estado_consolidacion_codigo: str
    estado_consolidacion_nombre: Optional[str]
