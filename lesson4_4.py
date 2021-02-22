import requests
import xmltodict
from datetime import datetime
import utils
valute = input('Введите название валюты: ')
kurs, val_date, name_val= utils.currency_rates(valute)
if kurs != None:
    kurs = kurs.replace(',', '.')
    print(f'Курс рубля к {name_val} на {val_date}  --> {float(kurs):.2f}')
else:
    print('None')
