from django.shortcuts import render
from rest_framework.views import APIView  
from django.http import JsonResponse  

class MainPage(APIView):  

 def get(self, request, format=None):
    return JsonResponse({"message":
    'HELLO WORLD FROM DJANGO AND DOCKER'})  
