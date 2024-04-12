import pandas as pd
import yfinance as yf
import datetime
import math
from plot import plot

df = pd.read_csv("data/russell2000.csv", usecols=['Ticker'])

russell_2000_list = []
bfd_data = []
bfd_occurences = []
bfd_natural = []


for index, row in df.iterrows():
    # Fetch data from 'Symbol' column in CSV column, and cast it to an int type
    russell_2000_list.append(df['Ticker'][index])
   
stock_data = yf.download(tickers = " ".join(russell_2000_list), period = "1d")
stock_data_close = stock_data['Close'].to_string(index=False, header=False).replace("\n", " ").split(" ")

for i in range(len(stock_data_close)):
    data = stock_data_close[i]
    sdc = data[:1]
    bfd_data.append(str(sdc))

for i in range(1, 10):
    # Get the amount of occurences of numbers 1 through 9 in the data, and turn it into a percent
    bfd_occurences.append(float(bfd_data.count(f'{i}')/len(bfd_data))*100)
    # Benford's law - log10 (i + 1) - log10 (i)
    bfd_log = (math.log10(i + 1) - math.log10(i)) * 100 
    bfd_natural.append(str(round(bfd_log, 2)).split())


plot (
    bfd_natural, 
    bfd_occurences, 
    f"Russell 2000 Component Closing Prices of { datetime.date.today().strftime('%Y-%m-%d') }", 
    "Russell 2000 Component Closing Prices", 
    "russell2000.png"
)
