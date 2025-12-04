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