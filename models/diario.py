from typing import Optional
from sqlmodel import SQLModel, Field


class Diario(SQLModel, table=True):
    diario_id: Optional[int] = Field(default=None, primary_key=True)
    diario_codigo: str
    diario_nombre: Optional[str]
