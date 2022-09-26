import requests
import json
import math

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .utils import get_currency, str_to_bool

provider_key = "2016939750"

reservation_endpoint = {
  "prof" : "https://api-6yfe7nq4sq-uc.a.run.app/book",
  "team" : "http://server.aurelientorres.com/bookings/"
}

vol_endpoint = {
  "prof" : "https://api-6yfe7nq4sq-uc.a.run.app/flights",
  "team" : "http://server.aurelientorres.com/flights"
}

def build_vol(source, external_vol, currencies) :

  if  source == "prof" :
    montant = external_vol["base_price"]

    price_dict = {

    }

    for currency in currencies:
        price_dict[currency] = montant * float(currencies[currency])
    vol = {
                "code" : external_vol["code"],
                "depart" : external_vol["departure"],
                "arrive" : external_vol["arrival"],
                "montant" : external_vol["base_price"],
                "places" : external_vol["plane"]["total_seats"],
                "price_map" : price_dict,
                "source" : source
              }
    return vol
  else :
    montant = external_vol["price"]

    price_dict = {

    }

    for currency in currencies:
        price_dict[currency] = montant * float(currencies[currency])
    vol = {
                "code" : external_vol["internal_code"],
                "depart" : external_vol["departure"],
                "arrive" : external_vol["arrival"],
                "montant" : montant,
                "places" : external_vol["total_seats"],
                "price_map" : price_dict,
                "source" : external_vol["tenant"]
              }
    return vol

def build_booking(source, booking) :

  payload = {}

  if source == "prof":
    vols = json.loads(requests.get(vol_endpoint[source]).content.decode('utf-8'))
    vol = list(filter(lambda vol: vol["code"] == booking.get("code"), vols))

    champagne = str_to_bool(booking.get('champagne'))
    retour_inclut = str_to_bool(booking.get('retour_inclut'))
    first_class = str_to_bool(booking.get('first_class'))

    montant_vol = vol[0]["base_price"] * int(booking.get('nb_place'))

    if champagne : montant_vol += 100

    if first_class : montant_vol += montant_vol * 1.5

    if retour_inclut : montant_vol *= 1.95

    date = datetime.strptime(booking.get('date_depart'), "%Y-%m-%d")
    date_str = date.strftime("%d-%m-%Y")
    payload = {
      "code": "None",
      "flight": {
          "code": vol[0]["code"],
          "departure": vol[0]["departure"],
          "arrival": vol[0]["arrival"],
          "base_price": vol[0]["base_price"],
          "plane": {
              "name": vol[0]["plane"]["name"],
              "total_seats": vol[0]["plane"]["total_seats"]
          }
      },
      "date": date_str,
      "payed_price": int(montant_vol),
      "customer_name": booking.get('prenom') + " " + booking.get('nom'),
      "customer_nationality": "",
      "options": [],
      "booking_source": "GROUP2"
    }
  else :
    vols = json.loads(requests.get(vol_endpoint["team"]).content.decode('utf-8'))
    vol = list(filter(lambda vol: vol["internal_code"] == booking.get("code") and vol["tenant"] == source, vols))

    montant_vol = vol[0]["price"] * int(booking.get('nb_place'))

    if champagne : montant_vol += 100

    if first_class : montant_vol += montant_vol * 1.5

    if retour_inclut : montant_vol *= 1.95

    date = datetime.strptime(booking.get('date_depart'), "%Y-%m-%d")
    date_str = date.strftime("%d/%m/%Y")

    payload = {
      "provider_key": provider_key,
      "booking": {
        "total_price": montant_vol,
        "currency":
        {
            "currency_code": "EUR",
            "currency_name": "euro"
        },
        "tickets":
        [
            {
                "flight_code": vol["internal_code"],
                "person":
                {
                    "first_name": booking.get('prenom'),
                    "last_name" : booking.get('nom'),
                    "birth_date": "None"
                },
                "price": 0,
                "booking_date" : date_str,
                "option_codes": []
            }
        ]
      }
    }
  return payload

class ExternalVol(APIView):
    def get(self, request, format=None):

        currencies = get_currency()
        vols = []
        for endpoint in vol_endpoint :
          result = None
          try:
            result = requests.get(vol_endpoint[endpoint], verify=False, timeout=5)
          except :
            continue
          
          for external_vol in json.loads(result.content.decode('utf-8')):

            if "tenant" in external_vol and external_vol["tenant"] == "GROUP2" : continue
            vols.append(build_vol(endpoint, external_vol, currencies))
        
        return Response(vols)

    def post(self, request, format=None):
      source = "prof" if request.data.get("source") == "prof" else "team"

      result = None

      payload = build_booking(source, request.data)
        
      try :
        result = requests.post(self.reservation_endpoint[source], json = payload)
      except:
        result = "Something went wrong, booking failed."

      return Response(result)