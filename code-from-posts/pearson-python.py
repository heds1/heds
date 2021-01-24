import pandas as pd
from scipy import stats
import seaborn
import matplotlib.pyplot as plt

mpg = seaborn.load_dataset('mpg')

plt.scatter(x=mpg['weight'], y=mpg['mpg'])
plt.xlabel("Weight")
plt.ylabel("Miles per gallon")
plt.show()

stats.pearsonr(mpg['mpg'], mpg['weight'])