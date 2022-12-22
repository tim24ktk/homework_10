from requests import get


def get_currency(value):
    resp = get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    if value.upper() in resp['Valute']:
        result = resp['Valute'][value.upper()]['Value']
        date = resp["Date"][:resp["Date"].find('T')]

        return f'Курс {value.upper()}  к рублю ЦБ РФ на {date}: 1{value.upper()} = {result} руб.'
    else:
        return 'Вы ввели неверную валюту! Попробуйте снова!'
