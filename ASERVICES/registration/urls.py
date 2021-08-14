from django.urls import path
from registration import views
from django.conf.urls import url

app_name= 'registration'

urlpatterns = [
    url('professional/$', views.registration, name='Professional'),
]
