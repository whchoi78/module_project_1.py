from django.conf.urls import include, url
from django.contrib import admin
from airflow_test import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'airflow_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main),
]
