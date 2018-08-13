import os

import requests
from chartjs.views.lines import BaseLineChartView
from django.http import HttpResponse, JsonResponse, request, HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView

from main.forms import FarmForm, ExpenseForm, ProductionForm
from .models import Farm, Crop_requirements, farm_production, csv_Data
from sklearn import datasets, linear_model
from pandas import DataFrame
import numpy as np
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

#from .models import Crop_requirements
#from django.contrib.auth import User
from django.contrib.staticfiles.finders import find
from .templates_switcher import Contents
#data source: http://www.eldoret.climatemps.com/


#global variables
file_path = "main/static/main/data/"
colnames = ['month', 'minTemp', 'maxTemp', 'avgTemp','avgRainfall']
maizePeriod= pd.read_csv(file_path+'maize.csv',names=colnames, skiprows=(1))
wheatPeriod=pd.read_csv(file_path+'wheat.csv',names=colnames, skiprows=(1))
CurrentClimate=pd.read_csv(file_path+'current.csv',names=colnames, skiprows=(1))

months = maizePeriod['month'].tolist()
maxTemp = maizePeriod['maxTemp'].tolist()
minTemp = maizePeriod['minTemp'].tolist()
avgRainfall=maizePeriod['avgRainfall'].tolist()
avgTemp=maizePeriod['avgTemp'].tolist()

def IndexView(request):
    months = maizePeriod['month'].tolist()
    maxTemp = maizePeriod['maxTemp'].tolist()
    minTemp = maizePeriod['minTemp'].tolist()
    avgRainfall=maizePeriod['avgRainfall'].tolist()
    avgTemp=maizePeriod['avgTemp'].tolist()
    crop_req = Crop_requirements.objects.all()
    return render(request, 'index.html',{'months':months,'maxTemp':maxTemp,'minTemp':minTemp,'avgRainfall':avgRainfall,'avgTemp':avgTemp, 'crop_req':crop_req})



#My Weather API key
#4d89ddd3a328f1b98c21646328fa9289

def AdvisoryView(request):
    crop_req = Crop_requirements.objects.all()
    return render(request,'advisory_pannel.html',{'crop_req':crop_req})


def ProductionStatsView(request):
    return render(request,'production_statistics.html',context=None)


def FarmerView(request):
    maize=[]
    wheat=[]
    maizeTotal=0
    wheatTotal=0
    MaizeFarm=Farm.objects.filter(type='wheat',farmer_id=request.user.id)
    for k in MaizeFarm:
        maize.append(k.size)
        r = list(map(int, maize))
        maizeTotal =sum(r)
    WheatFarm=Farm.objects.filter(type='maize',farmer_id=request.user.id)
    for s in WheatFarm:
        wheat.append(s.size)
        w=list(map(int, wheat))
        wheatTotal=sum(w)
    AllFarms=Farm.objects.filter(farmer_id=request.user.id)
    #FarmProduction=
    return render(request,'famers_dashboard.html', { 'wheatTotal':maizeTotal, 'maizeTotal':wheatTotal ,'AllFarms':AllFarms})


def getLocation(request):
    if request.method=='POST' and request.is_ajax():
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('http://freegeoip.net/json/%s' % ip_address)
        request.session['geodata'] = response.json()
    return JsonResponse(response)



