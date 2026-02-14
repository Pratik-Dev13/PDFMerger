from django.contrib import admin
from django.urls import path
from merger.views import *

urlpatterns = [
    path('pdf-merger/',merger)
    
]