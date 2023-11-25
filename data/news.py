import yfinance as yf

from util.file_util import get_file_path


def load_news_data(symbol):
    ticker = yf.Ticker(symbol)
    news = ticker.news
    with open(get_file_path(symbol, "news"), "w") as file:
        # Write each headline and URL to the file
        for item in news:
            file.write(f"Headline: {item['title']}\n")
            file.write(f"Link: {item['link']}\n")
            file.write("-" * 30 + "\n")


def get_news_data(symbol):
    # Open the file in read mode
    with open(get_file_path(symbol, "news"), "r") as file:
        # Read the content of the file
        return file.read()