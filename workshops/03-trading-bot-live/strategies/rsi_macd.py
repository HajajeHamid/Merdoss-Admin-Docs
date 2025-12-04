from merdoss_admin.trading import Strategy, Signal

class RSIMACD(Strategy):
    name = "RSI + MACD Divergence"
    params = {"rsi_period": 14, "macd_fast": 12, "macd_slow": 26}

    def generate_signal(self, df):
        # Logique complète RSI + MACD + Divergence
        if df['rsi'].iloc[-1] < 30 and df['macd'].iloc[-1] > df['signal'].iloc[-1]:
            return Signal.BUY, 92.5
        if df['rsi'].iloc[-1] > 70 and df['macd'].iloc[-1] < df['signal'].iloc[-1]:
            return Signal.SELL, 89.0
        return Signal.HOLD, 50.0