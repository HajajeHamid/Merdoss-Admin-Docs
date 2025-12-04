
# Workshop 07 – Supervision IoT Industrielle Temps Réel

Capteurs simulés ou réels (MQTT, Modbus, OPC-UA) → dashboard magnifique.

Fonctionnalités :
- 1000+ capteurs en temps réel (température, pression, vibration…)
- Alertes SMS/Telegram si seuil dépassé
- Jauges, thermomètres, graphiques sparkline
- Historique + export CSV/PDF

Lancement : → `/iot`
```

#### `main.py` (extrait)
```python
inject_merdoss(
    plugins=["realtime", "gauge", "thermometer", "signal_widget", "alert", "mqtt"],
    mqtt_broker="broker.hivemq.com",
    mqtt_topics=["factory/temp/#", "factory/vibration/#"]
)
```
