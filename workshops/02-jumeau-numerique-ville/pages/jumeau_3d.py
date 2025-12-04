from merdoss_admin.ui import Page

@Page("/jumeau-3d", title="Jumeau Numérique Paris 2025")
def jumeau_3d_page():
    return """
    <div class="h-screen w-screen relative bg-black">
      <iframe src="/3d/cesium" class="absolute inset-0 w-full h-full border-0"></iframe>
      
      <div class="absolute top-4 left-4 bg-black bg-opacity-80 text-white p-8 rounded-2xl shadow-2xl border border-green-500">
        <h1 class="text-4xl font-bold mb-4 text-green-400">Paris 2025 – Jumeau Numérique</h1>
        <p class="text-lg mb-6">Bâtiments 3D • LiDAR • Trafic temps réel • IA prédiction</p>
        <div class="flex gap-4 flex-wrap">
          <a href="/3d/potree" class="btn btn-error">Vue LiDAR Potree</a>
          <button onclick="startTraffic()" class="btn btn-success">Lancer Simulation Trafic</button>
          <button onclick="predictFlood()" class="btn btn-info">Simulation Inondation</button>
        </div>
      </div>
      
      <div class="absolute bottom-4 right-4 text-white text-sm bg-black bg-opacity-60 px-4 py-2 rounded">
        Powered by Merdoss-Admin v5 • 2025
      </div>
    </div>

    <script>
    function startTraffic() {
      fetch('/traffic/start');
      alert("Simulation trafic démarrée – voitures animées en temps réel");
    }
    function predictFlood() {
      alert("Prédiction inondation IA en cours… (disponible dans v5.1)");
    }
    </script>
    """