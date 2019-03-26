from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import workout


def home(request):
    if request.method == 'POST':
        pushups_home=request.POST.get('pushups')
        situps_home=request.POST.get('situps')
        name_home=request.POST.get('name')
        c = workout(pushups=pushups_home,situps=situps_home,name=name_home,date=datetime.datetime.now().strftime("%x"))
        c.save()
        return render(request, 'front_end/index.html')
    else:
        return render(request, 'front_end/index.html')

def about(request):
    return render(request, 'front_end/about.html')