from django.shortcuts import render

# Create your views here.
from .forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO = TopicForm()
    d = {'ETFO':ETFO}
    
    if request.method=='POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            
            # return HttpResponse('Topic inserted successfully!!!!!!!!')

            QLTO = Topic.objects.all()
            d = {'topics':QLTO}
            return render(request,'display_topic.html',d)
    
    return render(request,'insert_topic.html',d)




def insert_webpage(request):
    EWFO = WebpageForm()
    d = {'EWFO':EWFO}
    
    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            
            return HttpResponse('Webpage inserted successfulyy!!!!!!!')
    
    return render(request,'insert_webpage.html',d)




def insert_accessrecord(request):
    EARFO = AccessRecordForm()
    d = {'EARFO':EARFO}
    
    if request.method =='POST':
        ARFDO = AccessRecordForm(request.POST)
        if ARFDO.is_valid():
            ARFDO.save()
            
            return HttpResponse('<h2>Accessrecord data inserted successfully</h2>')
    
    return render(request,'insert_accessrecord.html',d)