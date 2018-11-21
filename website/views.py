from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

def home(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    data= {}
    data['transacoes']=['t1', 't2', 't3']
    data['now']=datetime.datetime.now()
    return render(request, 'website/home.html', data)