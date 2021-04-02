from django.contrib import admin
from airflow_test.models import MwTable

class MwTableView(admin.ModelAdmin):
    list_display=('weather_time', 'dist', 'temp_max', 'temp_min', 'weather_sky', 'rnst')
            
admin.site.register(MwTable, MwTableView)