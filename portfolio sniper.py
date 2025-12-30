import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Portfolio specs

Assets = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "GC=F", "XOM", "WMT", "COST", "JPM"]  #You can change these tickers as you wish
period= "5y" #You can change the period as you wish (e.g: "1y", "6mo", "3mo", "5y", "10y") keep in mind that the larger the period the longer it will take the fetch and process the data
print(f"Fetching data for your portfolio)")

#Parameters
annual_rf=0.042  #the 2025 is roughly 4,2%
daily_rf= annual_rf/252 #Calculating daily risk free rate assuming 252 trading days in a year

print(f"Fetching data and applying Risk free rate of {annual_rf*100}%...")
data= yf.download(Assets, period=period)["Close"]
returns= data.pct_change().dropna()

#Calculate correlation matrix
correlation_matrix=returns.corr()

#Calculate sharpe ratio
excess_daily_returns= returns - daily_rf
sharpe_ratios=(excess_daily_returns.mean()/returns.std())*np.sqrt(252) #Annualizing the sharpe ratio

#Calculate Sortino ratio
downside_returns=returns[returns<0]
sortino_ratio=(excess_daily_returns.mean() / downside_returns.std())*np.sqrt(252) #Annualizing the sortino ratio


#VISUALIZATION OF RESULTS

print("---PROFESSIONAL RISK-ADJUSTED METRICS FOR YOUR PORTFOLIO---")
metrics=pd.DataFrame({
    "Sharpe ratio":sharpe_ratios,
    "Sortino_ratio":sortino_ratio
}).sort_values(by="Sharpe ratio", ascending=False)

print(metrics)


#Creating the heatmap for correlation matrix

plt.figure(figsize=(12,9))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title(f"Portfolio assets correlation matrix ({period})", fontsize=16)
plt.style.use('dark_background')

#Final adjustments

plt.xticks(rotation=45)
plt.yticks(rotation=0)


print("--Graph incoming check your taskbar!!---")
plt.show()
