import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, date2num
import numpy as np
from mpl_finance import candlestick_ohlc

start = datetime.datetime(2016, 1, 1)
end = datetime.date.today()
apple_stock = web.DataReader("AAPL", "yahoo", start, end)
google_stock = web.DataReader("GOOG", "yahoo", start, end)
microsoft_stock = web.DataReader("MSFT", "yahoo", start, end)

stocks = pd.DataFrame({"AAPL": apple_stock['Adj Close'],
                       'MSFT': microsoft_stock['Adj Close'],
                      'GOOG': google_stock['Adj Close']})

# stock_return = stocks.apply(lambda x: x / x[0])
# stock_return.plot(grid=True).axhline(y=1, color='k', lw=2)
stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1)))
stock_change.plot(grid=True).axhline(y=0, color='k', lw=2)
plt.show()


