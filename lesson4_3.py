import requests
import xmltodict
from datetime import datetime
from urllib.request import urlopen
from xml.etree import ElementTree as etree
def currency_rates(val):
    val = val.upper()
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:
        end_val = etree.parse(r).findtext('.//Valute[CharCode="' + val + '"]/Value')
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:
        tree = etree.parse(r)
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:
        name_val = etree.parse(r).findtext('.//Valute[CharCode="' + val + '"]/Name')
    root = tree.getroot()
    val_d = root.attrib['Date']
    val_date = val_d
    return end_val, val_date, name_val
valute = input('Введите название валюты: ')
kurs, val_date, name_val= currency_rates(valute)
if kurs != None:
    kurs = kurs.replace(',', '.')
    print(f'Курс рубля к {name_val} на {val_date}  --> {float(kurs):.2f}')
else:
    print('None')
