from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

def home(request):
    data= {}
    return render(request, 'website/home.html', data)