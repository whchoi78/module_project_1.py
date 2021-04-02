from django.shortcuts import render
from airflow_test.models import *

def main(request):
    info = MwTable.objects.values('weather_time','dist','temp_max','temp_min','weather_sky','rnst')
    context = {"weather":info}
    
    
    return render(request, "myhtml/index.html",context)
    