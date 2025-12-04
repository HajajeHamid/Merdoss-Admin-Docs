# Workshop 06 – Smart City Complète avec Simulation Trafic + Inondation IA

Le jumeau numérique que les mairies paient 200 k€… tu le livres en 48h.

Fonctionnalités :
- Simulation trafic 10 000 véhicules en temps réel
- Prédiction embouteillages IA
- Simulation inondation avec niveaux d’eau dynamiques
- Dashboard exécutif + alertes SMS/email
- Export scénario PDF interactif

Lancement : `uvicorn main:app --reload` → `/smart-city`
```

#### `main.py` (extrait clé)
```python
inject_merdoss(
    app=app,
    theme="glass",
    plugins=["geo", "traffic", "twin_ai", "realtime", "alert", "3d"],
    title="Smart City Paris 2025",
    traffic_simulation=True,
    flood_model="data/paris_dem.tif"
)
```