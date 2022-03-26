from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, Http404
from gallery.models import Image
# from django.template import Template



# Create your views here.

def welcome(request):
    return render (request, 'welcome.html')


def imagedisplay(request):  
    resultsdisplay=Image.objects.all()
    return render(request,'all-gallery/image.html',{'image':resultsdisplay})  









