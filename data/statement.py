import yfinance as yf
import pandas as pd

from util.file_util import get_file_path


def load_statement_data(symbol, period):
    ticker = yf.Ticker(symbol)

    if period == 'q':
        stmt = ticker.quarterly_income_stmt
    else:
        stmt = ticker.income_stmt

    stmt.to_csv(get_file_path(symbol, "statement"))


def get_statement_data(symbol):
    statement_data = pd.read_csv(get_file_path(symbol, "statement"))
    return statement_data.to_string(index=False)