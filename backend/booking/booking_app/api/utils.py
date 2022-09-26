from django.db.models import Q
from ..models.vol import Vol

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


def post_service():
  vols_internes = Vol.objects.all()

  vols = {
    "provider_key" : "KEY_GROUP2",
    "flights" : []
  }
  
  for vol_interne in vols_internes:
    vol = {
      "tenant" : "BookingVol",
      "departure": vol_interne.depart,
      "arrival": vol_interne.arrive,
      "internal_code": vol_interne.id,
      "available_options": [
      
      ],
      "stop_overs": [
      
      ],
      "total_seats": vol_interne.places,
      "price": vol_interne.montant
    }

    vols["flights"].append(vol)

  try : 
    result = requests.post('http://10.8.111.81:8000/flights', json = vols)
    print(result)
  except :
    return

post_service()