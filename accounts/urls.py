from django.urls import path
from django.conf.urls import url
from .views import login,logout,signup

app_name = "accounts"
urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]