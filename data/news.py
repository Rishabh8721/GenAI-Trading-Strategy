import yfinance as yf

from util.file_util import get_file_path, file_exists

data_type = "news"


def get_news_data(symbol, live=True):
    if live:
        ticker = yf.Ticker(symbol)
        news = ticker.news
        news_data = ""
        for item in news:
            news_data = news_data + "Headline: " + str(item['title']) + "\n" + "Publish Time: " + str(
                item['providerPublishTime']) + "\n" + "Link: " + str(item['link']) + "\n\n"
        return news_data
    elif file_exists(symbol, data_type):
        with open(get_file_path(symbol, "news"), "r") as file:
            return file.read()
    else:
        ticker = yf.Ticker(symbol)
        news = ticker.news
        news_data = ""
        for item in news:
            news_data = news_data + "Headline: " + str(item['title']) + "\n" + "Publish Timestamp: " + str(
                item['providerPublishTime']) + "\n" + "Link: " + str(item['link']) + "\n\n"

        text_file = open(get_file_path(symbol, "news"), "w")
        text_file.write(news_data)
        text_file.close()
        return news_data

