import os

import requests
from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pandas as pd
from django.template.loader import render_to_string
from django.views.generic import TemplateView
import json

from .models import Crop_requirements
#from django.contrib.auth import User
from django.contrib.staticfiles.finders import find



from .templates_switcher import Contents
#data source: http://www.eldoret.climatemps.com/

def IndexView(request):
    file_path = "main/static/main/data/"
    colnames = ['month', 'maxTemp', 'minTemp', 'avgRainfall','avgTemp']
    climaticData = pd.read_csv(file_path+'climaticData.csv',names=colnames, skiprows=(1))
    months = climaticData['month'].tolist()
    maxTemp = climaticData['maxTemp'].tolist()
    minTemp = climaticData['minTemp'].tolist()
    avgRainfall=climaticData['avgRainfall'].tolist()
    avgTemp=climaticData['avgTemp'].tolist()
    return render(request, 'index.html',{'months':months,'maxTemp':maxTemp,'minTemp':minTemp,'avgRainfall':avgRainfall,'avgTemp':avgTemp})



#My Weather API key
#4d89ddd3a328f1b98c21646328fa9289

def AdvisoryView(request):
    crop_req = Crop_requirements.objects.all()
    return render(request,'advisory_pannel.html',{'crop_req':crop_req})


def ProductionStatsView(request):
    return render(request,'production_statistics.html',context=None)


def FarmerView(request):
    return render(request,'famers_dashboard.html',context=None)


def getLocation(request):
    if request.method=='POST' and request.is_ajax():
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('http://freegeoip.net/json/%s' % ip_address)
        request.session['geodata'] = response.json()
    return JsonResponse(response)



class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Jan", "Feb", "Mar", "Ap", "May", "Jun", "Jul","Aug","Sep","Oct","Nov","Dec"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

line_chart = TemplateView.as_view(template_name='index.html')



def TestPage(request):
    return render(request,'test.html', context=None)


def getData(request):
    data = {}
    if request.method=='POST' and request.is_ajax():  # os request.GET()
        get_value =request.POST.get('crop_name')
        data['result'] = 'You made a request to get '+get_value+ 'yield prediction'
    return JsonResponse(data)



