import pandas as pd
import yfinance as yf
import numpy as np 
import matplotlib.pyplot as plt

# 1. SETUP DEGLI INGREDIENTI (La lista dei Ticker)
# Ho scelto TLT come proxy per i Treasury Bond a lungo termine


assets = ["AAPL","GC=F","GOOGL","NVDA","AMD","WMT","COST","CCJ","META","AMZN","MSFT","TLT","BRK-B"]

#The datas

start_date="2015-01-01"
end_date = "2025-12-30"

print(f"Downloading data for selected assets...let me cook them for you")

raw_data=yf.download(assets, start=start_date, end=end_date,auto_adjust=True)

if isinstance(raw_data.columns, pd.MultiIndex):
    try:
        data = raw_data["Close"]
    except KeyError:
        data = raw_data["Close"]
else:
    data = raw_data



data=data.dropna()

if data.empty:
    print("I wasn't able to download any data. Please check the ticker symbols and your internet connection.")
else:
    print("Successfully downloaded data and cleaned them")


print("Data downloaded successfully!")

#Let's calculate the returns

stocks_return= data.pct_change().dropna()
print("---Data fetched successfully! Now let's cook the with Monte Carlo simulation!---")

#MONTECARLO SIMULATION
scenarios=50000
days_in_year = 252
risk_free_rate = 0.042

#Initialize arrays

weights_array = np.zeros((scenarios, len(data.columns)))
returns_array = np.zeros(scenarios)
volatility_array= np.zeros(scenarios)
sharpe_array = np.zeros(scenarios)
np.random.seed(42)  # For reproducibility

for index in range (scenarios):
    #Generate random weights
    numbers=np.array(np.random.random(len(data.columns)))
    weights = numbers / np.sum(numbers)
    weights_array[index, :]= weights
    #Calculate metrics
    returns_array[index]=np.sum(stocks_return.mean() * days_in_year * weights)
    volatility_array[index] = np.sqrt(np.dot(weights.T, np.dot(stocks_return.cov() *days_in_year, weights)))
    sharpe_array[index] = (returns_array[index]- risk_free_rate) / volatility_array[index]
   
   


#let's find the winnder

index_max_sharpe = sharpe_array.argmax()
optimal_weights = weights_array[index_max_sharpe, :]


#CREATE THE PRO SUMMARY TABLE


total_stock_return = (data.iloc[-1] / data.iloc[0]) -1
    

#Create the dataframe

summary_table= pd.DataFrame({
    "Asset": data.columns,
    "Allocation (%)": optimal_weights * 100,
    "Current price ($)": data.iloc[-1].values,
    "Total Stock Return (%)": total_stock_return.values * 100
})

#Let's do some formatting

summary_table = summary_table.sort_values(by="Allocation (%)", ascending=False)
summary_table = summary_table.round(2) #it means we want it to round by 2 decimals

print("----OPTIOMAL PORTFOLIO SUMMARY ----")
print(summary_table)

#Now we do the scatter plot that is very useful

plt.figure(figsize=(12,8))
scatter = plt.scatter(volatility_array, returns_array, c=sharpe_array, cmap='viridis', alpha=0.5)
plt.colorbar(scatter, label="Sharpe Ratio")
plt.xlabel("Volatility")
plt.ylabel("Annualized Return")
plt.title(f"Efficient Frontier: {scenarios:,} Simulated Portfolios", fontsize=14)

#We draw a red star on the winnder in order to highlight it
max_sharpe_ret = returns_array[index_max_sharpe]
max_sharpe_vol= volatility_array[index_max_sharpe]
plt.scatter(max_sharpe_vol, max_sharpe_ret, c="red", s=200, marker="*", label="Max Sharpe Ratio")
plt.legend(loc="upper left")



#Now we create the perfomance line chart assuming we invested 10k dollar using the optimal weights
initial_investment = 10000
portfolio_daily_returns = (stocks_return* optimal_weights).sum(axis=1)
cumulative_return= (1+portfolio_daily_returns).cumprod()
portfolio_value = cumulative_return * initial_investment

#Plotting

plt.figure(figsize=(12,6))
plt.plot(portfolio_value, label = "Max Sharpe Portfolio", color="green", linewidth=2)
plt.title("Performance of the Optimal Portfolio (10 years)", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Portfolio Value ($)")
plt.legend(loc="upper left")
plt.grid(True, alpha=0.3)

#Let's add a textbox with a final value

final_value = portfolio_value.iloc[-1]
total_return_pct = ((final_value / initial_investment) -1) * 100

plt.text(0.95, 0.05,
        f"Initial: ${initial_investment:,.0f}\nFinal:${final_value:,.2f}\nreturn: +{total_return_pct:.1f}%",
        fontsize=12, bbox=dict(facecolor="white", alpha=0.8),
        transform=plt.gca().transAxes, ha="right", va="bottom")

print("Displaying growth graph of the optimal portfolio over 10 years...")
plt.show()





