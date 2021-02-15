import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf

dat = (
    pd.read_csv('data/new-zealands-greenhouse-gas-emissions-19902016.csv')
        .melt(id_vars=['Gas','Source'],
            var_name='Year', value_name='Units')
        .astype({
            'Year': 'int32',
            'Gas': 'category',
            'Source': 'category'    
        })
)

summary = dat.query("Gas == 'All gases' & Source.isin(['All sources, Net (with LULUCF)', 'All sources, Gross (excluding LULUCF)'])")
summary.Source = summary.Source.cat.remove_unused_categories()
sns.lineplot(data=summary, x='Year', y='Units', hue='Source')

reg = smf.ols('Units ~ Year', data=summary).fit()
print(reg.summary())