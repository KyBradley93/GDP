import pandas as pd
import patsy
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

gdp = pd.read_csv('all_data.csv')

chile = gdp[gdp['Country'] == 'Chile']
china = gdp[gdp['Country'] == 'China']
germany = gdp[gdp['Country'] == 'Germany']
mexico = gdp[gdp['Country'] == 'Mexico']
usa = gdp[gdp['Country'] == 'United States of America']
zimbabwe = gdp[gdp['Country'] == 'Zimbabwe']

plt.plot(chile['Year'], chile['GDP'] / 1e9, label='Chile')
plt.plot(china['Year'], china['GDP'] / 1e9, label='China')
plt.plot(germany['Year'], germany['GDP'] / 1e9, label='Germany')
plt.plot(mexico['Year'], mexico['GDP'] / 1e9, label='Mexico')
plt.plot(usa['Year'], usa['GDP'] / 1e9, label='USA')
plt.plot(zimbabwe['Year'], zimbabwe['GDP'] / 1e9, label='Zimbabwe')

plt.xlabel('Year')
plt.ylabel('GDP (billions)')
plt.legend()

plt.show()
plt.clf()


plt.plot(chile['Year'], chile['Life expectancy at birth (years)'], label='Chile')
plt.plot(china['Year'], china['Life expectancy at birth (years)'], label='China')
plt.plot(germany['Year'], germany['Life expectancy at birth (years)'], label='Germany')
plt.plot(mexico['Year'], mexico['Life expectancy at birth (years)'], label='Mexico')
plt.plot(usa['Year'], usa['Life expectancy at birth (years)'], label='USA')
plt.plot(zimbabwe['Year'], zimbabwe['Life expectancy at birth (years)'], label='Zimbabwe')

plt.xlabel('Year')
plt.ylabel('Life expectancy at birth (years)')
plt.legend()

plt.show()
plt.clf()

print('AVG GDP: \n', gdp.groupby('Country')['GDP'].mean() / 1e9)
print('AVG Life Exp: \n', gdp.groupby('Country')['Life expectancy at birth (years)'].mean())