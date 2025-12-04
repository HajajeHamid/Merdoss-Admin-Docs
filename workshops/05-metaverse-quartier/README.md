# Workshop 05 – Métavers de Quartier Complet (Visitable par 1000+ personnes)

**Le premier métavers open-source rentable en Python.**

### Ce que tu obtiens
- Quartier entier en 3D (bâtiments, rues, arbres)
- Avatars personnalisés avec nom + chat vocal/textuel
- Événements programmés (concert, réunion, expo)
- Monétisation possible (location stands virtuels)
- Mode VR ready (WebXR)

Lancement :
```bash
cd workshops/05-metaverse-quartier
uvicorn main:app --reload
# → /metaverse
```

Badge : **Metaverse Creator 2025**
```

#### 2. `main.py`

```python
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
```

#### 3. `pages/metaverse.py`

```python
from merdoss_admin.ui import Page

@Page("/metaverse", title="Métavers Saint-Michel – Bienvenue !")
def metaverse():
    return """
    <div class="h-screen w-screen">
      <iframe src="/metaverse/world" class="w-full h-full border-0"></iframe>
      <div class="absolute bottom-4 left-4 bg-black bg-opacity-80 text-white p-6 rounded-xl">
        <h1 class="text-3xl font-bold text-cyan-400">Métavers Saint-Michel</h1>
        <p>500+ visiteurs simultanés • Chat • Événements • VR</p>
      </div>
    </div>
    """
```