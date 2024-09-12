# nlp_processing.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english')) 

def preprocess_query(query):  # preprocess_query fonksiyonu tanımlanıyor
    tokens = word_tokenize(query.lower())  # query değişkeni küçük harfe çevirilip word_tokenize fonksiyonu ile tokenlere ayrılıyor
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]  # tokenlerin içindeki alfanumerik olmayanları ve stop_words içinde olanları filtreleniyor
    return filtered_tokens # filtrelenmiş tokenler döndürülüyor

def identify_intent(query_tokens):
    if "price" in query_tokens and "time" in query_tokens:
        return "time_price"
    elif 'price' in query_tokens:
        return 'price'
    elif 'summary' in query_tokens:
        return 'summary'
    
    else:
        return 'unknown'
