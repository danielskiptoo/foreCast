from django.shortcuts import render
from . import functions
import pandas as pd
import highcharts






def IndexView(request):
    colnames = ['Year', 'Temperature', 'Rainfall', 'maize_yield', 'wheat_yield']
    data = pd.read_csv('F:/kip stuffs/projects/foreCast/main/data/data.csv', names=colnames, skiprows=(1))
    years = data['Year'].tolist()
    maize_yield = data['maize_yield'].tolist()
    wheat_yield = data['wheat_yield'].tolist()
    #temperature =data['Temperature'].tolist()

    return render(request, 'index.html',{'data':years,'maize':maize_yield,'wheat':wheat_yield})
