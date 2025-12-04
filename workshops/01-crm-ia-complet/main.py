from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from merdoss_admin import inject_merdoss

# Import des modèles (crée le fichier models.py juste après)
from models import *

app = FastAPI(
    title="Merdoss CRM IA – Workshop 01",
    description="CRM complet + IA upsell – Livrable professionnel",
    version="1.0.0"
)

# Base de données (SQLite local, PostgreSQL en prod)
engine = create_engine("sqlite:///crm_ia.db")
SQLModel.metadata.create_all(engine)

# Injection magique Merdoss
inject_merdoss(
    app=app,
    db_url="sqlite:///crm_ia.db",
    theme="glass",
    plugins=["ai", "export", "realtime", "kanban"],
    title="CRM IA Professionnel",
    favicon="rocket",
    login_required=False  # passe à True + JWT en prod
)

@app.get("/")
def home():
    return {"message": "Ton CRM IA est prêt – va sur /admin"}