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