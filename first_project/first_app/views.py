from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,Webpage

# def index(request):
#     # return HttpResponse("Hello world!")
#     my_dict={'insert_me':'Iam nickie!'}
#     return render(request,'index.html',context=my_dict)
# # Create your views here.
def index(request):
    webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpage_list}
    return render(request, 'first_app/index.html', context=date_dict)
def index2(request):
    # return HttpResponse("Hello world!")
    my_dict={'insert_me':'Iam nickie!'}
    return render(request,'index2.html',context=my_dict)
