from multiprocessing import context
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def eventsView(request):
    context = {
        "title": "etikiti - Events"
    }
    
    return render(request, "events.html", context)