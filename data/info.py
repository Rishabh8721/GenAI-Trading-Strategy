import yfinance as yf
import pandas as pd

from util.file_util import get_file_path


def load_info_data(symbol):
    ticker = yf.Ticker(symbol)

    info_data = ticker.major_holders

    # Save the data to a CSV file
    info_data.to_csv(get_file_path(symbol, "info"))


def get_info_data(symbol):
    info_data = pd.read_csv(get_file_path(symbol, "info"))
    text_data = info_data.to_string(index=False)
    return text_data

