import yfinance as yf
from util.file_util import get_file_path, file_exists
import requests
from bs4 import BeautifulSoup

data_type = "news"


def get_news_data(symbol, detailed=False, live=True):
    if live:
        ticker = yf.Ticker(symbol)
        news = ticker.news
        news_data = ""
        for item in news:
            if detailed:
                news_data = news_data + _get_detailed_news(item) + "\n\n"
            else:
                news_data = news_data + "Headline: " + str(item['title']) + "\n" + "Publish Time: " + str(
                    item['providerPublishTime']) + "\n" + "Link: " + str(item['link']) + "\n\n"
        return news_data
    elif file_exists(symbol, data_type, "txt"):
        with open(get_file_path(symbol, data_type, "txt"), "r") as file:
            return file.read()
    else:
        ticker = yf.Ticker(symbol)
        news = ticker.news
        news_data = ""
        for item in news:
            if detailed:
                news_data = news_data + _get_detailed_news(item) + "\n\n"
            else:
                news_data = news_data + "Headline: " + str(item['title']) + "\n" + "Publish Timestamp: " + str(
                    item['providerPublishTime']) + "\n" + "Link: " + str(item['link']) + "\n\n"

        text_file = open(get_file_path(symbol, data_type, "txt"), "w")
        text_file.write(news_data)
        text_file.close()
        return news_data


def _get_detailed_news(item):
    output_data = "Headline: " + str(item['title']) + "\nTimestamp: " + str(
        item['providerPublishTime'])

    url = str(item['link'])
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        article_content = soup.find('div', class_='caas-body')
        if article_content:
            output_data = output_data + "\nSummary:-\n" + article_content.get_text(separator='\n').replace('\n', '')

    return output_data
