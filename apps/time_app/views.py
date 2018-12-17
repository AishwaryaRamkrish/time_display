from django.shortcuts import render
from time import strftime, gmtime

def index(request):
    context = {
        'date': strftime('%b %d, %Y',gmtime()),
        'time': strftime('%I:%M %p',gmtime())

    }
    return render(request,'time_app/index.html',context)
