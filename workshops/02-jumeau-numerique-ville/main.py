from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from merdoss_admin import inject_merdoss
import os

# Import modèles
from models import *

app = FastAPI(
    title="Jumeau Numérique 3D – Paris 2025",
    description="Workshop 02 – Ville complète + LiDAR + trafic live",
    version="1.0.0"
)

# Base de données
engine = create_engine("sqlite:///jumeau_ville.db")
SQLModel.metadata.create_all(engine)

# Injection Merdoss avec TOUS les plugins 3D/geo
inject_merdoss(
    app=app,
    db_url="sqlite:///jumeau_ville.db",
    theme="matrix",
    plugins=["geo", "3d", "ai", "realtime", "cesium", "potree", "twin_ai", "traffic"],
    title="Jumeau Numérique Paris",
    favicon="city",
    enable_3d=True,
    cesium_token="ton_token_ici_ou_laisser_vide_pour_mode_gratuit"
)

# === IMPORT AUTOMATIQUE DES DONNÉES AU PREMIER LANCEMENT ===
if not os.path.exists("data/imported.flag"):
    os.makedirs("data", exist_ok=True)
    print("Import des données géospatiales en cours...")
    os.system("merdoss geo import data/paris_batiments.geojson --table=Batiment")
    os.system("merdoss geo import data/paris_routes.geojson --table=Route")
    os.system("merdoss 3d pointcloud data/paris_sample.laz")
    os.system("merdoss 3d tileset data/paris_batiments.geojson --height=hauteur")
    open("data/imported.flag", "w").write("done")
    print("Import terminé – redémarre l’app")

@app.get("/")
def home():
    return {
        "message": "Jumeau numérique prêt",
        "jumeau_3d": "/jumeau-3d",
        "lidar_potree": "/3d/potree",
        "cesium_3d_tiles": "/3d/cesium"
    }