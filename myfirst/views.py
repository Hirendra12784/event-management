from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse

from myfirst.models import eventadd
# Create your views here.

def home(request):
    return render(request,"home.html")
def insert(request):   #for adding events
    if request.method=="POST":
        if request.POST.get('edate') and request.POST.get('ename') and request.POST.get('etype'):
            saver=eventadd()
            saver.edate=request.POST.get('edate')
            saver.ename=request.POST.get('ename')
            saver.etype=request.POST.get('etype')
            saver.save()
            messages.success(request,saver.ename+' is saved successfully')
        return render(request, "insert.html")
    return render(request,"insert.html")
    


def fd(request,edate):
    edate='2022-06-26'
    obj=eventadd.objects.filter(edate=edate)
    
#print(obj.values_list())

def likePost(request):   
    # post_id = request.GET.get('post_id')
    # print(post_id)
    # data = {
    # 'my_data':"data_to_display"
    # }
    # print(request)
    # return JsonResponse(data)


    edate = request.GET.get('text')   
    obj=eventadd.objects.filter(edate=edate)
    r=list(obj.values_list('etype'))
    print(r)
    data = {
        'test': r
        }
    return JsonResponse(data)


def date(request):  #for particular date(range)
    if request.method=="POST":
        if request.POST.get('date1') and request.POST.get('date2'):
            date1=request.POST.get('date1')
            date2=request.POST.get('date2')
            r=eventadd.objects.filter(edate__range=[date1, date2])
            k=list(r.values_list('etype'))
            result = (''.join(tup) for tup in k)
        return render(request, "date.html",{"da":result,"l":len(k)})
    return render(request,'date.html')
def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))
def type(request):      #for particuar type
    if request.method=="POST":
        if request.POST.get('type'):
            etype=request.POST.get('type')
            print(etype)
            r=eventadd.objects.filter(ename=etype)
            k=list(r.values_list('etype'))
            result = (''.join(tup) for tup in k)
        return render(request, "type.html",{"da":result,"l":len(k)})
    return render(request,'type.html')