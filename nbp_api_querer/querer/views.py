from django.shortcuts import render
from rest_framework.views import APIView  
from django.http import JsonResponse, HttpResponse
import re
import requests
from workalendar.europe import Poland
from datetime import datetime

class AverageRate(APIView):  
    def get(self, request, *args, **kwargs):
        # check if date is in correct format
        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{kwargs['currency']}/{kwargs['date']}/?format=json"

        if not re.match(r'^\d{4}-\d{2}-\d{2}$', kwargs['date']):
            return HttpResponse("Date format should be YYYY-MM-DD")
        response=requests.get(url)

        # check if date is a working day
        cal = Poland()
        try:
            if not cal.is_working_day(datetime.strptime(kwargs['date'], '%Y-%m-%d')):
                return HttpResponse("Date is not a working day")
        except:
            return HttpResponse("Invalid date format. Should be YYYY-MM-DD")

        # check if date is in range

        try:
            response = response.json()
        except:
            return HttpResponse("Invalid currency code or date is out of range")
        
        return HttpResponse(response['rates'][0]['mid'])
       
 
class MinMaxAverage(APIView):
    def get(self, request, format=JsonResponse, *args, **kwargs):
        if kwargs['N'] > 255:
            return HttpResponse("Maximal value of last days (N) is 255")

        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{kwargs['currency']}/last/{kwargs['N']}/?format=json"
        response = requests.get(url)
        try:
            response = response.json()
        except:
            return HttpResponse("Invalid currency code")
        
        mids = [rate['mid'] for rate in response['rates']]
        return JsonResponse({"min": min(mids), "max": max(mids)})


class Difference(APIView):
    def get(self, request, format=JsonResponse, *args, **kwargs):
        if kwargs['N'] > 255:
            return HttpResponse("Maximal value of last days (N) is 255")
        url = f"http://api.nbp.pl/api/exchangerates/rates/c/{kwargs['currency']}/last/{kwargs['N']}/?format=json"
        response = requests.get(url)
        try:
            response = response.json()
        except:
            return HttpResponse("Invalid currency code")
        
        differences = [rate['ask'] - rate['bid'] for rate in response['rates']]
        return JsonResponse({"max_diff": round(max(differences),4)})
       

