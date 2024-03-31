from flask import Flask, request, jsonify
import asyncio
from app.converter import async_converter

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/cotacoes-moedas/')
async def cotacoes_moedas():
    from_currency = request.args.get('from_currency')
    to_currencies = request.args.get('to_currencies')
    value = float(request.args.get('value'))

    to_currencies = to_currencies.split(',')

    # Lista para armazenar as corotinas
    coroutines = []

    # Criando as corotinas para cada moeda de destino
    for currency in to_currencies:
        coro = async_converter(from_currency=from_currency, to_currency=currency, value=value)
        coroutines.append(coro)

    # Aguardando todas as corotinas
    results = await asyncio.gather(*coroutines)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)