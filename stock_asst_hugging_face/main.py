# # app.py
# from flask import Flask, request, jsonify
# from nlp_processing import preprocess_query, identify_intent
# from response_generation import generate_response

# app = Flask(__name__)

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_query = request.json.get('query')
#     if not user_query:
#         return jsonify({'response': "Please provide a query."})

#     query_tokens = preprocess_query(user_query)
#     intent = identify_intent(query_tokens)
#     response = generate_response(intent, query_tokens)
    
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)


# from nlp_processing import preprocess_query, identify_intent
from response_generation import generate_response, generator

def main():
    while True:
        user_query = input("Enter your stock (type 'q' to quit): ")
        if user_query.lower() == 'q':
            print("Goodbye!")
            break
        elif user_query.lower() == "":
            print("you pushed the enter, so type a stock symboll! ")
            continue

# Not => query tokens : sorgu belirteçleri veya sorgu tokenleri

        query_tokens = generator(user_query)
        intent = generator(query_tokens)
        response = generate_response(intent, query_tokens)
        
        print(response)

if __name__ == '__main__':
    main()


