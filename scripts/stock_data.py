import tushare as ts

pro = ts.pro_api('ecaaf0c71f9b375771f2f6e27b2c11803524b20fd37183bb9dbd9835')

# # 拉取数据
# df = pro.daily(
#     ts_code='603881.SH', start_date='20250101', end_date='20250722')
df = pro.daily(**{
    "ts_code": "603881.SH",
    "start_date": 20240101,
    "end_date": 20250722,
}, fields=[
    "ts_code",
    "open",
    "high",
    "low",
    "close",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount"
])
df.to_csv("stock.csv")