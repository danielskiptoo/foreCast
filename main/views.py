import os

import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pandas as pd
from django.template.loader import render_to_string
from .models import Crop_requirements
#from django.contrib.auth import User
from django.contrib.staticfiles.finders import find



from .templates_switcher import Contents


def IndexView(request):
    file_path = "main/static/main/data/"
    colnames = ['Year', 'Temperature', 'Rainfall', 'maize_yield', 'wheat_yield']
    data = pd.read_csv(file_path+'data.csv',names=colnames, skiprows=(1))
    years = data['Year'].tolist()
    maize_yield = data['maize_yield'].tolist()
    wheat_yield = data['wheat_yield'].tolist()



    #for t in mylist:
        #Mymodel(batch_cola=t[0], batch_colb=t[1],
                #batch_colc=t[2], batch_cold=t[3],
                #batch_cole=t[4]).save()
    #temperature =data['Temperature'].tolist()

    return render(request, 'index.html',{'years':years,'maize':maize_yield,'wheat':wheat_yield})



#My Weather API key
#4d89ddd3a328f1b98c21646328fa9289

def switch_html(request):

    if request.is_ajax():
        id_ = int(request.POST['id'])
        if id_==1:
            response =render_to_string('production_statistics.html',context=None)
        elif id_==2:
            response =render_to_string('famers_dashboard.html', context=None)
        elif id_==3:
            crop_req = Crop_requirements.objects.all()
            #response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=1.2921&lon=36.8219&APPID=4d89ddd3a328f1b98c21646328fa9289')
            #weather_data = response.json()
            response =render_to_string('advisory_pannel.html',{'crop_req':crop_req})

    return HttpResponse(response)

@login_required
def farmerPanel(request):
    if request.is_ajax():
        text=render_to_string('famers_dashboard.html', context=None)
    return HttpResponse(text)

def getLocation(request):
    if request.method=='POST' and request.is_ajax():
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('http://freegeoip.net/json/%s' % ip_address)
        request.session['geodata'] = response.json()
    return JsonResponse(response)