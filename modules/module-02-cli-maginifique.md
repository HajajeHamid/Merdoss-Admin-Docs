# Module 2 – La CLI Merdoss : Ton Assistant Qui Remplace 5 Développeurs (1h30)

Tu viens de voir que `inject_merdoss()` fait 95 % du boulot.  
Maintenant, tu vas découvrir que la **CLI Merdoss fait les 5 % restants… en 3 secondes**.

### Pourquoi la CLI est la fonctionnalité n°1 utilisée par tous les pros Merdoss

| Tâche habituelle (sans Merdoss)      | Temps normal | Avec la CLI Merdoss             | Temps |
|--------------------------------------|--------------|----------------------------------|-------|
| Créer un projet complet              | 2–4h         | `merdoss new monprojet`          | 8s    |
| Générer une migration DB             | 20 min       | `merdoss db migrate "add users"` | 4s    |
| Importer un fichier SIG (Shapefile, GeoJSON, etc.) | 1–3 jours | `merdoss geo import paris.shp`   | 15s   |
| Créer un dashboard IA                | 3–10 jours   | `merdoss ai generate "ventes 2025"` | 20s |
| Voir un nuage de points 3D           | 1 semaine    | `merdoss 3d pointcloud batiment.laz` | 30s |

### Les 15 commandes que tu vas taper 50 fois par jour

| Commande                                 | Ce qu’elle fait (magie noire incluse)                            | Exemple concret |
|------------------------------------------|-------------------------------------------------------------------|-----------------|
| `merdoss new monprojet --template=cyberpunk` | Crée un projet 100 % prêt (main.py, Dockerfile, merdoss.yaml, etc.) | `merdoss new crm-entreprise` |
| `merdoss run dev`                        | Lancement avec hot-reload + ouverture automatique du navigateur  | –               |
| `merdoss run prod --workers=8`           | Mode production optimisé                                          | –               |
| `merdoss db init`                        | Initialise Alembic (1 seule fois)                                 | –               |
| `merdoss db migrate "add table users"`   | Génère automatiquement la migration                               | –               |
| `merdoss db upgrade`                     | Applique toutes les migrations                                    | –               |
| `merdoss geo import fichier.shp`         | Importe + crée la table + index spatial automatique              | `merdoss geo import routes.geojson` |
| `merdoss geo serve 4326`                 | Lance un serveur de tuiles vectorielles instantané                | –               |
| `merdoss ai generate "dashboard ventes par région"` | Génère code Reflex + widgets IA complet                | → fichier `pages/dashboard_ventes.py` |
| `merdoss 3d pointcloud cloud.laz`        | Convertit & sert un viewer Potree 3D interactif                   | → http://localhost:8000/3d/xxx |
| `merdoss 3d tileset geojson/`            | Crée des 3D Tiles Cesium à partir de GeoJSON + hauteur           | –               |
| `merdoss trading backtest strategy.py BTCUSDT` | Backtesting ultra-rapide avec rapport HTML                  | –               |
| `merdoss cloud deploy . --provider=fly`  | Déploiement 1-clic (Fly.io, Render, Railway) – bientôt disponible | –               |
| `merdoss --help`                         | Affiche toutes les commandes (oui, il y en a plus de 40)          | –               |

### Exercice pratique (15 minutes – à faire maintenant)

1. Ouvre un terminal
2. Tape ces 4 commandes exactement :

```bash
merdoss new demo-cli --template=cyberpunk
cd demo-cli
merdoss run dev
# → ton navigateur s’ouvre automatiquement sur ton dashboard vide
```

3. Dans un deuxième terminal (même dossier) :

```bash
merdoss ai generate "tableau de bord suivi des ventes avec carte et prédiction IA"
# → il te crée 3 fichiers dans pages/ avec tout le code prêt
merdoss run dev   # (relance si besoin)
```

Tu as maintenant un dashboard pro avec carte + prédiction IA… en 2 commandes.

### Résumé : la CLI remplace
- Cookiecutter + 5 templates
- Alembic manuel
- GeoPandas + Fiona + Shapely
- LangChain + OpenAI pour la génération de code
- PotreeConverter + Cesium ion
- Backtrader

Et tout ça avec **une seule dépendance**.

Prochain module : les **règles DB strictes** (les seules que tu dois connaître pour que tout fonctionne à 100 %).

→ [Module 3 – Schéma DB : les 5 règles d’or](./module-03-schema-db-regles.md)