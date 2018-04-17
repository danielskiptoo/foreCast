import os

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from django.template.loader import render_to_string
from django.contrib.staticfiles.finders import find



from .templates_switcher import Contents




def IndexView(request):
    file_path = "main/static/main/data/"
    colnames = ['Year', 'Temperature', 'Rainfall', 'maize_yield', 'wheat_yield']
    data = pd.read_csv(file_path+'data.csv',names=colnames, skiprows=(1))
    years = data['Year'].tolist()
    maize_yield = data['maize_yield'].tolist()
    wheat_yield = data['wheat_yield'].tolist()
    #temperature =data['Temperature'].tolist()

    return render(request, 'index.html',{'years':years,'maize':maize_yield,'wheat':wheat_yield})




def switch_html(request):

    if request.is_ajax():
        id_ = request.POST['id']
        response = 'helooooo'
        if id_==1:
            response =render_to_string('production_statistics.html',context=None)
        elif id_==2:
            response =render_to_string('famers_dashboard.html', context=None)
        elif id_==3:
            response =render_to_string('advisory_pannel.html', context=None)

    return HttpResponse(response)

def Heloo(request):
    if request.is_ajax():
        text="Heloo there. This is another test"
    return HttpResponse(text)