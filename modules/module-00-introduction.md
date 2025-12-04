# Module 0 – Introduction & Installation (45 min)

Bienvenue dans le cours le plus puissant de 2025.

### 🎯 Objectif de ce module
À la fin de ces 45 minutes vous aurez :
- Votre environnement de développement 100 % prêt
- Votre première application Merdoss qui tourne en local
- Une vision claire de ce que vous allez livrer d’ici la fin du cours

### Pourquoi Merdoss-Admin change tout ?

| Avant Merdoss                          | Avec Merdoss v5.0                              |
|----------------------------------------|-------------------------------------------------|
| 8–15 packages différents               | 1 seul package                                  |
| 3 à 6 mois pour un dashboard pro       | 5 minutes pour le même résultat (mais en mieux) |
| Déploiement = cauchemar                | 1 commande → en ligne gratuitement              |
| UI moche ou 200 heures de Tailwind     | Thème cyberpunk/glass/matrix intégré par défaut |

→ 180+ modes de visualisation • IA intégrée • GeoAI • 3D Potree/Cesium • Trading • Métavers • Real-time • Multi-tenant • tout ça dans un seul `pip install`.

### Installation complète (la 3 minutes)

```bash
# Option 1 – pip (le plus rapide)
pip install "merdoss-admin[all]"

# Option 2 – Poetry (recommandé pour les projets pro)
poetry new mon-premier-merdoss
cd mon-premier-merdoss
poetry add merdoss-admin --extras "all"
```

Vérification instantanée
```bash
merdoss version
# → MERDOSS_ADMIN v5.0.0 • Décembre 2025 • 180 modes • God Mode ready
```

### Premier test ultra-rapide (30 secondes)

Crée un fichier `test.py` :
```python
from merdoss_admin import hello

hello()
```

Exécute :
```bash
python test.py
# → ✨ MERDOSS ADMIN v5.0 prêt à conquérir le monde !
```

Si tu vois ce message → ton environnement est parfait.

### Prérequis vérifiés (à cocher)

- [ ] Python 3.10+
- [ ] pip ou Poetry
- [ ] (Optionnel mais chaudement recommandé) VS Code + extensions Python / Pylance

### Prochain module
Module 1 → Tu vas créer ta première application professionnelle complète (avec base de données + interface cyberpunk) en exactement 5 minutes.

Prêt ? Ouvre le fichier suivant → [Module 1 – Ta première app en 5 minutes](./module-01-premiere-app.md)
