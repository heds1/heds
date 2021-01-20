{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.6-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3",
   "language": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<class 'statsmodels.iolib.summary.Summary'>\n",
       "\"\"\"\n",
       "                            OLS Regression Results                            \n",
       "==============================================================================\n",
       "Dep. Variable:           sepal_length   R-squared:                       0.619\n",
       "Model:                            OLS   Adj. R-squared:                  0.614\n",
       "Method:                 Least Squares   F-statistic:                     119.3\n",
       "Date:                Wed, 20 Jan 2021   Prob (F-statistic):           1.67e-31\n",
       "Time:                        19:45:41   Log-Likelihood:                -111.73\n",
       "No. Observations:                 150   AIC:                             229.5\n",
       "Df Residuals:                     147   BIC:                             238.5\n",
       "Df Model:                           2                                         \n",
       "Covariance Type:            nonrobust                                         \n",
       "============================================================================================\n",
       "                               coef    std err          t      P>|t|      [0.025      0.975]\n",
       "--------------------------------------------------------------------------------------------\n",
       "Intercept                    5.0060      0.073     68.762      0.000       4.862       5.150\n",
       "C(species)[T.versicolor]     0.9300      0.103      9.033      0.000       0.727       1.133\n",
       "C(species)[T.virginica]      1.5820      0.103     15.366      0.000       1.379       1.785\n",
       "==============================================================================\n",
       "Omnibus:                        1.188   Durbin-Watson:                   2.043\n",
       "Prob(Omnibus):                  0.552   Jarque-Bera (JB):                0.785\n",
       "Skew:                           0.119   Prob(JB):                        0.675\n",
       "Kurtosis:                       3.263   Cond. No.                         3.73\n",
       "==============================================================================\n",
       "\n",
       "Notes:\n",
       "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
       "\"\"\""
      ],
      "text/html": "<table class=\"simpletable\">\n<caption>OLS Regression Results</caption>\n<tr>\n  <th>Dep. Variable:</th>      <td>sepal_length</td>   <th>  R-squared:         </th> <td>   0.619</td>\n</tr>\n<tr>\n  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.614</td>\n</tr>\n<tr>\n  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   119.3</td>\n</tr>\n<tr>\n  <th>Date:</th>             <td>Wed, 20 Jan 2021</td> <th>  Prob (F-statistic):</th> <td>1.67e-31</td>\n</tr>\n<tr>\n  <th>Time:</th>                 <td>19:45:41</td>     <th>  Log-Likelihood:    </th> <td> -111.73</td>\n</tr>\n<tr>\n  <th>No. Observations:</th>      <td>   150</td>      <th>  AIC:               </th> <td>   229.5</td>\n</tr>\n<tr>\n  <th>Df Residuals:</th>          <td>   147</td>      <th>  BIC:               </th> <td>   238.5</td>\n</tr>\n<tr>\n  <th>Df Model:</th>              <td>     2</td>      <th>                     </th>     <td> </td>   \n</tr>\n<tr>\n  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n</tr>\n</table>\n<table class=\"simpletable\">\n<tr>\n              <td></td>                <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n</tr>\n<tr>\n  <th>Intercept</th>                <td>    5.0060</td> <td>    0.073</td> <td>   68.762</td> <td> 0.000</td> <td>    4.862</td> <td>    5.150</td>\n</tr>\n<tr>\n  <th>C(species)[T.versicolor]</th> <td>    0.9300</td> <td>    0.103</td> <td>    9.033</td> <td> 0.000</td> <td>    0.727</td> <td>    1.133</td>\n</tr>\n<tr>\n  <th>C(species)[T.virginica]</th>  <td>    1.5820</td> <td>    0.103</td> <td>   15.366</td> <td> 0.000</td> <td>    1.379</td> <td>    1.785</td>\n</tr>\n</table>\n<table class=\"simpletable\">\n<tr>\n  <th>Omnibus:</th>       <td> 1.188</td> <th>  Durbin-Watson:     </th> <td>   2.043</td>\n</tr>\n<tr>\n  <th>Prob(Omnibus):</th> <td> 0.552</td> <th>  Jarque-Bera (JB):  </th> <td>   0.785</td>\n</tr>\n<tr>\n  <th>Skew:</th>          <td> 0.119</td> <th>  Prob(JB):          </th> <td>   0.675</td>\n</tr>\n<tr>\n  <th>Kurtosis:</th>      <td> 3.263</td> <th>  Cond. No.          </th> <td>    3.73</td>\n</tr>\n</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
     },
     "metadata": {},
     "execution_count": 12
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from seaborn import load_dataset\n",
    "import statsmodels.formula.api as sm\n",
    "\n",
    "iris = load_dataset(\"iris\")\n",
    "\n",
    "\n",
    "# my_model = sm.ols(formula='sepal_length ~ C(species)', data=iris)\n",
    "\n",
    "# my_model.fit().summary()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "     sepal_length  sepal_width  petal_length  petal_width    species\n",
       "0             5.1          3.5           1.4          0.2     setosa\n",
       "1             4.9          3.0           1.4          0.2     setosa\n",
       "2             4.7          3.2           1.3          0.2     setosa\n",
       "3             4.6          3.1           1.5          0.2     setosa\n",
       "4             5.0          3.6           1.4          0.2     setosa\n",
       "..            ...          ...           ...          ...        ...\n",
       "145           6.7          3.0           5.2          2.3  virginica\n",
       "146           6.3          2.5           5.0          1.9  virginica\n",
       "147           6.5          3.0           5.2          2.0  virginica\n",
       "148           6.2          3.4           5.4          2.3  virginica\n",
       "149           5.9          3.0           5.1          1.8  virginica\n",
       "\n",
       "[100 rows x 5 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>sepal_length</th>\n      <th>sepal_width</th>\n      <th>petal_length</th>\n      <th>petal_width</th>\n      <th>species</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>5.1</td>\n      <td>3.5</td>\n      <td>1.4</td>\n      <td>0.2</td>\n      <td>setosa</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>4.9</td>\n      <td>3.0</td>\n      <td>1.4</td>\n      <td>0.2</td>\n      <td>setosa</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>4.7</td>\n      <td>3.2</td>\n      <td>1.3</td>\n      <td>0.2</td>\n      <td>setosa</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>4.6</td>\n      <td>3.1</td>\n      <td>1.5</td>\n      <td>0.2</td>\n      <td>setosa</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>5.0</td>\n      <td>3.6</td>\n      <td>1.4</td>\n      <td>0.2</td>\n      <td>setosa</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>145</th>\n      <td>6.7</td>\n      <td>3.0</td>\n      <td>5.2</td>\n      <td>2.3</td>\n      <td>virginica</td>\n    </tr>\n    <tr>\n      <th>146</th>\n      <td>6.3</td>\n      <td>2.5</td>\n      <td>5.0</td>\n      <td>1.9</td>\n      <td>virginica</td>\n    </tr>\n    <tr>\n      <th>147</th>\n      <td>6.5</td>\n      <td>3.0</td>\n      <td>5.2</td>\n      <td>2.0</td>\n      <td>virginica</td>\n    </tr>\n    <tr>\n      <th>148</th>\n      <td>6.2</td>\n      <td>3.4</td>\n      <td>5.4</td>\n      <td>2.3</td>\n      <td>virginica</td>\n    </tr>\n    <tr>\n      <th>149</th>\n      <td>5.9</td>\n      <td>3.0</td>\n      <td>5.1</td>\n      <td>1.8</td>\n      <td>virginica</td>\n    </tr>\n  </tbody>\n</table>\n<p>100 rows × 5 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 18
    }
   ],
   "source": [
    "my_subset = iris[iris[\"species\"].isin(['setosa', 'virginica'])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}