import pandas as pd
import numpy as np
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

mpg = seaborn.load_dataset('mpg')

# only take observations where cyl in 4, 6, 8
mpg = mpg[mpg['cylinders'].isin([4,6,8])]
# convert to categorical variable
mpg['cylinders'] = mpg['cylinders'].astype("category")

# categorise into 10-mpg ranges
labels = ["{0} - {1}".format(i, i + 9) for i in range(10, 50, 10)]
mpg['mpg_group'] = pd.cut(mpg.mpg, range(10, 60, 10), right=False, labels=labels)

# let's just take what we need
mpg = mpg[['mpg', 'mpg_group', 'cylinders']]

mpg.head()

# create contingency table of counts
contingency_tbl = pd.crosstab(mpg['mpg_group'], mpg['cylinders'])
print(contingency_tbl)
# we hypothesise that the top row (cylinders) 
# predicts mpg group.

# calculate columns sums (axis=1 would be row sums)
print(contingency_tbl/contingency_tbl.sum(axis=0))

# e.g., of the 8-cylinder cars, about 95% had mpg
# between 10-19, whereas only 2% of 4-cylinder
# cars had an mpg of 10-19.

# calculate chi-square statistic and p-value
print(scipy.stats.chi2_contingency(contingency_tbl))

# just to demonstrate this difference:
mpg.groupby('cylinders').mean()['mpg'].plot(
    kind='bar',
    xlabel='Number of cylinders',
    ylabel='Mean miles per gallon')

# post-hoc tests
combns = [
    [4, 6],
    [4, 8],
    [6, 8]
]

for i in combns:
    this_subset = mpg[mpg['cylinders'].isin(i)]
    contingency_tbl = pd.crosstab(this_subset['mpg_group'], this_subset['cylinders'])
    print('\nComparing ' + str(i))
    print(scipy.stats.chi2_contingency(contingency_tbl))