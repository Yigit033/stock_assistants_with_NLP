# data_fetching.py
import yfinance as yf

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        stock_period = stock.history(period="1d")
        if not stock_period.empty:
            latest_close = stock_period["Close"].iloc[-1]  # iloc[-1] => get the last row of the dataframe
            return latest_close
        else:
            return None, None
    except Exception as e:
        return e
    
def get_stock_time(ticker):
    try:
        stock = yf.Ticker(ticker)
        stock_period = stock.history(period="1d")
        if not stock_period.empty:
            latest_data = stock_period.iloc[-1]   # get the last row of the dataframe
            latest_timestamp = latest_data.name  # get the timestamp of the last row
            return latest_timestamp
        else:
            return None
    except Exception as e:
        return e
def get_stock_summary(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    summary = {
        'name': stock_info.get('shortName', 'N/A'),
        'sector': stock_info.get('sector', 'N/A'),
        'industry': stock_info.get('industry', 'N/A'),
        'market_cap': stock_info.get('marketCap', 'N/A'),
        'beta': stock_info.get('beta', 'N/A'),
        'pe_ratio': stock_info.get('trailingPE', 'N/A'),
    }
    return summary

# print(get_stock_price(ticker="AAPL"))  working correct
# print(get_stock_summary(ticker="AAPL"))   working correct
# print(get_stock_time(ticker="AAPL"))