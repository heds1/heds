import seaborn as sns
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# load data
dat = sns.load_dataset("titanic")
dat.info()

# first model
reg = smf.logit('survived ~ sex', data=dat).fit()
print(reg.summary())
np.exp(reg.params)

# relevel the sex variable (change the reference)
dat['sex_releveled'] = pd.Series(pd.Categorical(dat.sex, categories=["male", "female"]))
reg = smf.logit('survived ~ sex_releveled', data=dat).fit()

# simple odds ratios
np.exp(reg.params)

# odds ratios and confidence intervals in a table
params = reg.params
conf = reg.conf_int()
conf['OR'] = params
conf.columns = ["Lower CI", "Upper CI", "OR"]
np.exp(conf)

# confounding of age by sex
reg = smf.logit('survived ~ age', data=dat).fit()
print(reg.summary())
reg = smf.logit('survived ~ age + sex', data=dat).fit()
print(reg.summary())

# final model
reg = smf.logit('survived ~ age + sex_releveled + fare + embark_town', data=dat).fit()
print(reg.summary())
params = reg.params
conf = reg.conf_int()
conf['OR'] = params
conf.columns = ["Lower CI", "Upper CI", "OR"]
np.exp(conf)