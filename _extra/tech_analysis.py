import pandas as pd
import ta
from tushare import stock

df = pd.read_csv("../data/stock.csv")
# 添加技术指标
df = ta.add_all_ta_features(
    df,
    open="open", high="high", low="low", close="close", volume="vol",
    fillna=True
)
print(df.head())
df.to_csv("stock.csv")