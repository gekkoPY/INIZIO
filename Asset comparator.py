import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import yfinance as yf

#Where will the output be shown? In your default browser

pio.renderers.default = "browser"

#inputs the user will insert

print("---Welcome to your asset comparator!---")
ticker1 =input("Please enter the first ticker you'd like to compare").upper()
ticker2= input("Please enter the secondi ticker you'd like to compare").upper()
benchmark_ticker = "^GSPC"  #of course the sp500 will be the benchmarket. Will your asset beat the market?

#Getting data

print(f"Downloading data for {ticker1}, {ticker2}, and sp500")
data1= yf.download(ticker1, period="4y") ["Close"]
data2= yf.download(ticker2, period="4y") ["Close"]
benchmark_data = yf.download(benchmark_ticker, period="4y") ["Close"]


#Cleaning data

def force_series(df):
    if isinstance(df,pd.DataFrame):
        df= df.iloc[:, 0]
    return(df)
    
        
data1= force_series(data1)
data2= force_series(data2)
benchmark_data=force_series(benchmark_data)


data1=data1.dropna()
data2=data2.dropna()
benchmark_data=benchmark_data.dropna()

    
#Calculate comulative returns

growth1= (data1/data1.iloc[0]-1)*100
growth2= (data2/data2.iloc[0]-1)*100
benchmark_growth= (benchmark_data/benchmark_data.iloc[0]-1)*100
    

#Chart creation

fig= go.Figure()

fig.add_trace(go.Scatter(x=growth1.index, y=growth1, name=f"growth of {ticker1}", line=dict(color="orange", width=2)))
fig.add_trace(go.Scatter(x=growth2.index, y=growth2, name=f"growth of {ticker2}", line=dict(color="blue", width=2)))
fig.add_trace(go.Scatter(x=benchmark_growth.index, y=benchmark_growth, name=f"growth of the market", line=dict(color="white", width=1, dash="dash"), opacity=1))

#Layout

fig.update_layout(
    title=f"Comparison between {ticker1}, {ticker2} and the market!",
    template="plotly_dark",
    yaxis_title="Cumulative_return(%)",
    hovermode="x unified",
)
    



#Display

print(f"Opening chart comparison into your browser")
fig.show()


#Final reminder for the user

print("\n" + "="*45)
print("---Analysis completed!---")
print("---Remember to press play in order to make other comparisons!---")
print("="*45)

