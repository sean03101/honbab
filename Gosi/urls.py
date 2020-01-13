from django.urls import path
from .views import main,main2,main3,create

app_name = "Gosi"

urlpatterns = [
    path('', main, name = "main"),
    path('input/',main3, name ="input"),
    path('create/',create, name ="create"),
]