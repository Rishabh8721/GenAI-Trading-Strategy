import pandas as pd
import yfinance as yf

from util.file_util import get_file_path, file_exists

data_type = "stock"


def get_stock_data(symbol, period="3mo", interval="1wk", live=True):
    if live:
        stock_data = yf.download(symbol, period=period, interval=interval)
        return stock_data.to_string()
    elif file_exists(symbol, data_type):
        stock_data = pd.read_csv(get_file_path(symbol, data_type))
        return stock_data.to_string()
    else:
        stock_data = yf.download(symbol, period=period, interval=interval)
        stock_data.to_csv(get_file_path(symbol, data_type))
        return stock_data.to_string()