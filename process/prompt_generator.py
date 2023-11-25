from data import statement, info, news, stock


def generate_prompt(company_name, symbol):
    # Stock data
    stock.load_stock_data(symbol, "3mo", "1wk")
    stock_data = stock.get_stock_data(symbol)

    # Statement data
    statement.load_statement_data(symbol, "q")
    statement_data = statement.get_statement_data(symbol)

    # Info data
    info.load_info_data(symbol)
    info_data = info.get_info_data(symbol)

    # News data
    news.load_news_data(symbol)
    news_data = news.get_news_data(symbol)

    return "Analyze below financial data for company " + \
           company_name + \
           " along with some other information like news. Suggest investment strategy for this company" + \
           "\nThese are financial statements:-\n" + statement_data + \
           "\nThis is stock data:-\n" + stock_data + \
           "\nThese are major holders:-\n" + info_data + \
           "\nThis is news data:-\n" + news_data + \
           "\nGive one statement final verdict for investing in this company."
