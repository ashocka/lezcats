from django.shortcuts import render
from django.http import HttpResponse

from lezapi.shadilo.shadilo import get_facebook_events


# Function-Based View
def index(request):
    events = get_facebook_events('page_id')
    return HttpResponse("Hello, world. You're at the index of your new Django app.")

