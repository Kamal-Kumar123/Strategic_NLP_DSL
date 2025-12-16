import pandas as pd

class BacktestEngine:
    
    def __init__(self, df):
        self.df = df.copy()
        self.trades = []
        self.equity_curve = []

    def run(self, entry_signal, exit_signal):
        position = 0
        entry_price = None
        entry_date = None
        equity = 1.0  # starting capital = 1 (normalized)

        for i in range(len(self.df)):
            price = self.df.loc[i, "close"]
            date = self.df.loc[i, "datetime"]

            # ENTER TRADE
            if position == 0 and entry_signal[i]:
                position = 1
                entry_price = price
                entry_date = date

            # EXIT TRADE
            elif position == 1 and exit_signal[i]:
                exit_price = price
                exit_date = date

                pnl = (exit_price - entry_price) / entry_price
                equity *= (1 + pnl)

                self.trades.append({
                    "entry_date": entry_date,
                    "exit_date": exit_date,
                    "entry_price": entry_price,
                    "exit_price": exit_price,
                    "pnl_pct": pnl * 100
                })

                position = 0
                entry_price = None
                entry_date = None

            self.equity_curve.append(equity)

        return self._results()

    def _results(self):
        equity_series = pd.Series(self.equity_curve)
        peak = equity_series.cummax()
        drawdown = (equity_series - peak) / peak

        return {
            "total_return_pct": (equity_series.iloc[-1] - 1) * 100,
            "max_drawdown_pct": drawdown.min() * 100,
            "number_of_trades": len(self.trades),
            "trades": self.trades
        }
    
    def pretty_print_trades(self, trades):
        for i, t in enumerate(trades, 1):
            print(
                f"Trade {i}: "
                f"Entry {t['entry_date']} @ {t['entry_price']} | "
                f"Exit {t['exit_date']} @ {t['exit_price']} | "
                f"PnL: {t['pnl_pct']:.2f}%"
            )

