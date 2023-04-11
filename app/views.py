from django.shortcuts import render

# Create your views here.
from app.models import * 

from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topic_name = ' )
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    return HttpResponse('topic_name inserted successfully ')

def insert_webpage(request):
    tn=input('enter topic_name= ')
    n=input('enter name= ')
    ul=input('enter url= ')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wp=Webpage.objects.get_or_create(topic_name=To,name=n,url=ul)[0]

    Wp.save()
     
    return HttpResponse('inserted into webpagesuccessfully ')


def Display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'Display_Topic.html',d)


def Display_webpage(request):
    WOT=Webpage.objects.all()
    d={'webs':WOT}
    return render(request,'Display_webpage.html',d)

def Display_AccessRecord(request):
    AOT=AccessRecord.objects.all()
    d={'aecs':AOT}
    return render(request,'Display_AcRs.html',d)
