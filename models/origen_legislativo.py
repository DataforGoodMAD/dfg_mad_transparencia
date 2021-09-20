from typing import Optional
from sqlmodel import SQLModel, Field


class OrigenLegislativo(SQLModel, table=True):
    origen_legislativo_id: Optional[str] = Field(
        default=None, primary_key=True
    )
    origen_legislativo_codigo: str
    origen_legislativo_nombre: Optional[str]
