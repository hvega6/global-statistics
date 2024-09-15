import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the tickers and the date range
tickers = ['SPY', 'XOM', 'GOOG', 'GLD']
start_date = '2010-04-01'
end_date = '2012-07-31'

# Fetch the stock data
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Calculate the 20-day rolling median and standard deviation
rolling_median = data.rolling(window=20).median()
rolling_std = data.rolling(window=20).std()

# Calculate the upper and lower sigma lines (2 sigma)
upper_sigma = rolling_median + 2 * rolling_std
lower_sigma = rolling_median - 2 * rolling_std

# Display the data as a table
print("Stock Prices from April 2010 to July 2012:")
print(data)

# Plotting the stock prices, rolling median, and sigma lines
plt.figure(figsize=(12, 6))
for ticker in tickers:
    plt.plot(data.index, data[ticker], label=f'{ticker} Price')
    plt.plot(rolling_median.index, rolling_median[ticker], label=f'{ticker} 20-Day Rolling Median', linestyle='--')
    plt.plot(upper_sigma.index, upper_sigma[ticker], label=f'{ticker} Upper 2 Sigma', linestyle=':', color='orange')
    plt.plot(lower_sigma.index, lower_sigma[ticker], label=f'{ticker} Lower 2 Sigma', linestyle=':', color='orange')

# Set the limits for the y-axis
plt.ylim(0, 800)

# Adding labels and title
plt.title('Stock Prices, 20-Day Rolling Median, and 2 Sigma Lines from April 2010 to July 2012')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
