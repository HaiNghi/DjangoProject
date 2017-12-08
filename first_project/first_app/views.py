from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello world!")
    my_dict={'insert_me':'Iam nickie!'}
    return render(request,'index.html',context=my_dict)
# Create your views here.
def index2(request):
    # return HttpResponse("Hello world!")
    my_dict={'insert_me':'Iam nickie!'}
    return render(request,'index2.html',context=my_dict)