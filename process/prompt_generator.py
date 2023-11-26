from data import statement, info, news, stock


def generate_prompt(company_name, symbol, live):
    # Stock data
    stock_data = stock.get_stock_data(symbol, live=live)

    # Statement data
    statement_data = statement.get_statement_data(symbol, live=live)

    # Info data
    info_data = info.get_info_data(symbol, live=live)

    # News data
    news_data = news.get_news_data(symbol, live=live)

    return "Analyze below financial data for company " + \
           company_name + \
           " along with some other information like news. Suggest investment strategy for this company" + \
           "\nThese are financial statements:-\n" + statement_data + \
           "\nThis is stock data:-\n" + stock_data + \
           "\nThese are major holders:-\n" + info_data + \
           "\nThis is news data:-\n" + news_data + \
           "\nGive one statement final verdict for investing in this company."
