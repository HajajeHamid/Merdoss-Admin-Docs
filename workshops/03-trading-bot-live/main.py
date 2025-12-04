from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from merdoss_admin import inject_merdoss
import os

app = FastAPI(
    title="Merdoss Trading Pro 2025",
    description="Workshop 03 – Trading Bot + Backtesting + Telegram Live",
    version="1.0.0"
)

engine = create_engine("sqlite:///trading.db")
SQLModel.metadata.create_all(engine)

inject_merdoss(
    app=app,
    db_url="sqlite:///trading.db",
    theme="cyberpunk",
    plugins=["trading", "ai", "realtime", "export", "telegram"],
    title="Trading Bot Pro",
    favicon="chart",
    trading_exchanges=["binance", "bybit"],
    trading_default_pair="BTCUSDT",
    telegram_bot_token=os.getenv("TELEGRAM_TOKEN", "ton_token_ici"),
    telegram_chat_id=os.getenv("TELEGRAM_CHAT_ID", "ton_chat_id")
)

@app.get("/")
def home():
    return {
        "message": "Trading Bot prêt",
        "dashboard": "/trading",
        "backtesting": "/trading/backtest",
        "live_signals": "/trading/signals"
    }