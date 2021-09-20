from typing import Optional
from sqlmodel import SQLModel, Field


class EstatusLegislativo(SQLModel, table=True):
    estatus_legislativo_id: Optional[str] = Field(
        default=None, primary_key=True
    )
    estatus_legislativo_codigo: str
    estatus_legislativo_nombre: Optional[str]
