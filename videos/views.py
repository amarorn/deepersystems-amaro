from django.shortcuts import render, redirect
from videos.models import *
from videos.forms import *
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    v = Video.objects.all()
    return render(request,'index.html',{'video':v})

def like_button(request,like,id):
    Like.objects.create(video_id=id,like=like).save()

    return redirect('/')


def like_rank(request):
    rank = Like.objects.filter(like=0)
    rank1 = Like.objects.filter(like=1)
    video = Video.objects.all()

    a = []
    for v in video:
        a.append({'id': v.id,'theme':v.theme,'name':v.name,'qtd': 0})

    for r in rank:
        for i in a:
            if(i['id'] == r.video_id):
                i['qtd'] = i['qtd'] + 1
    for r1 in rank1:
        for i in a:
            if(i['id'] == r1.video_id):
                i['qtd'] = i['qtd'] + 1
    for i in a:
        if i['qtd'] > 0:
            i['qtd'] = i['qtd']/2

    sorted_list = sorted(a, key=lambda k: k['qtd'],reverse = True)
    return render(request, 'rank.html', {
        'rank': sorted_list
    })


def upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VideoForm()
    return render(request,'upload.html', {
        'form': form
    })

# def upload(request):
#     if request.method == "POST":
#         print(request.POST)
#         form = VideoForm(request.POST)
#         if form.is_valid():
#             name = request.POST['name']
#             theme = request.POST['theme']
#             video = request.FILES['video']
#             form.save()
#
#             return redirect('/')
#         else:
#             print(form.errors)
#             form = VideoForm()
#             print('Formulario ivalido')
#
#         return render(request,'upload.html',{'form':form})
