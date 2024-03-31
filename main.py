from flask import Flask, request, jsonify
from app.converter import sync_converter

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/cotacoes-moedas/')
def cotacoes_moedas():
    from_currency = request.args.get('from_currency')
    to_currencies = request.args.get('to_currencies')
    value = float(request.args.get('value'))

    to_currencies = to_currencies.split(',')
    
    results = []

    for currency in to_currencies:
        response = sync_converter(from_currency=from_currency, to_currency=currency, value=value)
        results.append(response)
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)