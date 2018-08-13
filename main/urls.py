
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('',views.IndexView, name='index'),
    path('farmer',views.FarmerView, name='farmer'),
    path('advisory',views.AdvisoryView, name='advisory-pannel'),
    path('production',views.ProductionStatsView, name='production-stats'),
    path('location',views.getLocation, name='location'),
    path('tempStats', views.LineChartJSONView.as_view()),
    path('test', views.TestPage, name='test'),
    path('main/getData',views.getData, name='regression'),
    path('getFarmProductions',views.getFarmHistorProduction, name='farm-productions'),
    path('farmer/addFarm', views.CreateFarm.as_view(), name='add_farm'),
    path('farmer/addExpense', views.AddExpense.as_view(), name='add_expense'),
    path('farmer/addProduction', views.AddProduction.as_view(), name='add_production'),


]