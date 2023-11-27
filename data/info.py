import yfinance as yf

from util.file_util import get_file_path, file_exists

data_type = "info"


def get_info_data(symbol, live=True):
    if live:
        ticker = yf.Ticker(symbol)
        info_data = ticker.info
        return str(info_data)
    elif file_exists(symbol, data_type, "txt"):
        with open(get_file_path(symbol, data_type, "txt"), "r") as file:
            return file.read()
    else:
        ticker = yf.Ticker(symbol)
        info_data = ticker.info
        text_file = open(get_file_path(symbol, data_type, "txt"), "w")
        text_file.write(str(info_data))
        text_file.close()
        return str(info_data)