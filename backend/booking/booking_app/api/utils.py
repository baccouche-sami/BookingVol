from locale import currency
from django.db.models import Q

import xml.etree.ElementTree as ET
import requests

def get_currency() :

  result = requests.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')

  currencies = {}

  tree = ET.fromstring(result.content.decode('utf-8'))

  for currency in tree[2][0] :
    currencies[currency.attrib["currency"]] = currency.attrib["rate"]

  return currencies

def str_to_bool(value) :
  return str(value).lower() == 'true'

def custom_query(params):
  query = Q()

  for param in params :
      sub_query = Q()
      for value in params[param].split('|'):
          if value.lower() == 'true' or value.lower() == 'false' : value = str_to_bool(value)
          sub_query |= Q(**{'' + param : value})
      query &= sub_query
  return query
