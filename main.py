import pandas as pd
import matplotlib.pyplot as plt

btc_df = pd.read_parquet(path='test_data.parquet')
btc_df = btc_df.reset_index(drop=False)

fig, ax = plt.subplots()
ax.plot(btc_df['timestamp'], btc_df['close'])
plt.show()