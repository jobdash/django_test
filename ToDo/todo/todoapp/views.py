from django.shortcuts import render
from django.http import HttpResponse

# creating the view

def index(request):
    return HttpResponse('Hello JobDash, you are at Kelsey Jacobsen\'s ToDo app')
