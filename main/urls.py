
from django.urls import path
from . import views
from .views import *

app_name='main'

urlpatterns = [
    path('',views.IndexView, name='index'),
    path('content',views.switch_html, name='farmer'),
    path('test',views.Heloo, name='test')


]