import pandas as pd
import yfinance as yf
import matplotlib as plp
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default="browser"   #We tell to python to open the interactive graph on our default browser


#USER IMPUT

print("---WELCOME IN YOUR FINANCIAL TERMINAL xD---")

ticker_input= input("Enter the Ticker you would like to see (e.g: TSLA, NVDA, AAPL):")
ticker=ticker_input.upper()


#We get the data

print(f"Downloading data for {ticker}...") 
data= yf.download(ticker, period="5y")


#yahoo ha cambiato i modi in cui si visualizzano i dati per cui dobbiamo aggiungere questa riga che dice a plotly come visualizzare i dati senno il povero plotly non sa che fare
if isinstance(data.columns, pd.MultiIndex):
    data.columns= data.columns.get_level_values(0)
    

#we make the moving averages

data["MA_20"]=data["Close"].rolling(window=20).mean()
data["MA_50"]=data["Close"].rolling(window=50).mean()
data["MA_100"]=data["Close"].rolling(window=100).mean()
data["MA_200"]=data["Close"].rolling(window=200).mean()
data=data.dropna()


#we cook the interactive graph

fig= go.Figure()

#Now we gotta add the price to this beauty

fig.add_trace(go.Scatter(
    x=data.index,
    y=data["Close"],
    name=f"{ticker} price",   #tornaci dopo
    line=dict(color="white", width=1),
    opacity=0.5 
))

#Now we set the moving averages

columns=["MA_20", "MA_50", "MA_100", "MA_200"]
colors=["orange", "yellow", "blue", "pink"]

#Now we actually add the moving averages to the graph

for column, color in zip(columns, colors):
    fig.add_trace(go.Scatter(
    x=data.index,
    y=data[column],
    name=column,
    line=dict(color=color, width=2)
))


#Now the cool interactive part 

fig.update_layout(
    title=f"{ticker} Interactive stock chart",
    hovermode="x unified", #it actually makes it possible for you to have the interactive data once you go with cursor on the MA
    template="plotly_dark", #dark theme which is very professional and "eastethic"
    xaxis_title= "Date",
    yaxis_title=("Price (USD)") #prova a rimuoverlo una volta che il codice ti va
)


#Now we wanna see the interactive graph

print(f"{ticker} interactive stock chart incoming....")
fig.show()


#FINAL REMINDER

print("/n" + "="*45)
print("---PROCESS SUCCESSFULLY FINISHED!---")
print(f"To analyze a new ticker just pla the code again")
print("="*45)





