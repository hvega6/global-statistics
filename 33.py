import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the tickers and the date range
def test_run():
    dates = pd.date_range("2010-01-01", "2012-12-31")
    symbols=[SPY, XOM, GOOG, GLD]
    df = get_data(symbols, dates)\
    plot_data(df)

    print df.std()

if __name__ == '__main__':
    test_run()