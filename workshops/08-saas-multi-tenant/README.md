# Workshop 08 – SaaS B2B Multi-Entreprise avec Facturation Stripe

Le SaaS que tout le monde rêve de vendre en abonnement.

Fonctionnalités :
- Multi-tenant complet (une instance = 1000 entreprises)
- RBAC Casbin ultra-fin (admin, manager, user, auditor…)
- Facturation Stripe automatique (mensuelle
- Dashboard par entreprise + quota
- Sous-domaines automatiques (acme.mondomaine.com)

Lancement : → `/saas`
```

#### `main.py` (extrait)
```python
inject_merdoss(
    plugins=["casbin", "billing", "realtime", "stripe"],
    stripe_secret_key=os.getenv("STRIPE_SK"),
    multi_tenant=True,
    subdomain_routing=True
)
```