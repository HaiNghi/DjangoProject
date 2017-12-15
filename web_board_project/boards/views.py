from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, Http404
from .models import Board,Topic,Post
from .forms import NewTopicForm

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


def board_topics(request,pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
    # board=Board.objects.get(pk=pk)
    # return render(request,'topics.html',{'board':board})

def new_topic(request,pk):
    # board = get_object_or_404(Board,pk=pk)
    # if request.method== 'POST':
    #     newTopicForm= NewTopicForm(request.POST)
    #
    #     if newTopicForm.is_valid():
    #         subject=newTopicForm.cleaned_data.get('subject')
    #         message=newTopicForm.cleaned_data('message')
    #
    #         newTopic=Topic.objects.create(board=board,starter=User.objects.first(),subject=subject)
    #         newPost=Post.objects.create(message=message,topic=newTopic,created_by=User.objects.first())
    #
    #         return redirect('board_topics', pk=board.pk)
    # else:
    #     newTopicForm= NewTopicForm()
    # # board= get_object_or_404(Board,pk=pk)
    #
    # return render(request,'new_topic.html',{'board':board,'newTopicForm':newTopicForm})

        board = get_object_or_404(Board, pk=pk)
        user = User.objects.first()  # TODO: get the currently logged in user
        if request.method == 'POST':
            form = NewTopicForm(request.POST)
            if form.is_valid():
                topic = form.save(commit=False)
                topic.board = board
                topic.starter = user
                topic.save()
                post = Post.objects.create(
                    message=form.cleaned_data.get('message'),
                    topic=topic,
                    created_by=user
                )
                return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
        else:
            form = NewTopicForm()
        return render(request, 'new_topic.html', {'board': board, 'form': form})