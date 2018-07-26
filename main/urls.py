
from django.urls import path
from . import views
from .views import *

app_name='main'

urlpatterns = [
    path('',views.IndexView, name='index'),
    path('farmer',views.FarmerView, name='farmer'),
    path('advisory',views.AdvisoryView, name='advisory-pannel'),
    path('production',views.ProductionStatsView, name='production-stats'),
    path('location',views.getLocation, name='location'),
    path('tempStats', views.LineChartJSONView.as_view()),
    path('test', views.TestPage, name='test'),
    path('getData',views.getData, name='regression'),



]