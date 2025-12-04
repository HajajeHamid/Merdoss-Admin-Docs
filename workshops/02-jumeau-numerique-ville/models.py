from sqlmodel import SQLModel, Field, Column
from geoalchemy2 import Geometry
from typing import Optional

class Batiment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: Optional[str] = None
    hauteur: float = Field(default=10.0)
    usage: Optional[str] = None
    geom: str = Field(sa_column=Column(Geometry("POLYGON", srid=4326)))

class Route(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: Optional[str] = None
    type: str
    geom: str = Field(sa_column=Column(Geometry("LINESTRING", srid=4326)))

class VehiculeTracking(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    vehicule_id: str
    vitesse: float
    direction: float
    geom: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))
    timestamp: str = Field(default_factory=lambda: "2025-01-01T12:00:00Z")