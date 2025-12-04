from merdoss_admin.ui import Page

@Page("/chat-ia", title="Chat IA Upsell")
def chat_ia():
    return """
    <div class="hero min-h-screen bg-base-200">
      <div class="hero-content text-center max-w-4xl">
        <div class="bg-base-100 rounded-3xl shadow-2xl p-10">
          <h1 class="text-5xl font-bold bg-gradient-to-r from-emerald-400 to-cyan-400 bg-clip-text text-transparent mb-8">
            Chat IA Upsell
          </h1>
          <div id="messages" class="space-y-4 mb-8 max-h-96 overflow-y-auto"></div>
          
          <div class="flex gap-4">
            <input id="question" class="input input-bordered input-lg flex-1" placeholder="Ex: Propose un upsell pour Dupont SARL…" />
            <button onclick="send()" class="btn btn-success btn-lg">Envoyer</button>
          </div>
          
          <div class="mt-6 text-sm text-gray-500">
            Exemples : "Top 5 clients à risque churn" • "Upsell pour Acme Corp" • "CA prévisionnel Q1"
          </div>
        </div>
      </div>
    </div>

    <script>
    async function send() {
      const q = document.getElementById('question').value;
      if (!q) return;
      
      // Message utilisateur
      document.getElementById('messages').innerHTML += 
        `<div class="chat chat-start"><div class="chat-bubble chat-bubble-primary">${q}</div></div>`;
      
      const res = await fetch('/ai/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question: q})
      });
      const data = await res.json();
      
      // Réponse IA
      document.getElementById('messages').innerHTML += 
        `<div class="chat chat-end"><div class="chat-bubble chat-bubble-success">${data.answer}</div></div>`;
      
      document.getElementById('question').value = '';
    }
    </script>
    """