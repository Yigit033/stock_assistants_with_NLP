# nlp_processing.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_query(query):
    tokens = word_tokenize(query.lower())     
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_tokens

def identify_intent(query_tokens):
    if 'price' in query_tokens:
        return 'price'
    elif 'summary' in query_tokens:
        return 'summary'
    else:
        return 'unknown'
