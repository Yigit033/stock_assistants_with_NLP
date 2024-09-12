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

from nlp_processing import preprocess_query, identify_intent
from response_generation import generate_response

def main():
  while True:
    user_input = input("Enter the stock symbol and the query you want:")
    if user_input.lower() == "q":
      print("See you soon!!")
      break
    elif user_input == "":
      print("Please enter a valid stock symbol")
      continue

    query_tokens = preprocess_query(user_input)
    intent = identify_intent(query_tokens)
    response = generate_response(intent, query_tokens)

    print(response)


if __name__ == "__main__":
  main()