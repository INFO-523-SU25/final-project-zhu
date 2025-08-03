# Data
This project uses a cleaned dataset of Shanghai AtHub (数据港, 603881.SH), consisting of 375 trading days of stock market data enriched with over 25 technical indicators. The dataset is designed to support time series modeling and technical analysis for forecasting stock price movements.

* **Source**: Retrieved and engineered using Tushare and `ta`-lib technical analysis library.
* **Dimensions**: `375` rows $\times$ `31` columns
* **Target variable**: `close` (the closing price of the stock)
* **Features**:

  * **OHLC data**: open, high, low, close
  * **Volume indicators**: vol, amount, OBV, CMF, VWAP, VPT, MFI
  * **Volatility indicators**: Bollinger Band Width, ATR, Ulcer Index
  * **Trend indicators**: MACD, ADX, CCI, Aroon
  * **Momentum indicators**: RSI, Williams %R, ROC, Awesome Oscillator, PPO histogram

These indicators are commonly used by traders and quants to detect patterns, momentum shifts, and breakout signals in price movement.

# Codebook for `df_clean.csv` Dataset

## Variable Names and Descriptions:

| Variable            | Description                                       |
| ------------------- | ------------------------------------------------- |
| `ts_code`           | Stock code (603881.SH)                            |
| `open`              | Opening price of the day                          |
| `high`              | Highest price of the day                          |
| `low`               | Lowest price of the day                           |
| `close`             | Closing price (target variable)                   |
| `pct_chg`           | Daily percentage change                           |
| `vol`               | Trading volume                                    |
| `amount`            | Trading amount                             |
| `volume_obv`        | On-Balance Volume                                 |
| `volume_cmf`        | Chaikin Money Flow                                |
| `volume_vpt`        | Volume Price Trend                                |
| `volume_vwap`       | Volume Weighted Average Price                     |
| `volume_mfi`        | Money Flow Index                                  |
| `volatility_bbw`    | Bollinger Band Width                              |
| `volatility_atr`    | Average True Range                                |
| `volatility_ui`     | Ulcer Index                                       |
| `trend_macd`        | MACD line                                         |
| `trend_macd_signal` | MACD signal line                                  |
| `trend_macd_diff`   | MACD histogram (diff between MACD and signal)     |
| `trend_adx`         | Average Directional Index                         |
| `trend_adx_pos`     | ADX positive directional indicator                |
| `trend_adx_neg`     | ADX negative directional indicator                |
| `trend_cci`         | Commodity Channel Index                           |
| `momentum_rsi`      | Relative Strength Index                           |
| `momentum_wr`       | Williams %R                                       |
| `momentum_roc`      | Rate of Change                                    |
| `momentum_ao`       | Awesome Oscillator                                |
| `momentum_ppo_hist` | Percentage Price Oscillator (histogram)           |
| `trend_aroon_up`    | Aroon Up indicator                                |
| `trend_aroon_down`  | Aroon Down indicator                              |
| `trend_aroon_ind`   | Aroon Oscillator (difference between Up and Down) |


## Data Types:

| Column            | Data Type |
| ----------------- | --------- |
| `ts_code`         | object    |
| All other columns | float64   |


