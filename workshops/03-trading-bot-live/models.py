from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class TradeSignal(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    pair: str
    side: str  # BUY ou SELL
    price_entry: float
    price_tp: Optional[float] = None
    price_sl: Optional[float] = None
    strategy: str
    confidence: float  # 0-100
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    executed: bool = False
    pnl: Optional[float] = None

class BacktestResult(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    strategy: str
    pair: str
    timeframe: str
    start_date: str
    end_date: str
    total_trades: int
    win_rate: float
    profit_factor: float
    max_drawdown: float
    net_profit: float
    sharpe_ratio: Optional[float] = None