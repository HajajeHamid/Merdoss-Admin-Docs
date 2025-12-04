# Workshop 04 – ERP Entrepôt + Stock Visualisé en 3D (Potree + Kanban)

**Tu vas pouvoir dire à ton client : “Voici votre entrepôt entier en 3D, cliquez sur une étagère pour voir le stock”**

### Fonctionnalités livrées
- Gestion complète produits / stocks / emplacements
- Vue Kanban des commandes
- Entrepôt 3D complet avec nuage de points (Potree)
- Clic sur une étagère → détail stock + photo
- Alertes réapprovisionnement IA
- Picking optimisé par chemin le plus court
- Export picking list PDF avec QR codes

Lancement :
```bash
cd workshops/04-erp-stock-3d
pip install "merdoss-admin[all]"
uvicorn main:app --reload
# → /erp-3d
```

Badge obtenu : **ERP Legend 2025**
```

#### 2. `main.py`

```python
from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from merdoss_admin import inject_merdoss
import os

app = FastAPI(title="ERP Stock 3D – Workshop 04")

engine = create_engine("sqlite:///erp_stock.db")
SQLModel.metadata.create_all(engine)

inject_merdoss(
    app=app,
    db_url="sqlite:///erp_stock.db",
    theme="dracula",
    plugins=["core", "kanban", "inventory-3d", "3d", "ai", "export"],
    title="ERP Entrepôt 3D",
    favicon="warehouse",
    enable_3d=True
)

# Import automatique du scan LiDAR de l’entrepôt
if not os.path.exists("data/imported.flag"):
    os.system("merdoss 3d pointcloud data/entrepot_scan.laz")
    open("data/imported.flag", "w").write("done")
```

#### 3. `models.py`

```python
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
```

#### 4. `pages/erp_3d.py`

```python
from merdoss_admin.ui import Page

@Page("/erp-3d", title="Entrepôt 3D Interactif")
def erp_3d():
    return """
    <div class="h-screen w-screen relative">
      <iframe src="/3d/potree" class="absolute inset-0 w-full h-full"></iframe>
      <div class="absolute top-4 left-4 bg-black bg-opacity-90 text-white p-8 rounded-xl">
        <h1 class="text-4xl font-bold text-purple-400 mb-4">Entrepôt 3D – ERP Pro</h1>
        <p class="text-xl">Cliquez sur une étagère → détail produit + stock</p>
        <div class="mt-6 flex gap-4">
          <a href="/admin/Produit" class="btn btn-primary">Gestion Produits</a>
          <a href="/admin/Emplacement" class="btn btn-secondary">Emplacements</a>
        </div>
      </div>
    </div>
    """
```