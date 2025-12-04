from merdoss_admin.ui import Page

@Page("/trading", title="Trading Bot Live")
def trading_dashboard():
    return """
    <div class="min-h-screen bg-black text-green-400">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 p-8">
        <div class="lg:col-span-2">
          <iframe src="/trading/chart/BTCUSDT" class="w-full h-96 rounded-xl border-2 border-green-500"></iframe>
          <div class="grid grid-cols-3 gap-4 mt-6">
            <div class="bg-gray-900 p-6 rounded-xl text-center">
              <h3 class="text-2xl font-bold">Win Rate</h3>
              <p class="text-4xl text-emerald-400">73.4%</p>
            </div>
            <div class="bg-gray-900 p-6 rounded-xl text-center">
              <h3 class="text-2xl font-bold">Profit Factor</h3>
              <p class="text-4xl text-emerald-400">2.87</p>
            </div>
            <div class="bg-gray-900 p-6 rounded-xl text-center">
              <h3 class="text-2xl font-bold">PNL 30j</h3>
              <p class="text-4xl text-emerald-400">+428%</p>
            </div>
          </div>
        </div>
        <div class="space-y-6">
          <div class="bg-gray-900 p-6 rounded-xl">
            <h2 class="text-3xl font-bold mb-4">Derniers Signaux Telegram</h2>
            <div class="space-y-3 text-sm">
              <div class="bg-green-900 p-3 rounded">BUY BTCUSDT @ 83250 → TP 89200</div>
              <div class="bg-red-900 p-3 rounded">SELL ETHUSDT @ 3420 → TP 3100</div>
            </div>
          </div>
          <button onclick="startBot()" class="btn btn-success btn-lg w-full">LANCER LE BOT LIVE</button>
        </div>
      </div>
    </div>
    """