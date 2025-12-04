# Module 3 – Schéma de Base de Données : Les 5 Règles Strictes à Respecter (1h45)

Merdoss-Admin est **zero-config**… mais il n’est pas magique : il a besoin de 5 règles simples.  
Si tu les respectes → tout fonctionne automatiquement.  
Si tu les oublies → tu perds des heures à chercher pourquoi.

### Les 5 règles d’or (à tatouer sur ton front)

| Règle | Code obligatoire | Pourquoi c’est NON NÉGOCIABLE |
|------|------------------|--------------------------------|
| 1. Chaque table doit avoir un `id: int` en primary key | `id: int = Field(default=None, primary_key=True)` | Merdoss utilise l’ID pour tout (relations, CRUD, export, realtime…) |
| 2. Les relations → toujours `foreign_key="table.id"` | `user_id: int = Field(foreign_key="user.id")` | Sinon pas de select déroulant ni de relation affichée |
| 3. Colonne géométrique → `Geometry("POINT", srid=4326)` | (voir exemple ci-dessous) | Sinon le plugin geo ne la détecte pas |
| 4. Nommage classe = nom table (par défaut) | `class Client(SQLModel, table=True):` | Merdoss utilise le nom de classe directement |
| 5. Utiliser SQLModel (pas SQLAlchemy classique) | from sqlmodel import SQLModel, Field | Compatibilité 100 % avec auto_generate_app |

### Exemples de modèles parfaits (à copier-coller)

```python
from sqlmodel import SQLModel, Field
from typing import Optional
from geoalchemy2 import Geometry

# 1. Modèle classique
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(index=True)
    is_active: bool = True

# 2. Modèle avec relation
class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    total: float
    user_id: int = Field(foreign_key="user.id")   # ← obligatoire
    status: str = "pending"

# 3. Modèle géographique (plugin geo activé)
class Site(SIGModel, table=True):   # SIGModel = SQLModel + geo support
    id: int = Field(default=None, primary_key=True)
    nom: str
    geom: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))
```

### Exercice pratique (10 minutes)

Dans ton projet `demo-cli` créé au Module 2 :

1. Ajoute un fichier `models.py` avec les 3 modèles ci-dessus
2. Dans `main.py`, ajoute en haut :
   ```python
   from models import *
   SQLModel.metadata.create_all(engine)
   ```
3. Relance → tu vois les 3 tables apparaître automatiquement avec :
   - Relations cliquables
   - Carte interactive pour la table Site
   - Export PDF/Excel fonctionnel

### Erreurs classiques (et comment les éviter)

| Erreur fréquente                  | Message d’erreur typique              | Solution en 1 ligne |
|-----------------------------------|---------------------------------------|---------------------|
| Oubli du `id` primary key         | Table non détectée                    | Ajouter le champ id |
| `foreign_key="users.id"` au lieu de `"user.id"` | Relation non affichée          | Respecter le nom exact de la table |
| Utiliser `str` au lieu de `Geometry` | Colonne geom ignorée               | Importer Geometry + plugin geo |

### Résumé visuel des 5 règles (à sauvegarder)

```
RÈGLE 1 → id: int + primary_key=True        ← OBLIGATOIRE
RÈGLE 2 → foreign_key="table.id"           ← OBLIGATOIRE pour les relations
RÈGLE 3 → Geometry("TYPE", srid=xxxx)      ← si tu veux des cartes
RÈGLE 4 → class MonModel(SQLModel, table=True)
RÈGLE 5 → Toujours SQLModel, jamais SQLAlchemy pur
```

Tu respectes ces 5 règles → Merdoss fait **littéralement tout le reste**.

Prochain module (le plus impressionnant) :  
**Module 4 – Les 12 domaines professionnels que tu vas pouvoir livrer dès demain**

→ [Module 4 – Domaines Pro (★ star ★)](./module-04-domaines-pro.md)
