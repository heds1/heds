import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset('mpg')

cyls = [4,6,8]
mpg = mpg[mpg.cylinders.isin(cyls)]

plt.scatter(x=mpg.displacement, y=mpg.mpg)
plt.xlabel('Engine displacement')
plt.ylabel('Miles per gallon')

stats.pearsonr(mpg.mpg, mpg.displacement)

g = sns.FacetGrid(mpg,
    col="cylinders")
g.map(sns.scatterplot, "displacement", "mpg")

for i in cyls:
    subset = mpg[mpg.cylinders == i]
    print('Miles per gallon predicted by engine displacement for ' + str(i) + '-cylinder cars')
    res = stats.pearsonr(subset.mpg, subset.displacement)
    print('Pearson correlation coefficient: ' + str(res[0]))
    print('Associated p-value: ' + str(res[1]))
    print('')