from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def basictemp(request):

    return render(request,"basic.html")