def getData(request):
    data ={}
    global predicted_yield
    predictedYield=[]
    #regr = linear_model.LinearRegression()
    if request.method=='POST' and request.is_ajax():  # os request.GET()
        get_value =request.POST.get('crop_name')
        if get_value=='maize':
            #maize  prediction calculations
            avgRainfall =list(map(int,  maizePeriod['avgRainfall'].tolist()))
            temperatures=list(map(int,maizePeriod['avgTemp'].tolist()))
            rainfall=list(map(int,maizePeriod['avgRainfall'].tolist()))
            maize_produce=csv_Data.objects.filter(cropName='Maize')
            #current Climatic Conditions
            currentTemp = list(map(int,CurrentClimate['avgTemp'].tolist()))
            currentRain = list(map(int,CurrentClimate['avgRainfall'].tolist()))
            productions=[]
            for j in maize_produce:
                maxYield=int(j.maxCropYield)
                minYield=int(j.minCropYield)
                for m in range(minYield, maxYield):
                    productions = np.linspace(minYield, maxYield, num=9, endpoint=False)
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
            predictedYield = []
            for avgT, avgR in zip(currentTemp, currentRain):
                predicted = regr.predict([[avgT, avgR]])
                predictedYield.append(predicted)
            final=[l.tolist() for l in predictedYield]
            maxProduce = max(final)
            minProduce = min(final)
            data['maxProduce'] = maxProduce
            data['minProduce'] = minProduce
        data['temp'] = list(map(int, CurrentClimate['avgTemp'].tolist()))
        data['rain'] = list(map(int, CurrentClimate['avgRainfall'].tolist()))
        data['mintemp'] = list(map(int, CurrentClimate['minTemp'].tolist()))
        data['maxtemp'] = list(map(int, CurrentClimate['maxTemp'].tolist()))
        data['months']=maizePeriod['month'].tolist()

        if get_value=='wheat':
            #maize  prediction calculations
            temperatures=list(map(int,wheatPeriod['avgTemp'].tolist()))
            rainfall=list(map(int,wheatPeriod['avgRainfall'].tolist()))
            wheat_produce = csv_Data.objects.filter(cropName='Wheat')

            currentTemp = list(map(int, CurrentClimate['avgTemp'].tolist()))
            currentRain = list(map(int, CurrentClimate['avgRainfall'].tolist()))
            for z in wheat_produce:
                minYield=int(z.minCropYield)
                maxYield=int(z.maxCropYield)
            productions=[]

            productions = np.linspace(minYield, maxYield, num=8, endpoint=False)
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
            predictedYield=[]
            for avgT,avgR in zip(currentTemp,currentRain):
                predicted = regr.predict([[avgT, avgR]])
                predictedYield.append(predicted)

            final=[l.tolist() for l in predictedYield]
            maxProduce= max(final)
            minProduce=min(final)
            data['maxProduce'] =maxProduce
            data['minProduce']=minProduce
        print(data['rain'])
        print(data['rain'])
        print(data['rain'])

        data['temp'] = list(map(int, CurrentClimate['avgTemp'].tolist()))
        data['rain'] = list(map(int, CurrentClimate['avgRainfall'].tolist()))
        data['mintemp'] = list(map(int, CurrentClimate['minTemp'].tolist()))
        data['maxtemp'] = list(map(int, CurrentClimate['maxTemp'].tolist()))
        data['months'] = wheatPeriod['month'].tolist()


    return JsonResponse(data)

def AddFarm(request):
    # if request.method=='POST':
    return request

class CreateFarm(CreateView):
    form_class = FarmForm
    template_name = 'createFarm.html'
    success_url = '/farmer/addFarm'

    def form_valid(self, form):
        farmer = form.save(commit=False)
        user = User.objects.get(id=self.request.user.id)
        farmer.farmer= user # use your own profile here
        farmer.save()
        return super(CreateFarm, self).form_valid(form)

class AddExpense(CreateView):
    form_class =ExpenseForm
    template_name = 'newExpense.html'
    success_url = '/farmer/addExpense'

    def form_valid(self, form):
        expense = form.save(commit=False)
        user = User.objects.get(id=self.request.user.id)
        expense.farmer= user # use your own profile here
        expense.save()
        return super(AddExpense, self).form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(AddExpense, self).get_form(*args, **kwargs)
        form.fields['farm'].queryset = Farm.objects.filter(farmer=self.request.user.id)
        return form



class AddProduction(CreateView):
    form_class =ProductionForm
    template_name = 'addProduction.html'
    success_url = '/farmer/addProduction'

    def form_valid(self, form):
        production = form.save(commit=False)
        user = User.objects.get(id=self.request.user.id)
        production.farmer= user # use your own profile here
        production.save()
        return super(AddProduction, self).form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(AddProduction, self).get_form(*args, **kwargs)
        form.fields['farm'].queryset = Farm.objects.filter(farmer=self.request.user.id)
        return form
def getFarmHistorProduction(request):
    if request.method=='POST' and request.is_ajax():
        production=[]
        p=[]
        years=[]
        responseData={}
        farmId = request.POST.get('farm_id')
        farmProductions=farm_production.objects.filter(farm=farmId)
        for p in farmProductions:
            production.append(p.production_amount)
        for y in farmProductions:
            years.append(y.year)


        finalProduction = [float(i) for i in production]
        responseData['prod'] = finalProduction
        responseData['years']=years

    print(finalProduction)
    return JsonResponse(responseData)


#######################################################################################################
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




##########################################################################
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







