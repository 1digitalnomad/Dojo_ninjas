from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response='This is the books index.'
    return HttpResponse(response)