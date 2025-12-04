from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Entreprise(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    secteur: str
    ca_annuel: Optional[float] = None
    employees: Optional[int] = None

class Client(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    prenom: str
    email: str = Field(unique=True, index=True)
    telephone: Optional[str] = None
    entreprise_id: Optional[int] = Field(default=None, foreign_key="entreprise.id")
    statut: str = Field(default="Prospect")  # Prospect / En négociation / Client / Fidèle / Churn
    score_ia: Optional[float] = Field(default=50.0)  # 0–100
    date_creation: datetime = Field(default_factory=datetime.utcnow)

class Interaction(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key="client.id")
    type: str = Field(default="note")  # note, appel, email, réunion
    contenu: str
    date: datetime = Field(default_factory=datetime.utcnow)