from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    context = {
        'count' : request.session['counter'],
        'rand_word': get_random_string(length = 14, allowed_chars ='ABCDEFGHaeiouUVWXYZ')
    }
    return render(request,'random_word/index.html',context)

def generate(request):
    # if request.method == "POST":
    return redirect('/random_word')

def reset(request):
    del request.session['counter']
    return redirect('/random_word')