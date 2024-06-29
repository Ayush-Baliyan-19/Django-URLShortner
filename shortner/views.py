from os import link
from django.shortcuts import render
import uuid
from .models import URL
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        link = request.POST['link']
        shortened_link = request.POST['shortened_link']
        print(link)
        newUrl = URL(link=link, uuid=shortened_link)
        newUrl.save()
        return HttpResponse(shortened_link)
def redirector(request, query):
    url_details = URL.objects.get(uuid=query)
    print(url_details.link)
    return HttpResponse(url_details.link)