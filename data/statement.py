import yfinance as yf
import pandas as pd

from util.file_util import get_file_path, file_exists

data_type = "statement"


def get_statement_data(symbol, period="q", live=True):
    if live:
        ticker = yf.Ticker(symbol)
        if period == 'q':
            statement_data = ticker.quarterly_income_stmt
        else:
            statement_data = ticker.income_stmt
        return statement_data.to_string()
    elif file_exists(symbol, data_type):
        statement_data = pd.read_csv(get_file_path(symbol, data_type))
        return statement_data.to_string()
    else:
        ticker = yf.Ticker(symbol)
        if period == 'q':
            statement_data = ticker.quarterly_income_stmt
        else:
            statement_data = ticker.income_stmt
        statement_data.to_csv(get_file_path(symbol, data_type))
        return statement_data.to_string()