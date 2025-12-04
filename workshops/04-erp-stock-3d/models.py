from sqlmodel import SQLModel, Field, Column
from geoalchemy2 import Geometry

class Produit(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    reference: str = Field(unique=True)
    nom: str
    stock: int = Field(default=0)
    seuil_alerte: int = Field(default=10)
    prix: float

class Emplacement(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    code: str  # A01-01-01
    produit_id: int = Field(foreign_key="produit.id", nullable=True)
    quantite: int = Field(default=0)
    geom: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))