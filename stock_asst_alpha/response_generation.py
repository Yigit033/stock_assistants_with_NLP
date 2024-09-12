# response_generation.py
from data_fetching import get_stock_price, get_stock_summary

def generate_response(intent, query_tokens):
    ticker = query_tokens[-1].upper()  # Assuming the ticker is the last token
    if intent == 'price':
        price = get_stock_price(ticker)
        if price:
            return f"The latest price of {ticker} is ${price:.2f}."
        else:
            return f"Could not fetch the price for {ticker}."
    elif intent == 'summary':
        summary = get_stock_summary(ticker)
        return (f"Stock: {summary['name']}\n"
                f"Sector: {summary['sector']}\n"
                f"Industry: {summary['industry']}\n"
                f"Market Cap: {summary['market_cap']}\n"
                f"Beta: {summary['beta']}\n"
                f"P/E Ratio: {summary['pe_ratio']}")
    else:
        return "Sorry, I didn't understand that. Please ask about the price or summary of a stock."
