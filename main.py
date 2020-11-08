import pandas as pd
import ta
import matplotlib.pyplot as plt

import seaborn as sns
sns.set()


df = pd.read_csv('USDINR.csv', sep=',')

df = ta.utils.dropna(df)

df = ta.add_all_ta_features(
  df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)

df['EMA26'] = ta.trend.EMAIndicator(df['Close'], 26, True).ema_indicator()
df['EMA12'] = ta.trend.EMAIndicator(df['Close'], 12, True).ema_indicator()

df['MACD'] = ta.trend.MACD(df['Close'], 12, 26, 9).macd()
df['MACD_diff'] = ta.trend.MACD(df['Close'], 12, 26, 9).macd_diff()
df['Signal Line'] = ta.trend.MACD(df['Close'], 12, 26, 9).macd_signal()

df['ROC12'] = ta.momentum.ROCIndicator(df['Close'], 12, True).roc()

df['RSI'] = ta.momentum.RSIIndicator(df['Close'], 14, True).rsi()

df['MFI'] = ta.volume.MFIIndicator(df['High'], df['Low'], df['Close'], df['Volume'], 14, True).money_flow_index()

df.plot('Date', ['RSI', 'MFI'], figsize=(12,6))

# mpl.rcParams['axes.prop_cycle'] = cycler(color=['teal', 'magenta'])

# ax = df.plot('Date', ['Close'], figsize=(24,12))

# ax.plot(['Close'], color = 'blue')

df.to_csv('df2.csv')

plt.tick_params(axis='y',labelsize=20)
plt.tick_params(axis='x',labelsize=17)

# plt.xticks(rotation=90)

plt.legend(loc='best',prop={'size': 20}, markerscale=20)

# plt.xticks(np.arange(min(x), max(x)+1, 1.0))

# ax.set_xticks(ax.get_xticks()[::1])

plt.savefig('RSI_MFI.png')