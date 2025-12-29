import yfinance as yf
import matplotlib.pyplot as plt



#Select the stock you want to watch
ticker = "TSLA"  #It has to be the real ticker ofc
data= yf.download(ticker, start="2020-01-01")

#Let's create the Moving Average which is one of the basics of technical analysis

data["MA_20"]=data["Close"].rolling(window=20).mean()
data["MA_50"]=data["Close"].rolling(window=50).mean()
data["MA_200"]=data["Close"].rolling(window=200).mean()

#Now that we've extracted the stock data + having created the MA it's time to make the graph

plt.figure(figsize=(14,8))
plt.plot(data["Close"], label=f"{ticker} price", color="black", linewidth=3, alpha=0.5) 
plt.plot(data["MA_20"], label="(MA_20) trend", color="orange", linewidth=2, alpha=1)
plt.plot(data["MA_50"], label="(MA_50) trend", color="pink", linewidth=2, alpha=1)      
plt.plot(data["MA_200"],label="(MA_200) trend", color="yellow", linewidth=2, alpha=1)


plt.title((f"Financial trend analysis:{ticker}"))
plt.legend()
plt.grid()            #la grid puoi inserirla o meno


#Now that we made the graph we'd like to see it (seems fair does it?)
print(f"{ticker} graph incoming...")
plt.show()


