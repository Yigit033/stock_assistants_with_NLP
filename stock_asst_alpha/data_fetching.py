# data_fetching.py
import requests

API_KEY = 'TFQ16MMXKY2T8IG6'  # Replace with your actual API key

def get_stock_price(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    if 'Time Series (1min)' in data:
        latest_timestamp = sorted(data['Time Series (1min)'].keys())[-1]
        latest_close = data['Time Series (1min)'][latest_timestamp]['4. close']
        return float(latest_close)
    else:
        return None

def get_stock_summary(ticker):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    summary = {
        'name': data.get('Name', 'N/A'),
        'sector': data.get('Sector', 'N/A'),
        'industry': data.get('Industry', 'N/A'),
        'market_cap': data.get('MarketCapitalization', 'N/A'),
        'beta': data.get('Beta', 'N/A'),
        'pe_ratio': data.get('PERatio', 'N/A'),
    }
    return summary
