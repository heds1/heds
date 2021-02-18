import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn import preprocessing

# import ghg data
dat = (
    pd.read_csv('data/new-zealands-greenhouse-gas-emissions-19902016.csv')
        .melt(id_vars=['Gas','Source'],
            var_name='Year', value_name='Units')
        .query('Gas == "All gases"')
        .astype({
            'Year': 'int32',
            'Gas': 'category',
            'Source': 'category'    
        })
        .pivot(index='Year', columns='Source', values='Units')
        .rename(columns={
            "All sources, Gross (excluding LULUCF)": "GrossUnits"
        })
        # set Year as variable rather than index
        .reset_index()
)

# import cars data
# source: http://infoshare.stats.govt.nz/
# Industry sectors --> Transport - TPT --> Motor Vehicles Currently Licensed by Type (Annual-Mar)
years = [str(i) for i in list(range(1990, 2017))] 
cars = (
    pd.read_csv('data/vehicle-regos.csv')
    .rename(columns={
        "Motor Vehicles Currently Licensed by Type (Annual-Mar)": "Year",
        "Unnamed: 1": "NumLicensedVehicles"
    })
    .query("Year.isin(@years)")
    .astype({
        "Year": "int32",
        "NumLicensedVehicles": "int32"
    })
)

# import agricultural data
# source: http://infoshare.stats.govt.nz/
# Industry sectors --> Agriculture - AGR --> Variable by Total New Zealand (Annual-Jun)
agr = (
    pd.read_csv('data/agr.csv').
    rename(columns={
        "Variable by Total New Zealand (Annual-Jun)": "Year",
        "Unnamed: 1": "NumDairyCattle",
    })
    .replace("..", np.NaN)
    .query("Year.isin(@years)")
)

# impute missing values
# (from 1997 to 2001, four out of five years have missing data)
imputer = KNNImputer(n_neighbors=2, weights="uniform")
agr = pd.DataFrame(imputer.fit_transform(agr),columns = agr.columns)

# import agricultural data
# source: http://infoshare.stats.govt.nz/
# Industry sectors --> Alcohol Available for Consumption --> Litres of Alcohol (Annual-Dec)
alcohol = (
    pd.read_csv('data/beer.csv')
    .rename(columns={
        "Litres of Alcohol (Annual-Dec)": "Year",
        "Unnamed: 1": "LitresOfAlcohol",
    })
    .query("Year.isin(@years)")
    .astype({
        "Year": "int32",
        "LitresOfAlcohol": "float"
    })
)

# join all data
dat = (
    dat.merge(
        cars, on='Year', how='left'
    )
    .merge(
        agr, on='Year', how='left'
    )
    .merge(
        alcohol, on='Year', how='left'
    )
)

# let's just take what we need
dat = dat.loc[:, ['Year', 'GrossUnits', 'NumLicensedVehicles', 'NumDairyCattle', 'LitresOfAlcohol']]

# what does it look like now?
dat.head()

# center the explanatory variables!
dat.NumLicensedVehicles = dat.NumLicensedVehicles - dat.NumLicensedVehicles.mean()
dat.NumDairyCattle = dat.NumDairyCattle - dat.NumDairyCattle.mean()
dat.NumSheep = dat.NumSheep - dat.NumSheep.mean()
dat.LitresOfAlcohol = dat.LitresOfAlcohol - dat.LitresOfAlcohol.mean()

reg = smf.ols('GrossUnits ~ NumLicensedVehicles + LitresOfAlcohol + NumDairyCattle', data=dat).fit()
print(reg.summary())

reg = smf.ols('GrossUnits ~ NumLicensedVehicles + LitresOfAlcohol', data=dat).fit()
print(reg.summary())

# Q-Q plot for normality
sm.qqplot(reg.resid, line='r')

# residuals plot
stdres = pd.DataFrame(reg.resid_pearson)
plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')

# leverage plot
sm.graphics.influence_plot(reg, size=8)

reg = smf.ols('GrossUnits ~ NumDairyCattle + I(NumDairyCattle**2)', data=dat).fit()
stdres = pd.DataFrame(reg.resid_pearson)
plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')

sm.qqplot(reg.resid, line='r')