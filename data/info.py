import yfinance as yf
import pandas as pd

from util.file_util import get_file_path, file_exists

data_type = "info"


def get_info_data(symbol, live=True):
    if live:
        ticker = yf.Ticker(symbol)
        info_data = ticker.major_holders
        return info_data.to_string(index=False)
    elif file_exists(symbol, data_type):
        info_data = pd.read_csv(get_file_path(symbol, data_type))
        return info_data.to_string(index=False)
    else:
        ticker = yf.Ticker(symbol)
        info_data = ticker.major_holders
        info_data.to_csv(get_file_path(symbol, data_type))
        return info_data.to_string(index=False)