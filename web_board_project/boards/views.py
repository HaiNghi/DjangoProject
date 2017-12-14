from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home(request):
    # return HttpResponse("Hello world!")
    boards=Board.objects.all()
    # boards_name= list()
    #
    # for board in boards:
    #     boards_name.append(board.name)
    #
    #     response_html='<br>'.join(boards_name)
    #
    # return HttpResponse(response_html)

    return render(request,'home.html',{'boards':boards})
# Create your views here.
