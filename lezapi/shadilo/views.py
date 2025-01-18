from django.shortcuts import render
from django.http import HttpResponse


# Function-Based View
def index(request):
    return HttpResponse("Hello, world. You're at the index of your new Django app.")

