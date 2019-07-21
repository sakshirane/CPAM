# import libraries
import pandas as pd

'''
Download monthly prices of Google/Alphabet and S&P 500 index from 2014 to 2018
CSV file downloaded from Yahoo File
start period: 01/01/2014 
end period: 12/31/2018
period format: DD/MM/YEAR
'''
goog = pd.read_csv('GOOG.csv', parse_dates=True, index_col='Date',)
sp_500 = pd.read_csv('S_and_P.csv', parse_dates=True, index_col='Date')

# joining the closing prices of the two datasets 
monthly_prices = pd.concat([goog['Close'], sp_500['Close']], axis=1)
monthly_prices.columns = ['GOOG', 'SP']

# check the head of the dataframe
print(monthly_prices.head())

# calculate monthly returns
monthly_returns = monthly_prices.pct_change(1)
clean_monthly_returns = monthly_returns.dropna(axis=0)  # drop first missing row
print(clean_monthly_returns.head())

# split dependent and independent variable
X = clean_monthly_returns['SP']
y = clean_monthly_returns['GOOG']

# Scipy linear regression
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)

print(slope)