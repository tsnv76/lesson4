import requests
import xmltodict
def currency_rates(valute):
    valute = valute.upper()
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    doc = xmltodict.parse(r.text)
    valute_exist = 0
    items = doc['ValCurs']['Valute']
    kurs_per_rub = '0'
    name = 0
    for item in items:
        if item['CharCode'] == valute:
            kurs_per_rub = item['Value'].replace(',', '.')
            valute_exist = 1
            name = item['Name']
    return kurs_per_rub, valute_exist, name
valute = ['eur', 'usd']
for val in valute:
    kurs, val_ex , name_val= currency_rates(val)
    if val_ex != 1:
        print('None')
    else:
        print(f'Курс рубля к {name_val}   --> {float(kurs):.2f}')
