import os

import requests
from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pandas as pd
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from .models import Farm, Crop_requirements
from .forms import FarmForm
from sklearn import datasets, linear_model
from pandas import DataFrame
import numpy as np

#from .models import Crop_requirements
#from django.contrib.auth import User
from django.contrib.staticfiles.finders import find



from .templates_switcher import Contents
#data source: http://www.eldoret.climatemps.com/


#global variables
file_path = "main/static/main/data/"
colnames = ['month', 'maxTemp', 'minTemp', 'avgRainfall','avgTemp']
climaticData = pd.read_csv(file_path+'climaticData.csv',names=colnames, skiprows=(1))

def IndexView(request):
    months = climaticData['month'].tolist()
    maxTemp = climaticData['maxTemp'].tolist()
    minTemp = climaticData['minTemp'].tolist()
    avgRainfall=climaticData['avgRainfall'].tolist()
    avgTemp=climaticData['avgTemp'].tolist()
    return render(request, 'index.html',{'months':months,'maxTemp':maxTemp,'minTemp':minTemp,'avgRainfall':avgRainfall,'avgTemp':avgTemp})



#My Weather API key
#4d89ddd3a328f1b98c21646328fa9289

def AdvisoryView(request):
    #crop_req = Crop_requirements.objects.all()
    return render(request,'advisory_pannel.html',context=None)


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
    maize_requirements = Crop_requirements.objects.filter(crop_name='Wheat')
    wheat_expected_yield = 0
    temperatures = []
    rainfall = []
    productions = []
    for k in maize_requirements:
        maxTemp = int(k.temp_max)
        minTemp = int(k.temp_min)
        maxRainfall = int(k.max_rainfall)
        minRainfall = int(k.min_rainfall)
        minProduction = int(k.min_expected_acre)
        maxProduction = int(k.max_expected_acre)
        for temp in range(minTemp, maxTemp):
            temperatures = np.linspace(minTemp, maxTemp, num=10, endpoint=False)
        for rainfll in range(minRainfall, maxRainfall):
            rainfall = np.linspace(minRainfall, maxRainfall, num=10, endpoint=False)
        for production in range(minProduction, maxProduction):
            productions = np.linspace(minProduction, maxProduction, num=10, endpoint=False)
    Data = {
        'Temperature': temperatures,
        'Rainfall': rainfall,
        'Production': productions

    }
    df = DataFrame(Data, columns=['Temperature', 'Rainfall', 'Production'])
    X = df[['Temperature', 'Rainfall']].astype(float)
    Y = df['Production'].astype(float)
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)
    dat=regr.predict([[25, 900]])
    print(temperatures)
    print(rainfall)
    print(productions)
    return render(request,'test.html',{'tem':temperatures,'rnf':rainfall,'prdf':productions,'predicted':dat})


def getData(request):
    data = {}
    predictedYield=[]
    #regr = linear_model.LinearRegression()
    if request.method=='POST' and request.is_ajax():  # os request.GET()
        avgRainfall= climaticData['avgRainfall'].tolist()
        avgTemp= climaticData['avgTemp'].tolist()
        get_value =request.POST.get('crop_name')
        expected_yield=0

        if get_value=='maize':
            #maize  prediction calculations
            maize_requirements=Crop_requirements.objects.filter(crop_name='Maize')
            wheat_expected_yield=0
            temperatures=[]
            rainfall=[]
            productions=[]
            predictedYield=[]
            for k in maize_requirements:
                maxTemp = int(k.temp_max)
                minTemp = int(k.temp_min)
                maxRainfall = int(k.max_rainfall)
                minRainfall = int(k.min_rainfall)
                minProduction = int(k.min_expected_acre)
                maxProduction = int(k.max_expected_acre)
                for temp in range(minTemp, maxTemp):
                    temperatures = np.linspace(minTemp, maxTemp, num=10, endpoint=False)
                for rainfll in range(minRainfall, maxRainfall):
                    rainfall = np.linspace(minRainfall, maxRainfall, num=10, endpoint=False)
                for production in range(minProduction, maxProduction):
                    productions = np.linspace(minProduction, maxProduction, num=10, endpoint=False)
            Data = {
                'Temperature': temperatures,
                'Rainfall': rainfall,
                'Production': productions

            }
            df = DataFrame(Data, columns=['Temperature', 'Rainfall', 'Production'])
            X = df[['Temperature', 'Rainfall']].astype(float)
            Y = df['Production'].astype(float)
            regr = linear_model.LinearRegression()
            regr.fit(X, Y)
            for avgT,avgR in zip(avgRainfall,avgTemp):
                predicted = regr.predict([[avgT, avgR]])
                predictedYield.append(predicted)
        print(predictedYield)
        data['result'] = predictedYield



        if get_value=='wheat':
            #maize yield prediction
            maize_requirements = Crop_requirements.objects.filter(crop_name='Wheat')
            wheat_expected_yield = 0
            temperatures = []
            rainfall = []
            productions = []
            predictedYield=[]
            for k in maize_requirements:
                maxTemp = int(k.temp_max)
                minTemp = int(k.temp_min)
                maxRainfall = int(k.max_rainfall)
                minRainfall = int(k.min_rainfall)
                minProduction = int(k.min_expected_acre)
                maxProduction = int(k.max_expected_acre)
                for temp in range(minTemp, maxTemp):
                    temperatures = np.linspace(minTemp, maxTemp, num=10, endpoint=False)
                for rainfll in range(minRainfall, maxRainfall):
                    rainfall = np.linspace(minRainfall, maxRainfall, num=10, endpoint=False)
                for production in range(minProduction, maxProduction):
                    productions = np.linspace(minProduction, maxProduction, num=10, endpoint=False)
            Data = {
                'Temperature': temperatures,
                'Rainfall': rainfall,
                'Production': productions

            }
            df = DataFrame(Data, columns=['Temperature', 'Rainfall', 'Production'])
            X = df[['Temperature', 'Rainfall']].astype(float)
            Y = df['Production'].astype(float)
            regr = linear_model.LinearRegression()
            regr.fit(X, Y)
            for avgT,avgR in zip(avgRainfall,avgTemp):
                predicted = regr.predict([[avgT, avgR]])
                predictedYield.append(predicted)
        print(predictedYield)
        data['result']= predictedYield

    return JsonResponse(data)

def AddFarm(request):
    farm_form=FarmForm()
    # if request.method=='POST':
    return request




