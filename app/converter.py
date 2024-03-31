import requests

def sync_converter(from_currency, to_currency, value):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    url = f'https://economia.awesomeapi.com.br/last/{from_currency}-{to_currency}'

    try:
        response = requests.get(url)
        data = response.json()
    except Exception as ex:
        print(ex)
        return None

    try:
        json_key = f'{from_currency}{to_currency}'.upper()
        ask = float(data[json_key]['ask'])
        bid = float(data[json_key]['bid'])
        cotacao_data = data[json_key]['create_date']
        total_ask = ask * value
        total_bid = bid * value
    except Exception as ex:
        print(ex)
        return None

    return {'Cotacao_de_para': data[json_key]['name'], 'Ask': ask, 'Bid': bid, 'Total_ask': total_ask, 'Total_bid': total_bid, 'Data_cotacao': cotacao_data}
