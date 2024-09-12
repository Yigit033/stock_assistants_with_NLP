# response_generation.py
from data_fetching import get_stock_price, get_stock_summary, get_stock_time

def generate_response(intent, query_tokens):

    ticker = query_tokens[-1].upper()  # Assuming the ticker is the last token

    if intent == "time_price": # hatayı anladım, nlp_processing.py deki identify_intent fonsiyonun önceliği var o yüzden orada return edileni buraya yazdım!!!
        time = get_stock_time(ticker)
        price = get_stock_price(ticker)
        return f"The time and the price of the latest data for {ticker} is {time} and ${price}."

    elif intent == 'price':
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

# NOT => buradaki responseleri nlp_processing.py deki süreçleri oluşturarak kurabilirsin yani nlp ile girilen bir sözcüğün, rakammın 
# veya sembolün falan anlamlı bir şekilde süzgeçten geçirdikten sonra oluşacak sonuçları bu response_generation.py da fonksiyonlar kurarak mantıklı cevaplar veririsin 
# böylelikle hem NLP(natural language process) hem de fonksiyonları daha iyi anlamış oluyorsun !
# Kullanıcıya da bir chatbot oluşturmuş oluyoruz!!!!