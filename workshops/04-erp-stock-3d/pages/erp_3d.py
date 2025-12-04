from merdoss_admin.ui import Page

@Page("/erp-3d", title="Entrepôt 3D Interactif")
def erp_3d():
    return """
    <div class="h-screen w-screen relative">
      <iframe src="/3d/potree" class="absolute inset-0 w-full h-full"></iframe>
      <div class="absolute top-4 left-4 bg-black bg-opacity-90 text-white p-8 rounded-xl">
        <h1 class="text-4xl font-bold text-purple-400 mb-4">Entrepôt 3D – ERP Pro</h1>
        <p class="text-xl">Cliquez sur une étagère → détail produit + stock</p>
        <div class="mt-6 flex gap-4">
          <a href="/admin/Produit" class="btn btn-primary">Gestion Produits</a>
          <a href="/admin/Emplacement" class="btn btn-secondary">Emplacements</a>
        </div>
      </div>
    </div>
    """