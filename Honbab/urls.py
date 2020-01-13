from django.urls import path
from .views import resturant_like,index
from django.conf.urls import url

app_name = "Honbab"
urlpatterns = [
    url(r'^$', index, name='main'),
    url(r'^(?P<pk>\d+)/like/$', resturant_like, name='resturant_like'), 
]