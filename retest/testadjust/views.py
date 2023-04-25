from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


class Receive_data(APIView):
    def get(self,request):
        return JsonResponse({"status":"0","msg":"ok","data":"Reereer"})

