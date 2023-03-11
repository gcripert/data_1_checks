import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


df = pd.read_csv('assets/sports_cars.csv')

df = df.replace(',', '', regex = True)

df['Horsepower'] = df['Horsepower'].astype('int')
df['Price (in USD)'] = df['Price (in USD)'].astype('int')

q_low = df['Horsepower'].quantile(0.01)
q_hi  = df['Horsepower'].quantile(0.99)
df = df[(df['Horsepower'] < q_hi) & (df['Horsepower'] > q_low)]





ax = df.plot (kind = 'scatter', x = 'Horsepower', y = 'Price (in USD)' )

plt.ticklabel_format(style='plain', axis='y', scilimits=(0,0))

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()
