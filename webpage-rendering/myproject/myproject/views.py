from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request,"login.html")


def registration(request):
    return render(request,"registration.html")

def dashboard(request):
    return render(request,"dashboard.html")