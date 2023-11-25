import pandas as pd
import yfinance as yf

from util.file_util import get_file_path


def load_stock_data(symbol, period, interval):
    # Download historical stock data
    stock_data = yf.download(symbol, period=period, interval=interval)

    stock_data.to_csv(get_file_path(symbol, "stock"))


def get_stock_data(symbol):
    stock_data = pd.read_csv(get_file_path(symbol, "stock"))
    return stock_data.to_string(index=False)
