"""Plot stock prices with a custom title and meaningful axis label"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    # Read Data
    ticker = 'SPY'
    start_date = '2010-04-01'
    end_date = '2012-07-31'
    
    # Fetch the stock data
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
    
    # Compute the 20-day rolling mean
    rolling_mean = data.rolling(window=20).mean()

    # Plot SPY data, retain matplotlib axis object
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data, label='SPY Price', color='blue')
    plt.plot(rolling_mean.index, rolling_mean, label='20-Day Rolling Mean', color='orange', linestyle='--')

    # Adding labels and title
    plt.title('SPY Stock Prices and 20-Day Rolling Mean (April 2010 - July 2012)')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    test_run()