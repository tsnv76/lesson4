import requests
import xmltodict
from datetime import datetime
import sys
import utils
if len(sys.argv) > 1:
    filename, valute = sys.argv
else:
    valute = input('Введите название валюты: ')
kurs, val_date, name_val= utils.currency_rates(valute)
if kurs != None:
    kurs = kurs.replace(',', '.')
    print(f'Курс рубля к {name_val} на {val_date}  --> {float(kurs):.2f}')
else:
    print('None')
