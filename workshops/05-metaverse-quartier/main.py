from fastapi import FastAPI
from merdoss_admin import inject_merdoss

app = FastAPI(title="Métavers Quartier Saint-Michel – 2025")

inject_merdoss(
    app=app,
    db_url="sqlite:///metaverse.db",
    theme="nord",
    plugins=["metaverse", "3d", "cesium", "realtime", "avatar", "chat"],
    title="Métavers Saint-Michel",
    favicon="globe",
    metaverse_world="data/quartier_3dtiles",
    enable_vr=True
)

@app.get("/")
def home():
    return {"metaverse": "/metaverse"}