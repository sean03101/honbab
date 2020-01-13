from datetime import datetime
from django.utils.dateformat import DateFormat
from django.shortcuts import render,redirect
from .models import Gosi
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def main(request):
    context = {
         'Gosis' : Gosi.objects.all(),
         'Pyear' : datetime.today().year,
         'Pmonth' : datetime.today().month,
         'Pday' : datetime.today().day,

    }
    return render(request,'Gosi/gosis.html', context)

def main2(request):
    return render(request,'Gosi/main.html')

@staff_member_required
def main3(request):
    return render(request,'Gosi/input.html')

def create(request):
    if request.method == "POST":
        Gosiname = request.POST.get('Gosiname')
        
        morning = request.POST.get('morning')
        lunch = request.POST.get('lunch')
        dinner = request.POST.get('dinner')
        
        date = request.POST.get('date')
        
        Gosi.objects.create(Gosiname = Gosiname, morning = morning, lunch = lunch, dinner = dinner, date = date)
        
        return redirect('main')