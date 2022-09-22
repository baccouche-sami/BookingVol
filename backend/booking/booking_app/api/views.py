import requests
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.vol import Vol
from datetime import datetime


class ExternalVol(APIView):

    def get(self, request, format=None):
        result = requests.get('https://api-6yfe7nq4sq-uc.a.run.app/flights')
        vols = []
        for external_vol in json.loads(result.content.decode('utf-8')):
            vol = {
              "code" : external_vol["code"],
              "depart" : external_vol["departure"],
              "arrive" : external_vol["arrival"],
              "montant" : external_vol["base_price"],
              "places" : external_vol["plane"]["total_seats"],

            }
            
            vols.append(vol)
        
        return Response(vols)

    def post(self, request, format=None):
      vols = json.loads(requests.get('https://api-6yfe7nq4sq-uc.a.run.app/flights').content.decode('utf-8'))
      vol = list(filter(lambda vol: vol["code"] == request.data.get("code"), vols))

      date = datetime.strptime(request.data.get('date_depart'), "%Y-%m-%dT%H:%M:%SZ")
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
        "payed_price": request.data.get('montant'),
        "customer_name": request.data.get('prenom') + " " + request.data.get('nom'),
        "customer_nationality": "",
        "options": [],
        "booking_source": "BookingVol"
      }
      
      result = requests.post('https://api-6yfe7nq4sq-uc.a.run.app/book', json = payload)

      return Response(result)