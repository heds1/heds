import pandas as pd
from scipy import stats
import seaborn
import matplotlib.pyplot as plt

mpg = seaborn.load_dataset('mpg')

plt.scatter(x=mpg['weight'], y=mpg['mpg'])
plt.xlabel("Weight")
plt.ylabel("Miles per gallon")
plt.show()

# get r
stats.pearsonr(mpg['mpg'], mpg['weight'])

# get r2
stats.pearsonr(mpg['mpg'], mpg['weight'])[0] ** 2