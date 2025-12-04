# Module 5 – UI Cyberpunk & Création de Widgets en 5 Lignes Max (1h30)

Merdoss n’est pas juste fonctionnel… il est **magnifique par défaut**.

### Les 6 thèmes intégrés (1 mot à changer)

```python
inject_merdoss(app, ..., theme="cyberpunk")   # défaut – le plus beau
# ou
theme="glass"      # ultra-moderne transparent
theme="matrix"     # vert fluo hacker
theme="dracula"    # violet/noir
theme="nord"       # minimal froid
theme="dark"       # classique sombre
```

### Les 80+ widgets prêts à l’emploi (copier-coller direct)

```python
from merdoss_admin.ui.widgets import (
    StatCard, ProgressRing, AvatarGroup, Gauge,
    Sparkline, Timeline, HotspotMap, SignalStrength
)

# Exemple 1 – Carte KPI de ouf
card = StatCard(
    title="Chiffre d'affaires 2025",
    value="4.8M€",
    trend=+34.8,
    color="emerald",
    icon="💰",
    sparkline_data=[1.2, 1.8, 2.4, 3.1, 4.0, 4.8]
)

# Exemple 2 – Jauge IoT
gauge = Gauge(value=87, max=100, label="Température serveur", color="red", unit="°C")

# Exemple 3 – Groupe d’avatars
avatars = AvatarGroup(
    users=["Alice", "Bob", "Charlie", "David"],
    size="lg",
    max_display=4
)
```

→ Tous ces widgets renvoient du **HTML Tailwind + DaisyUI + animations** prêt à intégrer dans Reflex, HTMX ou directement dans tes templates.

### Créer TON propre widget en 5 lignes (exemple réel)

```python
from merdoss_admin.ui.base import Widget

class CryptoPriceWidget(Widget):
    template_name = "widgets/crypto_price.html"
    
    def get_context(self):
        return {
            "symbol": "BTCUSDT",
            "price": 83250.0,
            "change_24h": +5.67,
            "color": "emerald" if self.change_24h > 0 else "red"
        }

# Utilisation
crypto = CryptoPriceWidget()
print(crypto.to_html())  # → HTML magnifique instantanément
```

### Exercice (15 min – très fun)

1. Crée un fichier `widgets/mon_super_kpi.py`
2. Fais hériter de `Widget`
3. Crée un template HTML dans `templates/widgets/mon_super_kpi.html` avec Tailwind
4. Utilise-le dans une page Reflex ou directement dans `main.py`

Les 5 plus beaux widgets seront intégrés **directement dans la prochaine version officielle de Merdoss-Admin v5.1** avec ton nom en crédit.

Prochain module → [Module 6 – DevOps & Déploiement 1-clic](./module-06-devops-securite.md)