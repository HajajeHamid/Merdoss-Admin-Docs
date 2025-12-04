
# Module 1 – Ta Première Application Pro en 5 Minutes Chrono

Objectif : avoir une application web complète avec base de données + interface moderne qui tourne en local → en moins de 5 minutes.

### Étape 1 – Crée le projet (30 secondes)

```bash
mkdir premiere-app-merdoss && cd premiere-app-merdoss
poetry new . --name premiere_app   # ou rien si tu utilises juste pip
```

### Étape 2 – Crée le fichier `main.py` (copie-colle exactement ça)

```python
from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine
from merdoss_admin import inject_merdoss

# 1. FastAPI app
app = FastAPI(
    title="🚀 Ma Première App Merdoss",
    description="CRM ultra-rapide créé en 5 minutes",
    version="1.0.0"
)

# 2. Modèle = Table SQL (c’est tout !)
class Client(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    email: str = Field(index=True, unique=True)
    entreprise: str
    ca_annuel: float = 0.0

# 3. Création automatique de la base SQLite
engine = create_engine("sqlite:///clients.db")
SQLModel.metadata.create_all(engine)

# 4. Injection magique de Merdoss → 180 modes + thème cyberpunk
inject_merdoss(
    app=app,
    db_url="sqlite:///clients.db",
    title="Merdoss Dashboard – CRM Express",
    theme="cyberpunk",           # ou "glass", "matrix", "dracula"…
    plugins=["ai", "export", "realtime", "trading"],
    favicon="🚀"
)

# Lancement → uvicorn main:app --reload
```

### Étape 3 – Lance l’application

```bash
uvicorn main:app --reload
# → http://127.0.0.1:8000/admin
```

### Ce que tu obtiens immédiatement

Ouvre ton navigateur → `http://127.0.0.1:8000/admin`

Tu as déjà :
- CRUD complet sur la table Client
- Thème cyberpunk magnifique
- Recherche, filtres, pagination
- Export Excel / CSV / PDF
- Mode sombre/clair
- Chat IA intégré (« Analyse mes clients »)
- 180 visualisations différentes disponibles en 1 clic

### Exercice rapide (5 minutes)

Ajoute un deuxième modèle `Produit` avec les champs :
- id, nom, prix, stock, categorie

Relance → tout apparaît automatiquement. Magique.

### Résumé des 3 objets magiques à retenir

| Objet                     | 1 ligne = ?                                        |
|---------------------------|-----------------------------------------------------|
| `app = FastAPI()`         | API complète                                        |
| Ton modèle SQLModel       | Table + formulaires + validations                   |
| `inject_merdoss(...)`     | 180 modes + thème + plugins + sécurité + DevOps     |

Prochain module  
Module 2 → La CLI Merdoss qui va te faire gagner 10h par semaine  
→ [Lire le Module 2](./module-02-cli-maginifique.md) (bientôt disponible)

Tu viens de créer en 5 minutes ce que 95 % des boîtes mettent 3 semaines à faire.  
Continue comme ça, tu vas devenir dangereux.
