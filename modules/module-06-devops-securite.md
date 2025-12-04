# Module 6 – DevOps, Sécurité & Déploiement Professionnel 1-Clic (1h30)

Tu vas passer de localhost → production mondiale en 3 commandes.

### Structure de fichiers générée automatiquement par `merdoss new`

```
monprojet/
├── main.py
├── Dockerfile              ← déjà optimisé multi-stage
├── docker-compose.yml      ← avec Redis + Postgres prêts
├── kubernetes/
│   ├── deployment.yaml
│   └── secrets.yaml
├── fly.toml                ← Fly.io prêt
└── merdoss.yaml            ← toute ta config
```

### Les 5 commandes de déploiement (à connaître par cœur)

| Commande                                    | Résultat final                                  | Coût mensuel |
|---------------------------------------------|--------------------------------------------------|--------------|
| `merdoss run prod --workers=8`              | Production locale ultra-rapide                   | 0 €          |
| `docker-compose up --build -d`              | En ligne sur ton serveur/VPS                     | ~5–15 €      |
| `fly deploy` (depuis le dossier)`         | Déploiement mondial Fly.io (gratuit 3 instances) | 0–19 €       |
| `render deploy` (bientôt intégré)           | Render.com – gratuit tier                                | 0–25 €       |
| `kubectl apply -f kubernetes/`              | Kubernetes partout (GKE, AKS, DigitalOcean)      | variable     |

### Sécurité incluse par défaut (rien à coder)

| Fonctionnalité          | Activée comment                                 |
|-------------------------|--------------------------------------------------|
| JWT + Refresh tokens    | `auth=True` dans inject_merdoss                  |
| RBAC ultra-fin (Casbin) | `plugins=["casbin"]` + fichier policy.csv        |
| Rate limiting           | automatique sur /admin                           |
| CORS configuré          | automatique                                      |
| Secrets via .env        | merdoss.yaml charge automatiquement              |
| HTTPS forcé en prod     | via Traefik dans docker-compose                  |

### Exercice final du module (20 min)

1. Dans ton projet `demo-cli` ou un nouveau :
```bash
merdoss new prod-ready --template=cyberpunk
cd prod-ready
```
2. Ajoute dans `merdoss.yaml` :
```yaml
deploy:
  provider: fly
  region: cdg   # Paris
```
3. Tape :
```bash
fly auth login
fly launch   # (il détecte fly.toml automatiquement)
fly deploy
```
→ Tu as une URL publique https://prod-ready.fly.dev/admin en moins de 4 minutes.

Poste ton lien dans #deployments sur Discord → badge **Merdoss Deploy Master**.

Prochain module (le plus intense)  
Module 7 → Projet final noté + 8 idées de projets pro à livrer en 48h  
→ [Module 7 – Projet Final Professionnel](./module-07-projet-final.md)

Tu es à **deux modules de la certification officielle**.  
Continue comme ça.