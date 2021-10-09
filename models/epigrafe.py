from typing import Optional
from sqlmodel import SQLModel, Field


class Epigrafe(SQLModel, table=True):
    epigrafe_id: Optional[str] = Field(default=None, primary_key=True)
    epigrafe_codigo: str
    epigrafe_nombre: Optional[str]
