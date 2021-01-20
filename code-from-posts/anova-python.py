import pandas as pd
from seaborn import load_dataset
import statsmodels.formula.api as sm
import statsmodels.stats.multicomp as multi

iris = load_dataset("iris")

my_subset = iris[iris["species"].isin(['setosa', 'virginica'])]
subset_model = sm.ols(formula='sepal_length ~ C(species)', data=my_subset)
subset_model.fit().summary()

my_subset.groupby("species").mean()
my_subset.groupby("species").std()

multi_comp = multi.MultiComparison(iris['sepal_length'], iris['species'])
multi_comp.tukeyhsd().summary()